from rest_framework import serializers
from .models import Flowers
class FlowerSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Flowers
        fields=('sepal_length','sepal_width','petal_length','petal_width')
        
        