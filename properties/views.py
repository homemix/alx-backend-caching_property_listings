from django.http import JsonResponse

from properties.utils import get_all_properties


# @cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({"data": list(properties)}, safe=False)
