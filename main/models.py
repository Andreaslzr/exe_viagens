from django.db import models
from django.utils import timezone
# Create your models here.

class categoria_viagem(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class viagens(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    valor_diaria = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    endereco = models.CharField(max_length=70)
    cidade = models.CharField(max_length=50)
    data_inicial = models.DateField()
    data_final = models.DateField()
    qtd_dias = models.IntegerField(default=1)
    categoriafk = models.ForeignKey(categoria_viagem, related_name="categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class fotos_viagem(models.Model):
    link = models.CharField(max_length=200)
    viagemfk = models.ForeignKey(viagens, related_name="viagemfk", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class usuarios(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField
    telefone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    
class categoria_pagamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class reservas(models.Model):
    usuariofk = models.ForeignKey(usuarios, related_name="usuario", on_delete=models.CASCADE)
    viagemfk = models.ForeignKey(viagens, related_name="viagem", on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now())
    valor_final = models.DecimalField(max_digits=10,decimal_places=2)
    quant_pessoas = models.IntegerField(default=1)
    animal = models.BooleanField(default=False)

    def __save__(self, *args, **kwargs):
        self.valor_final = self.viagemfk__valor_diaria * self.viagemfk__qtd_dias
        super(reservas, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

choices = (
    ("pendente","Pendente"),
    ("aprovada","Aprovada"),
    ("recusada","Recusada"),
)
    
class pagamentos(models.Model):
    dados = models.CharField(max_length=200)
    categoria = models.ForeignKey(categoria_pagamento, related_name="categoria_pag", on_delete=models.CASCADE)
    usuariofk = models.ForeignKey(usuarios, related_name="usuariofk", on_delete=models.CASCADE)
    status = models.CharField(choices=choices,max_length=50)
    reservafk = models.ForeignKey(reservas, related_name="reservapag", on_delete=models.CASCADE)


    def __str__(self):
        return self.name
       
class comentarios_reserva(models.Model):
    reservafk = models.ForeignKey(reservas, related_name="reservafk", on_delete=models.CASCADE)
    comentario = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class nota_reserva(models.Model):
    reservafk = models.ForeignKey(reservas, related_name="reserva", on_delete=models.CASCADE)
    nota = models.IntegerField()

    def __str__(self):
        return self.name