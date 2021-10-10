from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.index,name = 'home'),
    path('images/',views.images,name = 'images'),
    path('images/<int:pk>',views.image_spec,name = 'image'),
    path('images/copy/<int:pk>',views.image_spec_copy,name = 'image_copy'),
    path('category/<int:pk>',views.image_category,name = 'category'),
    path('search',views.search_images, name="search")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)