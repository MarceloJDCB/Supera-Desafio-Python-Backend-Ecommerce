from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True,
        allow_blank=True,
        allow_null=True,
        required=False
    )
    
    class Meta:
        model = User
        fields = '__all__'
    

class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        allow_blank=True,
        allow_null=True,
        required=False
    )
    
    class Meta:
        model = User
        fields = '__all__'
        

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance.set_password(None)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    raise exceptions.ValidationError("Account deactivated.")
            else:
                raise exceptions.ValidationError("Incorrect credentials.")
        else:
            raise exceptions.ValidationError(
                "Must provide both password and username")
        return data