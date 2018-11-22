from django import forms

from user.helper import set_password
from user.models import User


class RegisterModelForm(forms.ModelForm):
    """注册表单,验证"""
    password1 = forms.CharField(max_length=16,
                                min_length=6,
                                error_messages={
                                    'required': '密码必填',
                                    'max_length': '密码长度不能大于16个字符',
                                    'min_length': '密码长度不能少于6个字符',
                                })
    password2 = forms.CharField(error_messages={'required': '确认密码必填'})

    class Meta:
        model = User
        fields = ['phone', ]

        error_messages = {
            "phone": {
                "required": "手机号码必填!"
            }
        }

    def clean_password2(self):
        # 验证两次密码
        pwd1 = self.cleaned_data.get('password1')
        pwd2 = self.cleaned_data.get('password2')
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError('两次密码不一致!')
        return pwd2

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        res = User.objects.filter(phone=phone).exists()
        if res:
            raise forms.ValidationError('手机号码已注册')
        return phone


class LoginFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'password', ]
        error_messages = {
            'phone': {
                'required': '帐号必填'
            },
            'password': {
                'required': '密码必填'
            }
        }

    def clean(self):  # 校验数据
        clean_data = self.cleaned_data
        # 获取数据
        phone = clean_data.get('phone')
        password = clean_data.get('password')
        # 如果数据合法 对数据进行比对
        if all([phone, password]):

            try:
                # 根据手机号获取用户
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                raise forms.ValidationError({'phone': '用户不存在,请仔细核对帐号'})
            # 判断密码是否正确
            if user.password != set_password(password):
                raise forms.ValidationError({'password': '密码错误'})

            # 正确  返回 user信息为了登陆是保存在session中提供数据,不用格外再取
            clean_data['user'] = user # 吧获取的user信息保存在清洗后的数据中
            return user
        else:
            return clean_data

