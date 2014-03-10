from urlparse import urlparse

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from cms.models import CMSPlugin, Page

from filer.fields.image import FilerImageField

import mptt 

from arkestra_utilities.import_free_model_mixins import ArkestraGenericPluginItemOrdering
from arkestra_utilities.settings import PLUGIN_HEADING_LEVELS, PLUGIN_HEADING_LEVEL_DEFAULT
from links import schema


class LinkMethodsMixin(object):

    def __unicode__(self):
        return unicode(self.destination_content_object)
    
    def _smart_get_attribute_for_destination(self, field_basename):
        '''
        fetches the correct value based on override fields and the destination object
        wrapper:
          - check if the local model has a attribute named 'text_override', if
            it does and it has a value return that
          - lookup on the wrapped destination object to see if it has a value
        '''
        override_value = getattr(self, "%s_override" % field_basename, None)
        if override_value:
            return override_value
        value = getattr(self.wrapped_destination_obj, field_basename, '')
        return value
    
    @property
    def wrapped_destination_obj(self):
        # get the wrapped object
        return schema.get_wrapper(self.destination_content_object.__class__)(self.destination_content_object)
    
    """
    The properties of any link attribute - as in {{ link.attribute }} *must* be listed 
    here - otherwise, simply nothing will be returned.
    
    If an attribute matches:
    
    1.  is it an override attribute from the link instance? If so, use that. Otherwise:
    
    2.  look at the application's link_schema, and see what that returns. If there's nothing in there:
    
    3.  look at links.schema_registry.LinkWrapper. Returns the matching attribute from the model in the application's 
        link_schema; otherwise:
        
    4.  looks at widgetry.views.SearchItemWrapper and looks for the attribute there. If it matches, return that, or the fallback 
        
    """
    
    @property
    def text(self):
        return self._smart_get_attribute_for_destination('text')
    
    @property
    def short_text(self):
        return self._smart_get_attribute_for_destination('short_text')
    
    @property
    def url(self):
        return self._smart_get_attribute_for_destination('url')
    
    @property
    def heading(self):
        return self._smart_get_attribute_for_destination('heading')
    
    @property
    def description(self):
        return self._smart_get_attribute_for_destination('description')
    
    @property
    def image(self):
        return self._smart_get_attribute_for_destination('image')
    
    @property
    def optional_title(self):
        if self.html_title_element:
            return self.html_title_element
        else:
            return ""
        
    @property
    def metadata(self):
        return self._smart_get_attribute_for_destination('metadata')
    
    @property
    def thumbnail_url(self):
        return self._smart_get_attribute_for_destination('thumbnail_url')


class BaseLink(models.Model):
    """
    All links, whether placed using the Admin Inline mechanism or as plugins, require this information
    """
    destination_content_type = models.ForeignKey(ContentType, verbose_name="Type", related_name = "links_to_%(class)s") 
    destination_object_id = models.PositiveIntegerField(verbose_name="Item")
    destination_content_object = generic.GenericForeignKey('destination_content_type', 'destination_object_id')
    
    class Meta:
        abstract = True
        ordering = ['id',]


class Link(BaseLink, LinkMethodsMixin):
    """
    Abstract base class for link items as they appear in lists - used by ObjectLinks and links.GenericLinkListPluginItem
    """
    include_description = models.BooleanField(help_text=u"Also display metadata")
    text_override = models.CharField(verbose_name = "Link text, if required", 
        max_length=256, null=True, blank=True, 
        help_text="Will override the automatic default link text")
    description_override = models.TextField(max_length=256, null=True,
        blank=True, help_text="Will override the automatic default description text")
    heading_override = models.CharField(max_length=256, null=True, blank=True, 
        help_text="Will override the link destination's automatic default group heading")
    metadata_override = models.CharField(max_length=256, null=True, blank=True, 
        help_text="Override the link destination's default metadata")
    html_title_attribute = models.CharField(max_length=256, null=True, blank=True, 
        help_text="Add an HTML <em>title</em> attribute")
    key_link = models.BooleanField(help_text="Make this item stand out in the list")
    
    class Meta:
        abstract = True


class ObjectLink(Link):
    """
    When content_object object is rendered via its view, {% links %} in the template will display all the instances of this model that match its content_object field.
    """ 

    class Meta:
        verbose_name = "Link"

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id') # the content object the link is attached to    

class GenericLinkListPluginItem(ArkestraGenericPluginItemOrdering, Link):
    """
    Similar to ObjectLink above, but this one isn't attached to an object such as a NewsArticle, but to a plugin.
    """
    plugin = models.ForeignKey("GenericLinkListPlugin", related_name="links_item")
    
    class Meta:
        ordering = ['inline_item_ordering', 'id',]


"""
As well as links to objects within the system, we need to maintain a database of links to external web resources 
"""
class ExternalLink(models.Model):
    """
    Links to external sites
    """
    title = models.CharField(max_length=256)
    # this would have unique = True, but it makes it too hard to migrate from databases with duplicates
    url = models.CharField(max_length=255)
    external_site = models.ForeignKey('ExternalSite', related_name="links",
        null=True, blank=True,
        on_delete=models.PROTECT
        )
    description = models.TextField(max_length=256, null=True, blank=True)
    kind = models.ForeignKey('LinkType', 
        blank=True, null = True, 
        on_delete=models.SET_NULL,
        related_name='links')
    
    class Meta:
        ordering = ['title',]
        
    def __unicode__(self):
        return self.title or self.url

        
    def get_absolute_url(self):
        return self.url

    def save(self, *args, **kwargs):
        # here we either find the ExternalSite to attach to, or create it if it doesn't exist
        # split url into component parts
        purl = urlparse(self.url)
    
        # apply scheme (clean() has already checked that it's permissible, but check again because we save in housekeeping too)
        try:
            self.kind = LinkType.objects.get(scheme = purl.scheme)
        except ObjectDoesNotExist:
            # don't save
            return

        # get domain name
        domain = purl.netloc.partition(":")[0]
                
        # if we can find an exact domain match, make that the one
        try:
            self.external_site = ExternalSite.objects.get(domain=domain)
        # if we can't, we'll have to make it
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            external_site = ExternalSite(domain=domain, site=domain)
            external_site.save()
            self.external_site = external_site
        super(ExternalLink, self).save(*args, **kwargs)
        

class LinkType(models.Model):
    scheme = models.CharField(
        max_length=50, 
        help_text=u"e.g. 'http', 'mailto', etc",
        unique=True
        )
    name = models.CharField(
        max_length=50, 
        help_text=u"e.g. 'Hypertext', 'email', etc"
        )
    
    def __unicode__(self):
        return self.scheme


class ExternalSite(models.Model):
    
    site = models.CharField(
        "site name",
        max_length=50,
        help_text = u"e.g. 'BBC News', 'Welsh Assembly Goverment', etc", 
        null = True
        )
    domain = models.CharField(
        "domain name",
        max_length=256, 
        null = True, 
        blank = True,
        help_text = u"Do not amend unless you know what you are doing", 
        )
    parent = models.ForeignKey('self', 
        blank=True, 
        null = True, 
        related_name='children'
        )
    
    class Meta:
        verbose_name = "domain"
        ordering = ['domain',]
    
    def __unicode__(self):
        # if this site is unnamed, let's see if it has a named ancestor
        if self.site == self.domain:
            # get a list of domains like: cf.ac.uk, ac.uk, uk
            for domain in self.get_ancestors(ascending = True):
                # has this one been given a name?
                if domain.site != domain.domain:
                    return domain.site                    
        return self.site
    
    def save(self):
        
        # to-do: strip off port, if it exists

        # find the domain's parent domain
        parent_domain = self.domain.partition(".")[-1]
        
        # assuming that this domain exists
        if not self.domain == "":
            try:
                # try giving it an existing parent
                self.parent = ExternalSite.objects.get(domain = parent_domain)
            except ObjectDoesNotExist:
                # no such parent? better create it
                parent = ExternalSite(domain = parent_domain, site = parent_domain)
                
                # check that it will have a domain attribute
                if parent.domain:
                    # save it, then assign a FK to it
                    parent.save()
                    self.parent = parent
            super(ExternalSite, self).save()
        else:
            # we won't create a nameless domain!
            pass


try:
    mptt.register(ExternalSite)
except mptt.AlreadyRegistered:
    pass


class GenericLinkListPlugin(CMSPlugin):
    INSERTION_MODES = (
        (0, u"Inline in text"),
        (1, u"Unordered List - <ul>"),
        (2, u"Paragraphs - <p>"),
        )
    insert_as = models.PositiveSmallIntegerField(choices = INSERTION_MODES, default = 1)
    use_link_icons = models.BooleanField(help_text = "Place an icon on each link below (links in lists only)")
    separator = models.CharField(help_text = "Applies to Inline links only; default is ', '", max_length=20, null = True, blank = True, default = ", ")
    final_separator = models.CharField(help_text = "Applies to Inline links only; default is ' and '", max_length=20, null = True, blank = True, default = " and ")

    def copy_relations(self, oldinstance):
        for plugin_item in oldinstance.links_item.all():
            plugin_item.pk = None
            plugin_item.plugin = self
            plugin_item.save()



class CarouselPlugin(CMSPlugin):
    """
    The carousel inserted into a Page
    """
    CAROUSEL_WIDTHS = (
        (u'Widths relative to the containing column', (
            (100.0, u"100%"),
            (75.0, u"75%"),
            (66.7, u"66%"),
            (50.0, u"50%"),
            (33.3, u"33%"),
            (25.0, u"25%"),
            )
        ),
        ('Deprecated - do not use', (
            (1.0, u'Full'),
            (1.33, u'Three-quarters of the page'),
            (1.5, u'Two-thirds of the page'),
            (2.0, u'Half of the page'),
            (3.0, u'One-third of the page'),
            (4.0, u'One-quarter of the page'),
            )
        ),
    )
    ASPECT_RATIOS = (
        (2.5, u'5x2'),
        (2.0, u'2x1'),
        (1.5, u'3x2'),
        (1.333, u'4x3'),
        (1.0, u'Square'),
        (.75, u'3x4'),
        (.667, u'2x3'),
    )

    name = models.CharField(max_length=50)
    width = models.FloatField(choices=CAROUSEL_WIDTHS, default=100.0)
    aspect_ratio = models.FloatField(null=True, blank=True,
         choices=ASPECT_RATIOS, default=1.5)
    #height = models.PositiveIntegerField(null=True, blank=True)

    def copy_relations(self, oldinstance):
        for plugin_item in oldinstance.carousel_item.all():
            plugin_item.pk = None
            plugin_item.plugin = self
            plugin_item.save()



class CarouselPluginItem(BaseLink, LinkMethodsMixin, ArkestraGenericPluginItemOrdering):
    """
    The item in a carousel - basically a Link, with an image
    """
    plugin = models.ForeignKey(CarouselPlugin, related_name="carousel_item")
    image = FilerImageField()
    link_title = models.CharField(max_length=35)    

    class Meta:
        ordering = ['inline_item_ordering', 'id',]

class FocusOnPluginEditor(CMSPlugin):
    heading_level = models.PositiveSmallIntegerField(choices = PLUGIN_HEADING_LEVELS, default = PLUGIN_HEADING_LEVEL_DEFAULT)

    def copy_relations(self, oldinstance):
        for plugin_item in oldinstance.focuson_item.all():
            plugin_item.pk = None
            plugin_item.plugin = self
            plugin_item.save()


class FocusOnPluginItemEditor(LinkMethodsMixin, BaseLink):
    plugin = models.ForeignKey(FocusOnPluginEditor, related_name="focuson_item")
    text_override = models.CharField(max_length=256, null=True, blank=True, 
        help_text="Override the default link text")
    short_text_override = models.CharField(max_length=256, null=True, blank=True, 
        help_text="Override the default Focus on title text")
    description_override = models.TextField(max_length=256, null=True, blank=True, 
        help_text = "Override the item's default description")
    image_override = FilerImageField(blank=True, null=True,)
