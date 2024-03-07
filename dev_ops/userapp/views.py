from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def test_api(request):
    return Response({
        "api": "Looks all okay!!"
    })