from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list),
    path('<int:id>/',views.post_detail),

]