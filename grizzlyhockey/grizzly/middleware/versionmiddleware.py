from django.conf import settings


class VersionMiddleware(object):

    def process_response(self, request, response):

        if(hasattr(settings, 'NODE_NAME')):
            response["X-Node-Name"] = settings.NODE_NAME

        if(hasattr(settings, 'VERSION')):
            response["X-Version"] = settings.VERSION

        if(hasattr(settings, 'SERVICE_VERSION')):
            response["X-Service-Version"] = settings.SERVICE_VERSION

        if(hasattr(settings, 'API_VERSION')):
            response["X-Api-Version"] = settings.API_VERSION

        return response
