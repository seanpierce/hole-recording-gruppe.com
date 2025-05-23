"""
URL configuration for hole_recording_gruppe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static

from hole_recording_gruppe import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('404', views.not_found, name='404'),
    path('releases/<str:catalog>', views.release, name='release'),
    path('download', views.bandcamp_download, name='download'),
    path('fme-video', views.redirect_fme_video, name="fme-video")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)