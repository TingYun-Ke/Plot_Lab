from django.urls import path
from . import views
# 調用特定的視圖函數
urlpatterns = [
    path("", views.plot, name="plot"),
]
