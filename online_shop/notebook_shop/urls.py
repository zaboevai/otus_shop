from django.urls import path

from . import views

app_name = 'notebook_shop'
urlpatterns = [
    # path('', views.index_view, name='index')
    path('', views.IndexPageView.as_view(), name='index'),
    path('home', views.IndexPageView.as_view(), name='home'),
    path('catalog', views.CatalogPageView.as_view(), name='catalog'),
    path('contacts', views.ContactsPageView.as_view(), name='contacts'),
    path('content/mi_air', views.MiAirPageView.as_view(), name='mi_air'),
    path('content/lenovo_330', views.LenovoPageView.as_view(), name='lenovo_330')

]

