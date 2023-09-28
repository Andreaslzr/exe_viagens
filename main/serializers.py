from rest_framework import serializers
from .models import *

class categoriaViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria_viagem
        fields = '__all__'
        many = True

class viagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = viagens
        fields = '__all__'
        many = True

class fotosViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = fotos_viagem
        fields = '__all__'
        many = True

class usuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = '__all__'
        many = True

class categoriaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria_pagamento
        fields = '__all__'
        many = True

class pagamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagamentos
        fields = '__all__'
        many = True

class reservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = reservas
        fields = '__all__'
        many = True

class comentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = comentarios_reserva
        fields = '__all__'
        many = True

class notasSerializer(serializers.ModelSerializer):
    class Meta:
        model = nota_reserva
        fields = '__all__'
        many = True