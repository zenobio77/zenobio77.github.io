from django.urls import path
from. import views

urlpatterns = [
    path('', views.paginaPrincipal, name='pagina-principal'),
    path('quemSomos', views.quemSomos, name='quem-somos'),
    path('servicos', views.servicos, name='servicos'),
]
