from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LocationRequest

@api_view(['POST'])
def request_location(request):
    location = request.data.get('location')
    country = request.data.get('country')
    state = request.data.get('state')
    description = request.data.get('description', '')
    user_name = request.data.get('userName', '')
    user_email = request.data.get('userEmail', '')

    # Validate required fields
    if not location or not country:
        return Response(
            {'error': 'Location name and country are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    LocationRequest.objects.create(
        location=location,
        country=country,
        state=state,
        description=description,
        user_name=user_name,
        user_email=user_email,
    )
    return Response(
        {'message': 'Location request submitted successfully.'},
        status=status.HTTP_201_CREATED
    )
