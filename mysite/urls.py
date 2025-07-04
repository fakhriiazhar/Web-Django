from django.contrib import admin
from django.urls import path, include
from mysite.views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from mysite.authentication import login, logout, registrasi
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index,),
    path('artikel/<int:id>', detail_artikel, name='detail_artikel'),
    path('artikel-not-found', artikel_not_found, name='artikel-not-found'),
    path('kontak', kontak, name='kontak'),
    path('galeri', galeri, name='galeri'),
    
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/artikel-list', artikel_list, name='artikel_list'),
    
    path('dashboard/', include('artikel.urls')),

    
    #################### AUTHENTICATION #####################
    path('auth-login', login, name='login'),
    path('auth-logout', logout, name='logout'),
    path('auth-registrasi', registrasi, name='registrasi'),

    path('kategori/<int:kategori_id>/', artikel_by_kategori, name='artikel_by_kategori'),
]

################ Untuk Media ##########################
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)