from django.urls import path
from .views import article_list,article_detail,article_add,article_edit,article_delete,homepage,delete_comment


urlpatterns = [
    path('',homepage,name='home'),
    path('articles/',article_list,name='article_list'),
    path('articles/<int:id>/',article_detail,name='article_detail'),
    path('articles/add/',article_add,name='article_add'),
    path('articles/<int:id>/edit/',article_edit,name='article_edit'),
    path('articles/<int:id>/delete/',article_delete,name='article_delete'),
    path('articles/<int:id>/comment/delete',delete_comment,name='delete_comment')
]