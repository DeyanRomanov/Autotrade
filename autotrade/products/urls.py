from django.urls import path

from autotrade.products.views.views_autotrade import AutotradeCreateCarView, AutotradeVehicleCreateView, \
    AutotradeVehicleView
from autotrade.products.views.views_car import CarCreateView, CarDetailsView, CarsEditView, CarsDeleteView
from autotrade.products.views.views_motorcycle import MotorcycleCreateView, MotorcycleDeleteView, MotorcycleDetailsView, \
    MotorcycleEditView
from autotrade.products.views.views_part import PartCreateView, PartEditView, PartDetailsView, PartDeleteView
from autotrade.products.views.views_truck import TruckCreateView, TruckDeleteView, TruckDetailsView, TruckEditView
from autotrade.products.views.views_vehicles import UserVehiclesView, UserAdvertisementView

urlpatterns = [
    path('create_car', CarCreateView.as_view(), name='create car'),
    path('details_car/<int:pk>/', CarDetailsView.as_view(), name='details car'),
    path('edit_car/<int:pk>/', CarsEditView.as_view(), name='edit car'),
    path('delete_car/<int:pk>/', CarsDeleteView.as_view(), name='delete car'),

    path('create_motorcycle/', MotorcycleCreateView.as_view(), name='create motorcycle'),
    path('delete_motorcycle/<int:pk>/', MotorcycleDeleteView.as_view(), name='delete motorcycle'),
    path('details_motorcycle/<int:pk>/', MotorcycleDetailsView.as_view(), name='details motorcycle'),
    path('edit_motorcycle/<int:pk>/', MotorcycleEditView.as_view(), name='edit motorcycle'),

    path('create_truck/', TruckCreateView.as_view(), name='create truck'),
    path('delete_truck/<int:pk>/', TruckDeleteView.as_view(), name='delete truck'),
    path('details_truck/<int:pk>/', TruckDetailsView.as_view(), name='details truck'),
    path('edit_truck/<int:pk>/', TruckEditView.as_view(), name='edit truck'),

    path('create_part/', PartCreateView.as_view(), name='create part'),
    path('delete_part/<int:pk>/', PartDeleteView.as_view(), name='delete part'),
    path('details_part/<int:pk>/', PartDetailsView.as_view(), name='details part'),
    path('edit_part/<int:pk>/', PartEditView.as_view(), name='edit part'),

    path('user_vehicles/', UserVehiclesView.as_view(), name='user vehicles'),
    path('user_advestisement/', UserAdvertisementView.as_view(), name='user advertisement'),

    path('autotrade_advestisement/', AutotradeCreateCarView.as_view(), name='autotrade create cars'),
    path('autotrade_vehicle_create/', AutotradeVehicleCreateView.as_view(), name='autotrade create vehicles'),
    path('autotrade_vehicles/', AutotradeVehicleView.as_view(), name='autotrade vehicles'),
]
