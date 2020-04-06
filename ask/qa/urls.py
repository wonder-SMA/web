from . import views
from django.urls import path

urlpatterns = [
        path('', views.test),
        path('login/', views.test),
        path('signup/', views.test),
        path('question/<int:pk>/', views.test),
        path('ask/', views.test),
        path('popular/', views.test),
        path('new/', views.test),
]
