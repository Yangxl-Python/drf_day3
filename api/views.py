from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Book
from api.serializers import BookModelSerializer, BookModelDeSerializer, BookModelSerializerV2


class BookAPIView(APIView):

    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book_obj = Book.objects.get(pk=book_id)
            book_ser = BookModelSerializer(book_obj)

            return Response({
                'status': status.HTTP_200_OK,
                'message': '查询成功',
                'result': book_ser.data
            })
        else:
            book_list = Book.objects.all()
            book_list_ser = BookModelSerializer(book_list, many=True)

            return Response({
                'status': status.HTTP_200_OK,
                'message': '查询成功',
                'result': book_list_ser.data
            })


    def post(self, request, *args, **kwargs):
        book_data = request.data
        book_des = BookModelDeSerializer(data=book_data)
        book_des.is_valid(raise_exception=True)
        new_book = book_des.save()

        return Response({
            'status': status.HTTP_200_OK,
            'message': '添加成功',
            'result': BookModelSerializer(new_book).data
        })


class BookAPIViewV2(APIView):

    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book_obj = Book.objects.filter(pk=book_id, is_delete=False)
            book_ser = BookModelSerializerV2(book_obj)

            return Response({
                'status': status.HTTP_200_OK,
                'message': '查询成功',
                'result': book_ser.data
            })
        else:
            book_list = Book.objects.filter(is_delete=False)
            book_list_ser = BookModelSerializerV2(book_list, many=True)

            return Response({
                'status': status.HTTP_200_OK,
                'message': '查询成功',
                'result': book_list_ser.data
            })

    def post(self, request, *args, **kwargs):
        book_data = request.data
        if isinstance(book_data, dict):
            many = False
        elif isinstance(book_data, list):
            many = True
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '请求参数格式有误',
            })
        book_des = BookModelSerializerV2(data=book_data, many=many)
        book_des.is_valid(raise_exception=True)
        new_book = book_des.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': '添加成功',
            'result': BookModelSerializerV2(new_book, many=many).data
        })

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:  # 单个
            ids = [book_id]
        else:  # 多个
            ids = request.data.get('ids')
        res = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        if res:
            return Response({
                'status': status.HTTP_200_OK,
                'message': '删除成功'
            })
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '删除失败'
            })

    def patch(self, request, *args, **kwargs):

        book_id = kwargs.get('id')
        book_data = request.data

        book_obj = Book.objects.get(pk=book_id)
        book_ser = BookModelSerializerV2(data=book_data, instance=book_obj, partial=True)
        book_ser.is_valid(raise_exception=True)
        book_ser.save()

        return Response({
            'status': status.HTTP_200_OK,
            'message': '更新成功',
            'result': BookModelSerializerV2(book_obj).data
        })

    # def put(self, request, *args, **kwargs):
    #     book_id = kwargs.get('id')
    #     book_data = request.data
    #
    #     book_obj = Book.objects.get(pk=book_id)
    #     book_ser = BookModelSerializerV2(data=book_data, instance=book_obj)
    #     book_ser.is_valid(raise_exception=True)
    #     book_ser.save()
    #
    #     return Response({
    #         'status': status.HTTP_200_OK,
    #         'message': '更新成功',
    #         'result': BookModelSerializerV2(book_obj).data
    #     })
