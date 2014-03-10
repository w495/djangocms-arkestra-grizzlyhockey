import multiselectfield

class MultiSelectField(multiselectfield.MultiSelectField):

    def get_internal_type(self):
        return "TextField"


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^semanticeditor\.fields\.MultiSelectField"])
