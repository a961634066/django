# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    create_time = models.IntegerField(verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True)
    is_delete = models.CharField(max_length=1, default="0")

    class Meta:
        abstract = True


class Test(models.Model):

    SEX_CHOICES = (
        ("m","男"),
        ("w","女")
    )

    name = models.CharField(max_length=50, verbose_name="名称", help_text="姓名")
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices= SEX_CHOICES, verbose_name="性别")


    def __str__(self):
        return "%s" % self.name


    class Meta:
        db_table = 'pruduct_test'   # 自定义表名
        ordering = "id",     # 根据id排序
        verbose_name = "测试表"
        verbose_name_plural = "测试表"


class People(models.Model):
    peoples = models.CharField(max_length=150)
    card = models.CharField(max_length=150, unique=True)


class Student(models.Model):
    name = models.CharField(max_length=150)
    sex = models.CharField(max_length=150)
    number = models.CharField(max_length=150)


class Subject(models.Model):
    stu = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    kechengming = models.CharField(max_length=150)
    shichang = models.CharField(max_length=150)


class Teacher(models.Model):
    techer_name = models.CharField(max_length=150)
    # 最好自己定义第三章表
    stu = models.ManyToManyField(Student)


class Childre(BaseModel):

    name = models.CharField(max_length=100, unique=True, verbose_name="姓名")