from rest_framework import serializers
from main.models import MyField, MyArgument, MyClass, MyMethod

class MyFieldSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    access_modifier = serializers.CharField(max_length=30)
    data_type = serializers.CharField(max_length=30)
    field_name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        my_field = MyField(**validated_data)
        my_field.save()
        return my_field

    def update(self, instance, validated_data):
        instance.access_modifier = validated_data.get('access_modifier', instance.access_modifier)
        instance.data_type = validated_data.get('data_type', instance.data_type)
        instance.field_name = validated_data.get('field_name', instance.field_name)
        instance.save()
        return instance

class MyMethodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
