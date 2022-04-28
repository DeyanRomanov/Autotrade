from django.views import generic


class Home(generic.TemplateView):
    template_name = 'index.html'


class InternalErrorView(generic.TemplateView):
    template_name = 'error.html'
