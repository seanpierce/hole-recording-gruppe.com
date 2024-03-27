from urllib import request
from releases.models import Release


def get_meta_desctiption(release: Release | None) -> str:
    """
    Helper method used to 'sanitize' the info content from a release into a string that is meta-tag friendly.
    First, turn line breaks into spaces, then replace double quotes with single quotes.
    Next, remove any instances of the '&nbps;' entity. Finally, only take the first 150 characters.
    If no release is supplied, method will return generic content.
    """

    generic_meta = 'Hole Recording Gruppe is a record label operating out of Portland, Oregon, USA.'

    try:
        if release is None:
            return generic_meta
        else:
            return release.info.replace('<br>', ' ').replace('"', '\'').replace('&nbsp;', '')[:150]
    except:
        return generic_meta
    

def get_meta_image(release: Release | None, host: str) -> str:
    """
    Helper method used to return a meta image based on the first image associated with a release.
    If no release is supplied, method wull return a generic image.
    """

    generic_image_path = f'{host}assets/images/logo-with-tagger.png'

    try:
        if release is None:
            return generic_image_path
        else:
            return f'{host}/{release.image_set.first().image.url}'
    except:
        return generic_image_path

    

def scaffold_page_content(release: Release | None, host: str) -> dict:
    """
    Helper method used to scaffold meta data used in the application's head template.
    """

    return {
        'meta_description': get_meta_desctiption(release),
        'meta_image': get_meta_image(release, host),
        'meta_url': host if release is None else f'{host}releases/{release.catalog}'
    }