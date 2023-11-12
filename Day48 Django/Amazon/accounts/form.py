from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.models import UserProfile


class AccountCreationForm(UserCreationForm):
    firstname = forms.CharField(
        max_length=30, required=True, help_text="Required. Enter your first name.")
    lastname = forms.CharField(
        max_length=30, required=True, help_text="Required. Enter your last name.")
    email = forms.EmailField(max_length=254, required=True,
                             help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname',
                  'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(AccountCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]
        if commit:
            user.save()
        return user


class AccountUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
