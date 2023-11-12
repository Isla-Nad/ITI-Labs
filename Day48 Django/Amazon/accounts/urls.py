from django.urls import include, path
from accounts.views import profile, AccountCreateView, AccountUpdateView, ProfileUpdateView,  CustomLoginView, CustomLogoutView, UserDeleteView, CustomPasswordChangeView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', profile, name='accounts.profile'),
    path('register/', AccountCreateView.as_view(), name='accounts.register'),
    path('edit/', AccountUpdateView.as_view(), name='accounts.edit'),
    path('edit/profile/', ProfileUpdateView.as_view(), name='profile.edit'),
    # path('delete/', user_delete, name='accounts.delete'),
    path('delete/', UserDeleteView.as_view(), name='accounts.delete'),
    path('password_change/', CustomPasswordChangeView.as_view(),
         name='password_change'),
]
