from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from autotrade.userapp.forms import UserRegisterForm, ProfileEditForm, ProfileDeleteForm, CreateProfileForm
from autotrade.userapp.models import Profile, UserAppModel
from autotrade.common.mixins import UserPermissionAccessMixin, CurrentUserSaveProductMixin

from django.conf import settings
from django.core.mail import send_mail

UserModel = get_user_model()


# @receiver(signals.pre_save, sender=Profile)
# def send_email_after_register(instance, **kwargs):
#     subject = __SUBJECT_FOR_EMAIL
#     message = f'Добре дошли {instance.get_full_name}{__WELLCOME_MESSAGE}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [instance.email, ]
#     send_mail(subject, message, email_from, recipient_list)


class RegisterUser(generic.CreateView):
    __WELLCOME_MESSAGE = f', благодарим Ви, че се регистрирахте в нашия сайт. \
             Очакваме вашите запитвания, и предложения. При възникнали въпроси от Ваша страна , не се колебайте да се свържете \
                         с нашия управител Иван Иванов на тел.: 0888 888 888 !'

    __SUBJECT_FOR_EMAIL = 'Добре дошли в AUTOTRADE'

    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        # login after success register
        login(self.request, self.object)
        # send wellcome message
        user_mail = self.request.user.email
        send_mail(
            subject=self.__SUBJECT_FOR_EMAIL,
            message=f'{self.request.user.profile.get_full_name} {self.__WELLCOME_MESSAGE}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=(user_mail, ),
        )
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


class ProfileUserDeleteView(CurrentUserSaveProductMixin, mixins.LoginRequiredMixin, generic.DeleteView):
    model = UserAppModel
    form_class = ProfileDeleteForm
    template_name = 'user_profile_delete.html'
    success_url = reverse_lazy('home')


class AutotradeUsersView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'autotrade_users.html'
    model = UserModel
    paginate_by = 6
    context_object_name = 'autotrade_users'

    def get_queryset(self):
        return super(AutotradeUsersView, self).get_queryset().filter(is_staff=False).order_by('id')
