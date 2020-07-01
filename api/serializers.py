from rest_framework import serializers

from api.models import Book, Press


class PressModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Press

        fields = ('id', 'press_name', 'address')


class BookModelSerializer(serializers.ModelSerializer):

    publish = PressModelSerializer()

    class Meta:
        model = Book
        fields = ('book_name', 'price', 'pic', 'pic_addr', 'publish')
        # fields = '__all__'
        # exclude = ('is_delete', 'create_time', 'status')  # 不展示的字段

        # depth = 1  # 查询深度


class BookModelDeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        fields = ('book_name', 'price', 'publish', 'authors')

        extra_kwargs = {
            'book_name': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'required': '图书名是必填的',
                    'min_length': '长度要大于2'
                }
            },
            'price': {
                'max_digits': 5,
                'decimal_places': 2,
                'error_messages': {
                    'max_digits': '价格总位数不要超过5位',
                    'decimal_places': '小数点后不要超过2位'
                }
            }
        }

    # 局部校验钩子
    def validate_book_name(self, value):
        return value

    def validate(self, attrs):
        return attrs


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
