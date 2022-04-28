from django.http import HttpResponse
from django.views import generic
from django import views
from django.views.generic import RedirectView


class Home(generic.TemplateView):
    template_name = 'index.html'


class InternalErrorView(views.View):
    def get(self, request):
        return RedirectView()
