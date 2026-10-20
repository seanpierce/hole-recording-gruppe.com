from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static

from hole_recording_gruppe import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('404', views.not_found, name='404'),
    path('releases/<str:catalog>', views.release, name='release'),
    path('download', views.bandcamp_download, name='download'),
    path('fme-video', views.redirect_fme_video, name='fme-video'),

    # Uploaded files
    re_path(r"^uploads/(?P<filepath>.+)$", views.serve_upload),

    # CSS, JavaScript, images
    re_path(r"^assets/(?P<filepath>.+)$", views.serve_static),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )