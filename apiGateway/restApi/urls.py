from django.urls import path, include
from restApi import views

urlpatterns = [
    path('prediction/<str:market>/<str:ticker>/', views.PredictionView.as_view()),
]
