from rest_framework import serializers

from exams_api.models import Room, Exam


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    room_number = serializers.CharField(source='room.room_number', read_only=True)
    class Meta:
        model = Exam
        fields = ['id', 'subject_name', 'room_number']
