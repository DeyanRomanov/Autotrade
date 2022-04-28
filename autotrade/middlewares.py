import logging

from autotrade.views import InternalErrorView


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 500:
            logging.error('Info')
            return InternalErrorView.as_view()(request)

        return response

    return middleware
