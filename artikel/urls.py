
from django.urls import path
from artikel.views import (
    admin_kategori_list,
    admin_kategori_tambah,
    admin_kategori_update,
    admin_kategori_delete,
    
    admin_artikel_list,
    admin_artikel_tambah,
    admin_artikel_update,
    admin_artikel_delete,
)

urlpatterns = [
    path('operator/kategori/list', admin_kategori_list, name='admin_kategori_list'),
    path('operator/kategori/tambah', admin_kategori_tambah, name='admin_kategori_tambah'),
    path('operator/kategori/update/<int:id_kategori>', admin_kategori_update, name='admin_kategori_update'),
    path('operator/delete/<int:id_kategori>', admin_kategori_delete, name='admin_kategori_delete'),

    path('operator/list', admin_artikel_list, name='admin_artikel_list'),
    path('operator/tambah', admin_artikel_tambah, name='admin_artikel_tambah'),
     path('operator/update/<int:id_artikel>', admin_artikel_update, name='admin_artikel_update'),
    path('operator/delete/<int:id_artikel>', admin_artikel_delete, name='admin_artikel_delete'),
  
]
