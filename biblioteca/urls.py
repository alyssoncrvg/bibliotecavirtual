from django.contrib import admin
from django.urls import path
from livros.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_livro, name='listar_livro'),
    path('cadastrargenero/', cadastro_genero, name='cadastro_genero'),
    path('cadastrarlivro/livro/', cadastro_livro, name='cadastro_livro'),
    path('livro/edit/<int:id>/', editar_livro, name='editar_livro'),
    path('genero/<int:id>/edit/', editar_genero, name='editar_genero'),
    path('livro/<int:id>/delete/', deletar_livro, name='deletar_livro'),
    path('deletargenero/<int:id>', deletar_genero, name='deletar_genero'),
    path('livro/<int:id>/', detail_livro, name='detail_livros'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)