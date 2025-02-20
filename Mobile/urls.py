from django.urls import path
from .views import *

urlpatterns = [
    path("", mobile_home, name="mobile_home"),
    path("create/", mobile_post_create, name="mobile_create"),
    path("<int:id>/detail/", mobile_post_detail, name="post_detail"),
    path("<int:id>/update/", mobile_post_update, name="post_update"),
    path("<int:id>/delete/", mobile_post_delete, name="post_delete")
]