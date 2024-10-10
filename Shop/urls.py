from django.conf.urls.static import static
from django.urls import path

from Shop import views
from Shop.views import Mobile_Show
from djangoProject import settings

urlpatterns = [
                path('', views.index, name='index'),
                path('mobile-category/',views.Mobile_Category , name='mobile_category'),
                path('mobile-category/<slug:s>/' , views.Mobile_Show , name='mobile_show'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
