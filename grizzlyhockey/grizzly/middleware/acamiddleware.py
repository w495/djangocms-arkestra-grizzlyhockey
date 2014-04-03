from django.conf import settings


class AcaMiddleware(object):

    def process_response(self, request, response):

        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"

        return response
