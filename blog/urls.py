from django.urls import path
from .views import post_list, post_create, post_edit

urlpatterns = [path('', post_list, name='post_list'), path('edit/<int:post_id>/', post_edit, name='post_edit'),

               path('create/', post_create, name='post_create'),

                ]
