from django.db import models

# Create your models here.


class dipendente(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    descrizione = models.TextField()


    # da il tempo che abbiamo creato questa classe
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.nome + " " + self.cognome   


class lavoratore (models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    data_nascita = models.DateField()
    luogo_nascita = models.CharField(max_length=200)
    nazionalita = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    lingue = models.CharField(max_length=200)
    patente = models.CharField(max_length=200)
    patente_data = models.DateField()
    email = models.EmailField(max_length=200)
    descrizione = models.TextField()



    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.nome + " " + self.cognome


class lavoro (models.Model):
    nome = models.CharField(max_length=200)
    mansioni = models.CharField(max_length=200)
    luogo = models.CharField(max_length=200)
    descrizione = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=False)


    def __str__(self):
        return self.nome 

class esperienza (models.Model):
    azienda = models.CharField(max_length=200)
    luogo = models.CharField(max_length=200)
    mansioni = models.CharField(max_length=200)
    rettribuzione = models.CharField(max_length=200)
    periodo = models.CharField(max_length=200)
    descrizione = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.azienda + " " + self.periodo
    
class backup_person (models.Model):
    email = models.EmailField(max_length=200)
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.nome + " " + self.cognome 
  




