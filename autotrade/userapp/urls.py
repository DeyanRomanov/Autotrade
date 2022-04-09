from django.urls import path
from django.views.generic import TemplateView
from autotrade.userapp.views import RegisterUser, UserLogin, UserLogout, ProfileDetailsView, ProfileEditView, \
    ProfileUserDeleteView, ChangeUserPasswordView, ProfileCreateView, AutotradeUsersView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('change_password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('change_password_done/', TemplateView.as_view(template_name='change_password_done.html'),
         name='change password done'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile_create/<int:pk>/', ProfileCreateView.as_view(), name='profile create'),
    path('profile_details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile_edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
    path('user_profile_delete/<int:pk>/', ProfileUserDeleteView.as_view(), name='profile user delete'),
    path('autotrade_users/', AutotradeUsersView.as_view(), name='users'),
]
