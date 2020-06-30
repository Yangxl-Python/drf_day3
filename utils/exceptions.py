# 自定义异常处理
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception
from rest_framework import status


def exception_handler(exc, context):
    response = drf_exception(exc, context)
    if response is None:
        error_message = f'{context["view"]}, {context["request"].method}, {exc}'
        print(error_message)

        return Response({
            'error_msg': '程序失误了，请稍后再试'
        }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response


'''
Response(
    data=None, 响应数据
    status=None, 响应状态
    template_name=None, 渲染模板名称
    headers=None, 响应头
    exception=False, 是否异常
    content_type=None 内容格式
)
'''
