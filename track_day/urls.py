"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from booking_system import views as booking_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', include('booking_system.urls')),
    path('', booking_views.index, name='index'),
    path('about/', include('about.urls')),

    # Authentication
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='booking_system/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='index'),
        name='logout'
    ),
    path('signup/', booking_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]


# Errors
handler404 = 'booking_system.views.custom_404'
handler500 = 'booking_system.views.custom_500'
handler400 = 'booking_system.views.custom_400'
handler403 = 'booking_system.views.custom_403'
