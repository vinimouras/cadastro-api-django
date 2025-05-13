from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11, unique=True)

    cep = models.CharField(max_length=9)
    number = models.IntegerField()
    complement = models.CharField(max_length=50, blank=True, null=True)

    street = models.CharField(max_length=100, blank=True)
    neighborhood = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return "%s : %s" % (self.name, self.cpf)