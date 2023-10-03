from django.urls import path
from .import views

urlpatterns = [
    path('',views.addProduct,name='addProduct'),
    path('table',views.table,name='table'),
    path('addToDb',views.addToDb,name='addToDb'),
    path('edit',views.edit,name='edit'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('EditProduct/<int:pk>',views.EditProduct,name='EditProduct'),
    path('delete/<int:pk>',views.delete,name='delete')
]
