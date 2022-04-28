import logging

from django.shortcuts import redirect
from django.urls import reverse_lazy


errors = [400, 403, 404]


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code in errors:
            return response
        elif response.status_code >= 400:
            logging.info('INFO')
            logging.critical('CRITICAL')
            logging.warning('WARNING')
            logging.error('ERROR')
            return redirect(reverse_lazy('home'))

        return response

    return middleware
