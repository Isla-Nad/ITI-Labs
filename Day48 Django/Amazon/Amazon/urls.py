"""
URL configuration for Amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products.views import index
# from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='products.index'),
    path('products/', include('products.urls')),
    path('contacts/', include('contacts.urls')),
    path('categories/', include('categories.urls')),
    path('accounts/', include('accounts.urls')),
    # path('<int:pk>/password/', PasswordChangeView.as_view(), name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
