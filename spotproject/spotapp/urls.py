from django.urls import path
from . import views

app_name= "spotapp"

urlpatterns = [
    # これはトップ画面に遷移するpath
    path('', views.index, name="index"),
]
