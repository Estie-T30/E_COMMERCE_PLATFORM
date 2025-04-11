"""
URL configuration for Buckingham_Mall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from shop.views import product_list, product_create, product_update, product_delete, retrieve_product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', product_list, name='product-list'),
    path('create/', product_create, name='product-create'),
    path('update/<int:pk>/', product_update, name='product-update'),
    path('delete/<int:pk>/', product_delete, name='product-delete'),
    path('retrieve/<int:pk>/', retrieve_product, name='product-detail')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
