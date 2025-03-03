from django.db import models
from django.apps import apps 

class Takim(models.Model):
    ad = models.CharField(max_length=100)

    def __str__(self):
        return self.ad

class Ucak(models.Model):
    ad = models.CharField(max_length=100)

    def __str__(self):
        return self.ad

class Parca(models.Model):
    takim = models.ForeignKey(Takim, on_delete=models.CASCADE)
    ucak = models.ForeignKey(Ucak, on_delete=models.CASCADE)
    parca_adi = models.CharField(max_length=100, default="")
    stok = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.parca_adi

class Uretim(models.Model):
    user = models.ForeignKey("users.Kullanici", on_delete=models.CASCADE)  
    parca = models.ForeignKey(Parca, on_delete=models.CASCADE)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.parca.parca_adi} - {self.tarih}"
