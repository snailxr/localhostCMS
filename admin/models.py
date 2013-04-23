# coding=utf-8
#model的日期设置，允许空设置，对应数据库字段名设置
from django.db import models
from datetime import datetime


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    USER_STATUS_CHOICES = (
        ('DISABLED', 'disabled'),
        ('OK', 'ok'),
    )
    #状态
    status = models.CharField(choices=USER_STATUS_CHOICES,blank=True,null=True,max_length=20)
    lastLogin = models.DateTimeField(blank=True,null=True,db_column='last_login')
    createdDate = models.DateTimeField(auto_now_add=True, blank=True, null=True,db_column='created_date')
    description = models.CharField(max_length=1000, blank=True,null=True)


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True,null=True)
    createdDate = models.DateTimeField(blank=True,auto_now_add=True,null=True,db_column='created_date')
    users = models.ManyToManyField(User)

