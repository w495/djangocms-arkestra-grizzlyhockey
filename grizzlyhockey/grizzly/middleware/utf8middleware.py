
class Utf8Middleware(object):

    def process_response(self, request, response):
        response["Content-Type"] += "; charset=utf-8"
        return response
