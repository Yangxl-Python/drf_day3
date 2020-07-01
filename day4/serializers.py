from rest_framework import serializers

from api.models import Book
from day4.models import User


class BookListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        for index, obj in enumerate(instance):
            self.child.update(obj, validated_data[index])
        return instance


class BookModelSerializerV2(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('book_name', 'price', 'publish', 'authors', 'pic', 'pic_addr')
        extra_kwargs = {
            'pic': {
                'write_only': True
            },
            'pic_addr': {
                'read_only': True
            }
        }

        list_serializer_class = BookListSerializer

    def validate_book_name(self, value):
        print(self.context.get('request'))
        return value


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'username': {
                'max_length': 20,
                'min_length': 2
            },
            'password': {
                'max_length': 16,
                'min_length': 6
            }
        }
