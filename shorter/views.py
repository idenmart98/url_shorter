from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Url
from .serializers import UrlCreateSerializer
from .utils import get_full_url


# Create your views here.

@api_view(['POST'])
def shorten_url(request):
    serializer = UrlCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        client_url = serializer.validated_data['origin_url']
        try:
            url = Url.objects.get(origin_url=client_url)
            return Response(status=status.HTTP_200_OK, data={"shortened_url": get_full_url(url)})
        except Url.DoesNotExist:
            instanse = serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={"shortened_url": get_full_url(instanse)})


@api_view(['GET'])
def redirect_origin_url(request, code):
    url =  get_object_or_404(Url,short_code=code)
    return HttpResponseRedirect(url.origin_url)





    
    
    