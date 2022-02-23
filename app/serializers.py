from dataclasses import field
from rest_framework import serializers
from .models import Mybook
class MybookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mybook
        fields = ['id','name','email','job','phone']
