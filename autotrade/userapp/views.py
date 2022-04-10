from django.conf import settings
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins
from django.core.mail import send_mail
from django.db.models import signals
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from autotrade.userapp.forms import UserRegisterForm, ProfileEditForm, ProfileDeleteForm, CreateProfileForm
from autotrade.userapp.models import Profile, UserAppModel
from common.mixins import UserPermissionAccessMixin

UserModel = get_user_model()

__WELLCOME_MESSAGE = f', благодарим Ви, че се регистрирахте в нашия сайт. \
         Очакваме вашите запитвания, и предложения. При възникнали въпроси от Ваша страна , не се колебайте да се свържете \
                     с нашия управител Николай Романов на тел.: 089 998 5421!'

__SUBJECT_FOR_EMAIL = 'Добре дошли в AUTOTRADE'

#
# @receiver(signals.pre_save, sender=Profile)
# def send_email_after_register(instance, **kwargs):
#     subject = __SUBJECT_FOR_EMAIL
#     message = f'Добре дошли {instance.get_full_name}{__WELLCOME_MESSAGE}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [instance.email, ]
#     send_mail(subject, message, email_from, recipient_list)


class RegisterUser(generic.CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        # after success registration send email for wellcome
        # https: // www.geeksforgeeks.org / setup - sending - email - in -django - project /
        # user_names = Profile.objects.get(pk=self.request.user.pk)
        # subject = self.__SUBJECT_FOR_EMAIL
        # message = f'Добре дошли {user_names.get_full_name}{self.__WELLCOME_MESSAGE}'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [self.request.user.email, ]
        # send_mail(subject, message, email_from, recipient_list)
        return result

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user advertisement')
        return super().dispatch(request, *args, **kwargs)


class ChangeUserPasswordView(auth_views.PasswordChangeView, mixins.LoginRequiredMixin):
    template_name = 'change_password.html'
    success_url = reverse_lazy('change password done')


class UserLogin(auth_views.LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('autotrade vehicles')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class UserLogout(auth_views.LogoutView, mixins.LoginRequiredMixin):
    template_name = 'logout.html'
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProfileCreateView(generic.CreateView):
    form_class = CreateProfileForm
    template_name = 'profile_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id})


class ProfileDetailsView(UserPermissionAccessMixin, mixins.LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profile_details.html'


class ProfileEditView(UserPermissionAccessMixin, mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'profile_edit.html'
    model = Profile
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id})


class ProfileUserDeleteView(generic.DeleteView):
    model = UserAppModel
    form_class = ProfileDeleteForm
    template_name = 'user_profile_delete.html'
    success_url = reverse_lazy('home')


class AutotradeUsersView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'autotrade_users.html'
    model = UserModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autotrade_users'] = UserModel.objects.filter(is_staff=False)
        return context
