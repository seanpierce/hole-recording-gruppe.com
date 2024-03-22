
from django.shortcuts import render 

from releases.services import get_releases, get_release_by_catalog

 
def index(request):
    context = {
        'title': 'hole recording gruppe',
        'releases': get_releases()
    }

    return render(request, 'index.html', context)


def release(request, catalog):
    release = get_release_by_catalog(catalog)

    context = {
        'title': release,
        'release': release
    }

    return render(request, 'release.html', context)