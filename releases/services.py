from .models import Release, ReleaseImage

def get_releases():
    releases = Release.objects.all()
    return releases


def get_release_by_catalog(catalog):
    release = Release.objects.get(catalog=catalog)
    return release