import thread
import os
import time
import uuid
import logging

from django.conf import settings


class ProfileMiddleware(object):

    time = 0

    def process_request(self, request):
        self.time = time.time()

    def process_response(self, request, response):

        response["X-Dtm"] = time.time() - self.time
        response["X-Pid"] = os.getpid()
        response["X-Tid"] = thread.get_ident()
        response["X-Rid"] = "%s"%(uuid.uuid4())



        return response
