from datetime import date
import mimetypes
from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render 

from hole_recording_gruppe.helpers import scaffold_page_content
from releases.services import get_releases, get_release_by_catalog


 
def index(request):
    context = {
        **scaffold_page_content(None, request.build_absolute_uri('/')),
        'title': 'hole recording gruppe',
        'today': date.today(),
        'releases': get_releases()
    }

    return render(request, 'index.html', context)


def release(request, catalog):
    release = get_release_by_catalog(catalog)

    if not release:
        return redirect("/404")
    
    context = {
        **scaffold_page_content(release, request.build_absolute_uri('/')),
        'title': f'{release} | hole recording gruppe',
        'release': release,
    }

    return render(request, 'release.html', context)


def subscribe(request):
    context = {
        **scaffold_page_content(None, request.build_absolute_uri('/')),
        'title': 'hole recording gruppe',
    }
    return render(request, 'subscribe.html', context)


def redirect_fme_video(request):
    response = redirect('https://www.youtube.com/watch?v=zFPj-MX-ndk')
    return response


def not_found(request):
    context = {
        **scaffold_page_content(None, request.build_absolute_uri('/')),
        'title': 'hole recording gruppe',
        'release': release,
    }

    return render(request, '404.html', context)


def bandcamp_download(request):
    return redirect("https://hole-recording-gruppe.bandcamp.com/yum")


def serve_upload(request, filepath):
    root = Path(settings.UPLOADS_ROOT).resolve()
    target = (root / filepath).resolve()

    if not target.is_relative_to(root) or not target.is_file():
        raise Http404()

    return FileResponse(open(target, "rb"))


def serve_static(request, filepath):
    root = Path(settings.BASE_DIR, "assets").resolve()
    target = (root / filepath).resolve()

    if not target.is_relative_to(root) or not target.is_file():
        raise Http404()

    content_type, _ = mimetypes.guess_type(target.name)

    return FileResponse(
        open(target, "rb"),
        content_type=content_type or "application/octet-stream",
    )