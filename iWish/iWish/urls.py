"""
URL configuration for iWish project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_wish/', views.add_wish, name='add_wish'),
    path('confirm_delete/<int:wish_id>/', views.confirm_delete, name='confirm_delete'),
    path('accounts/login/', views.login_user, name='login'),  # Django's default login URL
    path('register/', views.register, name='register'),
    path('public_wish_list/<int:user_id>/', views.public_wish_list, name='public_wish_list'),
    path('wish_list/', views.wish_list, name='wish_list'),
    path('delete_wish/<int:wish_id>/', views.confirm_delete, name='delete_wish'),
    path('', lambda request: redirect('login'), name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

