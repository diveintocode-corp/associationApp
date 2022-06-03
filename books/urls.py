from django.urls import path
from . import views
app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:book_id>', views.detail, name='detail'),
    path('edit/<int:book_id>', views.edit, name='edit'),
    path('delete/<int:book_id>', views.delete, name='delete'),
]
