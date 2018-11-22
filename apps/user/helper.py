import hashlib
from django.conf import settings


def set_password(password):
    # 新的加密方式
    new_password = "{}{}".format(password, settings.SECRET_KEY)
    p = hashlib.md5(new_password.encode('utf-8'))
    return p.hexdigest()


def login(request, user):
    # 登陆保存session的方法
    # 将用户id和手机号码,保存到session中
    request.session['ID'] = user.pk
    request.session['phone'] = user.phone
    # request.session['head'] = user.head