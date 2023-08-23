from rest_framework import serializers
from api.models import profile

class profileSerializers(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'