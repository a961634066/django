from django.db import models

# Create your models here.


class Shopping(models.Model):

    name = models.CharField(max_length=20)
    price = models.IntegerField()
    num = models.IntegerField()

    def __str__(self):
        return str(self.id) + self.name

    class Meta:
        ordering = ("id",)
        db_table = "include_shop"