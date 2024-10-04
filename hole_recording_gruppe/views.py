
from datetime import date
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


def not_found(request):
    context = {
        **scaffold_page_content(None, request.build_absolute_uri('/')),
        'title': 'hole recording gruppe',
        'release': release,
    }

    return render(request, '404.html', context)


def bandcamp_download(request):
    return redirect("https://hole-recording-gruppe.bandcamp.com/yum")