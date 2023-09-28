from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
import django_filters

# Create your views here.
'''class viagemFilter(django_filters.filterset):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = viagens
        fields = ['titulo']'''

'''class categoriaViagemView(APIview):'''

'''class viagens(APIView):'''

'''class fotoViagemView(APIView):'''

class usuariosView(ModelViewSet):
   queryset = usuarios.objects.all()
   serializer_class = usuariosSerializer 
   filter_backends = [DjangoFilterBackend]
   filterset_fields = ['nome',]
   permission_classes = (IsAuthenticated,)

class categoriaPagamentoView(ModelViewSet):
   queryset = categoria_pagamento.objects.all() 
   serializer_class = categoriaPagamentoSerializer
   filter_backends = [DjangoFilterBackend] 
   filterset_fields = ['nome',]
   permission_classes = (IsAuthenticated,)

class reservasView(ModelViewSet):
   queryset = reservas.objects.all() 
   serializer_class = reservasSerializer
   filter_backends = [DjangoFilterBackend] 
   filterset_fields = ['usuariofk',]
   permission_classes = (IsAuthenticated,)

class pagamentosView(ModelViewSet):
   queryset = pagamentos.objects.all() 
   serializer_class = pagamentosSerializer
   filter_backends = [DjangoFilterBackend] 
   filterset_fields = ['status','reservafk','usuariofk']
   permission_classes = (IsAuthenticated,)

'''class comentariosView(APIView):'''

'''class nostasView(APIView)'''


