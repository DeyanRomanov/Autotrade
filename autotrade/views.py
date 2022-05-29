from django.db.models import Q
from django.views import generic

from autotrade.products.models import AutotradeCar, AutotradeTruck, AutotradeMotorcycle, AutotradePart


class Home(generic.TemplateView):
    template_name = 'index.html'


class SearchResultView(generic.ListView):
    model = AutotradeCar
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")

        cars = list(AutotradeCar.objects.filter(Q(mark__icontains=query) or Q(model__icontains=query)))
        trucks = list(AutotradeTruck.objects.filter(Q(mark__icontains=query) or Q(model__icontains=query)))
        motorcycles = list(AutotradeMotorcycle.objects.filter(Q(mark__icontains=query) or Q(model__icontains=query)))
        parts = list(AutotradePart.objects.filter(Q(name__icontains=query)))
        object_list = cars + trucks + motorcycles + parts

        return object_list
