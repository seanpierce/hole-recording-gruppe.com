
from datetime import date
from django.shortcuts import redirect, render 

from releases.services import get_releases, get_release_by_catalog

 
def index(request):
    context = {
        'title': 'hole recording gruppe',
        'meta_description': 'Hole Recording Gruppe is a record label operating out of Portland, Oregon',
        'today': date.today(),
        'releases': get_releases()
    }

    return render(request, 'index.html', context)


def release(request, catalog):
    release = get_release_by_catalog(catalog)

    if not release:
        return redirect("/404")

    context = {
        'title': release,
        'release': release,
        'meta_description': release.info
            .replace('<br>', ' ') # turn line breaks into spaces
            .replace('"', '\'') # turn double quotes into single quotes
            .replace('&nbsp;', '') # remove the '&nbps;' entity
    }

    return render(request, 'release.html', context)


def not_found(request):
    context = {
        'title': 'hole recording gruppe | 404',
        'meta_description': 'Hole Recording Gruppe is a record label operating out of Portland, Oregon',
    }

    return render(request, '404.html', context)