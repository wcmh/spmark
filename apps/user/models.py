from django.db import models
from db.base import BaseModel
from django.core.validators import RegexValidator


# Create your models here.


class User(BaseModel):
    """
    用户表
    """
    sex_choices = (
        (1, "男"),
        (2, "女"),
        (3, "保密"),
    )
    phone = models.CharField(max_length=11,
                             verbose_name="手机号码",
                             validators=[
                                 RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式错误')
                             ],
                             )

    nikname = models.CharField(max_length=50,
                               null=True,
                               blank=True,
                               verbose_name="昵称")
    password = models.CharField(max_length=32,
                                verbose_name="密码")
    gender = models.SmallIntegerField(choices=sex_choices,
                                      default=3,
                                      verbose_name="性别")
    school_name = models.CharField(max_length=200,
                                   verbose_name="学校信息")
    hometown = models.CharField(max_length=200,
                                verbose_name="家乡")
    birthday = models.DateField(null=True,
                                blank=True,
                                verbose_name="生日")
    address = models.CharField(max_length=200,
                               null=True,
                               blank=True,
                               verbose_name="家庭住址")

    def __str__(self):
        return self.phone

    class Meta:
        db_table = "user"
        verbose_name = "用户管理"
        verbose_name_plural = "用户管理"
