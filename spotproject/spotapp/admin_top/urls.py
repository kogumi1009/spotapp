from django.urls import path
from . import views

app_name= "spotapp"

urlpatterns = [
    # これは管理者（職員）のトップ画面に遷移するpath
    path('', views.index, name="index"),
]
