from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'notebook_shop'
urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('home/', views.IndexPageView.as_view(), name='home'),
    path('catalog/', views.CatalogPageView.as_view(), name='catalog'),
    path('contacts/', views.ContactsPageView.as_view(), name='contacts'),
    path('goods/', views.GoodInfoView.as_view(), name='good'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)