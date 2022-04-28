import logging

from autotrade.views import InternalErrorView


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 405:
            logging.critical('Critical')
            logging.error('Info')
            logging.warning('Warning')
            logging.debug('Debug')
            return InternalErrorView.as_view()(request)

        return response

    return middleware
