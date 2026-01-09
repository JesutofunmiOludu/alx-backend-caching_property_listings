from django.shortcuts import render
from .models import Property
from django.views.decorators.cache import cache_page
from django.http import JsonResponse as JSONResponse


# Create your views here.

@cache_page(60 * 15)  # Cache the view for 15 minutes
def property_list(request):   
 property_list = Property.objects.all().values('id', 'title', 'price', 'location', 'description')

    

 return JsonResponse({
        "data": {
            "properties": properties
        }
    })