from django.urls import path

from day4 import views

urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    path('books/<id>/', views.BookAPIView.as_view()),

    path('gen/', views.BookGenericAPIView.as_view()),
    path('gen/<pk>/', views.BookGenericAPIView.as_view()),

    path('list/', views.BookListAPIView.as_view()),
    path('list/<pk>/', views.BookListAPIView.as_view()),

    path('set/', views.BookGenericViewSet.as_view({'post': 'user_login', 'get': 'get_user_count'})),
    path('set/<pk>/', views.BookGenericViewSet.as_view({'post': 'user_login'})),

    path('register/', views.UserGenericViewSet.as_view({'post': 'register'})),
    path('login/', views.UserViewSet.as_view({'post': 'login'})),
]
