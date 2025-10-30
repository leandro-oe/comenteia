from django.contrib import admin
from django.urls import path
from analise import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("cadastrar/", views.cadastrar, name="cadastrar"), # Atualise esta URL
    path("entrar/", views.entrar, name="entrar"),
    path("sair/", views.sair, name="sair"),
    path('analisar/', views.analisar_comentario_form, name="analisar"),
    path('historico/', views.historico, name="historico"),
    path('grafico/', views.grafico_sentimentos, name="grafico"),
    path('editar/<int:id>/', views.editar_comentario, name='editar_comentario'),
    path('deletar/<int:id>/', views.deletar_comentario, name='deletar_comentario'),
]
