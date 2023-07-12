from .models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"