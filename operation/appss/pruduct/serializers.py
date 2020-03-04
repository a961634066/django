# -*- coding:utf-8 -*-
import time

from rest_framework import serializers

from appss.pruduct.models import Test, Student

"""
read_only:验证时不需要验证，但是返回时可以返回，此字段model中有
SerializerMethodField:某个字段不属于指定model，它是read_only，只需要将它序列化传递给用户，但是在这个model中，没有这个字段！我们需要用到SerializerMethodField。


"""

class TestSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20,min_length=3,required=True,error_messages={
        "max_length":"名字长度不能大于20",
        "min_length":"名字长度不能小于3",
        "required":"请填写名称",
    })
    age = serializers.IntegerField(required=True)
    sex = serializers.CharField()
    date_method = serializers.SerializerMethodField()
    # date_method1 = serializers.DateTimeField(format='%Y-%m-%d %H:%M')    格式化日期

    class Meta:
        model = Test
        fields = ("name", "age", "sex", "date_method")
        # fields = '__all__': 表示所有字段
        # exclude = ('add_time',):  除去指定的某些字段


    def get_date_method(self, obj):
        """
        命名：get + 字段名
        """
        return time.time() - 7 * 60


    def validate_age(self, age):
        """
        :param age:
        :return:
        自定义逻辑验证
        注意参数，self以及字段名
        注意函数名写法，validate_ + 字段名字
        """
        if age > 150:
            raise serializers.ValidationError("年龄非法")
        return age


class StudetSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=150)
    sex = serializers.CharField(max_length=150)

    # 有外键时，不显示为id，显示外键信息，需定义外键serializers，即ForKeySerializer，以下为举例
    # for_key = ForKeySerializer()
    class Meta:
        model = Student
        fields = "__all__"