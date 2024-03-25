
from django.shortcuts import redirect, render 

from releases.services import get_releases, get_release_by_catalog

 
def index(request):
    context = {
        'title': 'hole recording gruppe',
        'releases': get_releases()
    }

    return render(request, 'index.html', context)


def release(request, catalog):
    release = get_release_by_catalog(catalog)

    if not release:
        return redirect("/404")

    context = {
        'title': release,
        'release': release
    }

    return render(request, 'release.html', context)


def not_found(request):
    context = {
        'title': 'hole recording gruppe | 404'
    }

    return render(request, '404.html', context)