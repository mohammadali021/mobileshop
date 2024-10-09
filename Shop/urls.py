from django.conf.urls.static import static
from django.urls import path

from Shop import views
from djangoProject import settings

urlpatterns = [
                  path('', views.index, name='index'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
