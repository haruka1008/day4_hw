from django.urls import path
from . import views

app_name = 'fuji'

urlpatterns = [
    path('',views.Index, name='index'), # http://127.0.0.1:8000/fuji/
    path('add/',views.AddView.as_view(), name='add') # http://127.0.0.1:8000/fuji/add/
]