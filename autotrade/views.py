from django.http import HttpResponse
from django.views import generic, View


class Home(generic.TemplateView):
    template_name = 'index.html'


class InternalErrorView(View):
    def get(self, request):
        return HttpResponse('Възникна неочаквана грешка, моля опитайте отново')
