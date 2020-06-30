from django.urls import path

from api import views

urlpatterns = [
    path('book/', views.BookAPIView.as_view()),
    path('book/<id>/', views.BookAPIView.as_view()),

    path('v2/book/', views.BookAPIViewV2.as_view()),
    path('v2/book/<id>/', views.BookAPIViewV2.as_view()),
]
