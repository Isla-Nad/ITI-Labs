from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, reverse, redirect
from accounts.form import AccountUpdateForm, AccountCreationForm, ProfileUpdateForm
from accounts.models import UserProfile
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User


def profile(request, pk):
    # user = request.user
    user = User.objects.get(pk=pk)
    user_profile = UserProfile.objects.get(user=user)
    context = {
        'user': user,
        'user_profile': user_profile,
    }
    return render(request, 'accounts/profile.html', context)


# def user_delete(request):
#     user = request.user
#     user.delete()
#     url = reverse('products.index')
#     return redirect(url)

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/confirm_delete.html'
    success_url = reverse_lazy('products.index')

    def get_object(self, queryset=None):
        return self.request.user


class AccountCreateView(CreateView):
    form_class = AccountCreationForm
    template_name = 'accounts/register.html'
    success_url = '/accounts/login/'


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AccountUpdateForm
    template_name = 'accounts/edit.html'

    def get_success_url(self):
        return reverse_lazy('accounts.profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('accounts.profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user.userprofile


class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('accounts.profile', kwargs={'pk': self.request.user.pk})


class CustomLogoutView(auth_views.LogoutView):
    template_name = 'registration/logged_out.html'
    next_page = 'products.index'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('accounts.profile', kwargs={'pk': self.request.user.pk})
