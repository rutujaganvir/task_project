from .models import *
from django import forms


class Schoolform(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"

class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    