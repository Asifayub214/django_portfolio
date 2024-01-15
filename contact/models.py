from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    message=models.TextField()
    img=models.FileField(upload_to="contact/",max_length=250,null=True,default=None)
# Create your models here.
