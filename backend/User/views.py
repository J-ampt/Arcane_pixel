from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

from Utils.forms import RegistrationForm


class RegistrationView(APIView):
    def post(self, request):
        user = RegistrationForm(request.data)
        if not user.is_valid():
            return Response({'detail': user.errors.as_data()}, status=HTTP_400_BAD_REQUEST)
        user = user.save()
        return Response(
            {'detail': 'You have registered successfully'},
            status=HTTP_201_CREATED
        )
