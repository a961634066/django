# -*- coding:utf-8 -*-
from rest_framework import serializers

from appss.include_test.models import Shopping


class ShopSerializer(serializers.ModelSerializer):

    avg = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField(max_value=100)
    num = serializers.IntegerField(max_value=10000)


    class Meta:
        model = Shopping
        fields = "__all__"

    def get_avg(self, obj):
        print(type(obj))
        print(obj.__dict__)
        try:
            if "avg" in obj.__dict__.keys():
                avg = obj.avg
            else:
                avg = ""
        except:
            avg = "except"
        return avg