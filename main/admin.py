from django.contrib import admin
from .models import *

# Register your models here.

class detCategoriaViagem(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(categoria_viagem,detCategoriaViagem)

class detViagens(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(viagens,detViagens)

class detFotosViagem(admin.ModelAdmin):
    list_display = ('id', 'link')
    list_display_links = ('id', 'link')
    search_fields = ('viagemfk',)
    list_per_page = 10

admin.site.register(fotos_viagem,detFotosViagem)

class detUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(usuarios,detUsuarios)

class detCategoriaPagamento(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(categoria_pagamento,detCategoriaPagamento)

class detPagamentos(admin.ModelAdmin):
    list_display = ('id', 'dados')
    list_display_links = ('id', 'dados')
    search_fields = ('dados',)
    list_per_page = 10

admin.site.register(pagamentos,detPagamentos)

class detReservas(admin.ModelAdmin):
    list_display = ('id', 'usuariofk','viagemfk')
    list_display_links = ('id', 'usuariofk','viagemfk')
    search_fields = ('usuariofk','viagemfk')
    list_per_page = 10

admin.site.register(reservas,detReservas)

class detComentarios(admin.ModelAdmin):
    list_display = ('id', 'reservafk')
    list_display_links = ('id', 'reservafk')
    search_fields = ('reservafk',)
    list_per_page = 10

admin.site.register(comentarios_reserva,detComentarios)

class detNotas(admin.ModelAdmin):
    list_display = ('id', 'reservafk')
    list_display_links = ('id', 'reservafk')
    search_fields = ('reservafk',)
    list_per_page = 10

admin.site.register(nota_reserva,detNotas)