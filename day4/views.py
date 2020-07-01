from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets

from api.models import Book
from day4.models import User
from day4.serializers import BookModelSerializerV2, UserModelSerializer
from utils.response import APIResponse


class BookAPIView(APIView):

    def get(self, request, *args, **kwargs):
        book_list = Book.objects.filter(is_delete=False)
        data_ser = BookModelSerializerV2(book_list, many=True).data

        return APIResponse(results=data_ser)


class BookGenericAPIView(generics.GenericAPIView,
                         ListModelMixin,
                         RetrieveModelMixin,
                         CreateModelMixin,
                         UpdateModelMixin,
                         DestroyModelMixin):

    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializerV2
    # lookup_field = 'id'  # 指定获取单条信息的主键名称

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     book_obj = self.get_object()  # 获取单个
    #
    #     book_list = self.get_queryset()
    #     data_ser = self.get_serializer(book_list, many=True)
    #
    #     return APIResponse(results=data_ser.data)
    #
    # def book_list(self, request, *args, **kwargs):
    #     book_list = self.get_queryset()
    #     data_ser = self.get_serializer(book_list, many=True)
    #
    #     return APIResponse(results=data_ser.data)

    def post(self, request, *args, **kwargs):
        res = self.create(request, *args, **kwargs)
        return APIResponse(results=res.data)

    def put(self, request, *args, **kwargs):
        res = self.update(request, *args, **kwargs)
        return APIResponse(results=res.data)

    def patch(self, request, *args, **kwargs):
        res = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=res.data)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(http_status=status.HTTP_204_NO_CONTENT)


class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializerV2


class BookGenericViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializerV2

    def user_login(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_user_count(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserGenericViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserModelSerializer

    def register(self, request, *args, **kwargs):
        new_user = self.create(request, *args, **kwargs)
        if new_user:
            return APIResponse(data_message='注册成功')


class UserViewSet(viewsets.ViewSet):
    def login(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user_obj = User.objects.filter(username=username, password=password)
        if user_obj:
            return APIResponse(data_message='登录成功')
        return APIResponse(data_message='用户名或密码错误')
