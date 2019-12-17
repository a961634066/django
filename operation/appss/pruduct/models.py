# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Test(models.Model):

    SEX_CHOICES = (
        ("m","男"),
        ("w","女")
    )

    name = models.CharField(max_length=50, verbose_name="名称",unique=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices= SEX_CHOICES, verbose_name="性别")


    def __str__(self):
        return "%s" % self.name


    class Meta:
        db_table = 'test'   # 自定义表名
        ordering = "id",     # 根据id排序


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