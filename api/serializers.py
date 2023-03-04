from rest_framework import serializers
from .models import Student


def start_with_u(value):
    if value[0].lower() != 'u':
        raise serializers.ValidationError('Name Should Start With "u" ')


# class StudentSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     name = serializers.CharField(max_length=100, validators=[start_with_u])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def validate_roll(self, value):
#         if value >= 1000:
#             raise serializers.ValidationError('Seat Full')

#         return value

#     # def validate(self,data):
#     #     nm=data.get('name')
#     #     ct=data.get('city')

#     #     if nm != 'uzair':
#     #         raise serializers.ValidationError('Name Must Be Uzair')

#     #     return data

#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[start_with_u])
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name']



    def validate_roll(self, value):
        if value >= 1000:
            raise serializers.ValidationError('Seat Full')

        return value

    