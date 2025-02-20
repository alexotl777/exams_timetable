from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_api.serializers import UserSerializer
from exams_api.utils import exception_handler


class RegisterUserView(APIView):
    @exception_handler('RegisterUserView.post')
    def post(self, request) -> Response:
        """
        Рега пользователя

        :param request: {'email':'str', 'password':'str'}
        :return: Response
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
