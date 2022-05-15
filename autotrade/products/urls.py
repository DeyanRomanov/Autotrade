from django.urls import path
from django.views.decorators.cache import cache_page

from autotrade.products.views.views_autotrade import AutotradeCreateCarView, AutotradeVehicleCreateView, \
    AutotradeVehicleView, AutotradeCreateTruckView, AutotradeCreateMotorcycleView, AutotradeCreatePartView, \
    AutotradeEditCarView, AutotradeDetailsCarView, AutotradeUsersProductView, AutotradeDetailsTruckView, \
    AutotradeEditTruckView, AutotradeDetailsMotorcycleView, AutotradeEditMotorcycleView, AutotradeDetailsPartView, \
    AutotradeEditPartView
from autotrade.products.views.views_car import CarCreateView, CarDetailsView, CarEditView, CarDeleteView
from autotrade.products.views.views_motorcycle import MotorcycleCreateView, MotorcycleDeleteView, MotorcycleDetailsView, \
    MotorcycleEditView
from autotrade.products.views.views_part import PartCreateView, PartEditView, PartDetailsView, PartDeleteView
from autotrade.products.views.views_reviews import CarStaffEditView, MotorcycleStaffEditView, TruckStaffEditView, \
    PartStaffEditView
from autotrade.products.views.views_truck import TruckCreateView, TruckDeleteView, TruckDetailsView, TruckEditView
from autotrade.products.views.views_vehicles import UserVehiclesView, UserAdvertisementView

urlpatterns = [
    path('create_car/', CarCreateView.as_view(), name='create car'),
    path('delete_car/<int:pk>/', CarDeleteView.as_view(), name='delete car'),
    path('details_car/<int:pk>/', CarDetailsView.as_view(), name='details car'),
    path('edit_car/<int:pk>/', CarEditView.as_view(), name='edit car'),

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
    path('user_advestisement/', cache_page(60*60*24*30)(UserAdvertisementView.as_view()), name='user advertisement'),
    path('autotrade_reviewers_page/', AutotradeUsersProductView.as_view(), name='advertisement to review'),

    path('autotrade_create_car/', AutotradeCreateCarView.as_view(), name='autotrade create car'),
    path('autotrade_details_car/<int:pk>/', AutotradeDetailsCarView.as_view(), name='autotrade details car'),
    path('autotrade_edit_car/<int:pk>/', AutotradeEditCarView.as_view(), name='autotrade edit car'),
    path('autotrade_create_truck/', AutotradeCreateTruckView.as_view(), name='autotrade create truck'),
    path('autotrade_details_truck/<int:pk>/', AutotradeDetailsTruckView.as_view(), name='autotrade details truck'),
    path('autotrade_edit_truck/<int:pk>/', AutotradeEditTruckView.as_view(), name='autotrade edit truck'),
    path('autotrade_create_motorcycle/', AutotradeCreateMotorcycleView.as_view(), name='autotrade create motorcycle'),
    path('autotrade_details_motorcycle/<int:pk>/', AutotradeDetailsMotorcycleView.as_view(),
         name='autotrade details motorcycle'),
    path('autotrade_edit_motorcycle/<int:pk>/', AutotradeEditMotorcycleView.as_view(),
         name='autotrade edit motorcycle'),
    path('autotrade_create_part', AutotradeCreatePartView.as_view(), name='autotrade create part'),
    path('autotrade_details_part/<int:pk>/', AutotradeDetailsPartView.as_view(), name='autotrade details part'),
    path('autotrade_edit_part/<int:pk>/', AutotradeEditPartView.as_view(), name='autotrade edit part'),

    path('autotrade_create_vehicle/', AutotradeVehicleCreateView.as_view(), name='autotrade create vehicles'),
    path('autotrade_edit_user_car/<int:pk>/', CarStaffEditView.as_view(), name='autotrade user edit car'),
    path('autotrade_edit_user_motorcycle/<int:pk>/', MotorcycleStaffEditView.as_view(),
         name='autotrade user edit motorcycle'),
    path('autotrade_edit_user_truck/<int:pk>/', TruckStaffEditView.as_view(), name='autotrade user edit truck'),
    path('autotrade_edit_user_part/<int:pk>/', PartStaffEditView.as_view(), name='autotrade user edit part'),
    path('autotrade_vehicles/', AutotradeVehicleView.as_view(), name='autotrade vehicles'),
    path('last_viewed_vehicles/', AutotradeVehicleView.as_view(), name='last viewed vehicles'),
]
