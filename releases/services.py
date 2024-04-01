from .models import Release

def get_releases():
    releases = Release.objects.filter(published=True)
    return releases


def get_release_by_catalog(catalog: str) -> Release | None:
    try:
        release = Release.objects.get(catalog__iexact=catalog)
        return release
    except Release.DoesNotExist:
        return None