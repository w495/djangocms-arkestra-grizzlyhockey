# -*- coding: utf-8 -*-
import types

import time
import logging
import multiprocessing

from django.db import models
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
from django.db import connection

class Absabs(models.Model):
    '''
        Абстрактный объект
    '''
    ctime = models.DateTimeField(
        auto_now_add = True,
        verbose_name = u"ctime"
    )

    image = FilerImageField(
        blank = True,
        null = True,
        verbose_name = u"картинка"
    )


    def __pre_save_action_call(self, *args, **kwargs):
        if hasattr(self, 'pre_save_action'):
            if isinstance(self.pre_save_action, types.MethodType):
                return self.pre_save_action(*args, **kwargs)
        return  None


    def __post_save_action_call(self, *args, **kwargs):
        if hasattr(self, 'post_save_action'):
            if isinstance(self.post_save_action, types.MethodType):
                return self.post_save_action(*args, **kwargs)
        return  None

    def __async_save_action_wrapper(self, *args, **kwargs):
        logging.warning("async_save_action 1 %s"%(self.__class__))
        self.async_save_action(*args, **kwargs)
        ## Хак над особенностью работы с потоками в Python
        logging.warning("async_save_action 5 %s"%(self.__class__))


    def __async_save_action_call(self, *args, **kwargs):
        if hasattr(self, 'async_save_action'):
            if isinstance(self.async_save_action, types.MethodType):
                #connection.close()
                #multiprocessing.Process(target=self.__async_save_action_wrapper).start()
                return self.__async_save_action_wrapper(*args, **kwargs)
        return  None

    def resave(self, *args, **kwargs):
        result = None

        logging.warning("resave 1 %s"%(self.__class__))

        self.__pre_save_action_call(*args, **kwargs)
        result = super(Absabs, self).save(*args, **kwargs)
        self.__post_save_action_call(*args, **kwargs)

        logging.warning("resave 2 %s"%(self.__class__))

        self.__async_save_action_call(*args, **kwargs)

        logging.warning("resave 3 %s"%(self.__class__))

        return result

    def __async_resave_wrapper(self, *args, **kwargs):
        self.resave(*args, **kwargs)


    def async_resave(self, *args, **kwargs):
        #connection.close()
        #multiprocessing.Process(target=self.__async_resave_wrapper).start()
        return self.__async_resave_wrapper(*args, **kwargs)

    def save(self, *args, **kwargs):
        res = self.resave(*args, **kwargs)
        return res



    class Meta:
        abstract = True
        app_label = "grizzly"

