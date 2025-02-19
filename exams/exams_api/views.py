from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_api.models import User
from exams_api.models import Exam
from exams_api.serializers import ExamSerializer


class ExamRegistrationView(APIView):
    def post(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        exam_ids = request.data.get('exam_ids', [])
        if not isinstance(exam_ids, list) or not all(isinstance(i, int) for i in exam_ids):
            return Response({'error': 'Invalid exam IDs format'}, status=status.HTTP_400_BAD_REQUEST)
        exams = Exam.objects.filter(id__in=exam_ids)
        if not exams:
            return Response({'error': 'Exams not found'}, status=status.HTTP_400_BAD_REQUEST)
        user.exams.add(*exams)
        return Response({'message': 'User registered for exams'})

    def delete(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        exam_ids = request.data.get('exam_ids', [])
        if not isinstance(exam_ids, list) or not all(isinstance(i, int) for i in exam_ids):
            return Response({'error': 'Invalid exam IDs format'}, status=status.HTTP_400_BAD_REQUEST)
        exams = Exam.objects.filter(id__in=exam_ids)
        if not exams:
            return Response({'error': 'Exams not found'}, status=status.HTTP_400_BAD_REQUEST)

        user.exams.remove(*exams)
        return Response({'message': 'User unregistered from exams'})

class ExamListView(APIView):
    def get(self, request):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

class UserInfoView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        return Response({'email': user.email, 'exams': list(user.exams.values_list('id', flat=True))})
