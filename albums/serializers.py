from rest_framework import serializers
from .models import Album


from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = [
            'id',
            'name',
            'year',
            'user',
        ]
        read_only_fields = ['user']

    def get_user(self, album):
        user = album.user
        serializer = UserSerializer(user)
        return serializer.data