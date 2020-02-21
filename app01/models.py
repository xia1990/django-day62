from django.db import models

#图书管理系统
class Publisher(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=64,unique=True)

