from refugio import views
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tipo_rest', views.TipoList)
router.register('mascota_rest', views.MascotaList)
router.register('adoptante_rest', views.AdoptanteList)


urlpatterns = [
    path('api/', include(router.urls)),
    path('',views.base, name='base'),
    path('refugio/tipo/',views.tipo,name="tipo"),
    path('refugio/tipo/<int:tipo_id>/detail', views.tipo_detail, name="tipo-detail"),
    path('refugio/mascota/', views.MascotaListView.as_view(), name='mascota-list'),
    path('refugio/mascota/<int:pk>/detail', views.MascotaDetailView.as_view(), name='mascota-detail'),
    path('mascota/create/', views.MascotaCreate.as_view(), name='mascota-create'),
    path('mascota/<int:pk>/update/', views.MascotaUpdate.as_view(), name='mascota-update'),
    path('mascota/<int:pk>/delete/', views.MascotaDelete.as_view(), name='mascota-delete'),
    path('refugio/adoptante/', views.AdoptanteListView.as_view(), name='adoptante-list'),
    path('refugio/adoptante/<int:pk>/detail', views.AdoptanteDetailView.as_view(), name='adoptante-detail'),
    path('adoptante/create/', views.AdoptanteCreate.as_view(), name='adoptante-create'),
    path('adoptante/<int:pk>/update/', views.AdoptanteUpdate.as_view(), name='adoptante-update'),
    path('adoptante/<int:pk>/delete/', views.AdoptanteDelete.as_view(), name='adoptante-delete'),
    
]      