from django.core.cache import cache
from .models import Property

def get_all_properties():
    propertie = cache.get('all_properties')

    if propertie is None:

        propertie = list(Property.objects.all())

        cache.set('all_properties', propertie, 36000)

        return propertie
