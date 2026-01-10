from django.shortcuts import render
from .models import Property
from django.views.decorators.cache import cache_page
from django.http import JsonResponse as JSONResponse
from .utils import get_all_properties


# Create your views here.

@cache_page(60 * 15)  # Cache the view for 15 minutes
def property_list(request):   
 property_list = get_all_properties()

 property_data = [
  {
    "id": p.id,
    "title": p.title,
    "description": p.description,
    "price": float(p.price),
    "location": p.location,
    "created_at": p.created_at
  }
  for p in property_list
 ]

    

 return JSONResponse({
        "data": {
            "properties": property_data
        }
    })