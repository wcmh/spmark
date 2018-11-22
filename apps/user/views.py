from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

# class Index(View):
#     def get(self, request):
#         return render(request, 'user/index.html')
#
#     def post(self, request):
#         pass
from user.forms import RegisterModelForm, LoginFrom
from user.helper import set_password
from user.models import User


class LoginView(View):
    # 登陆
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        data = request.POST
        # 接收响应
        # 验证是否合法
        login_form = LoginFrom(data)
        # 判断是否合法
        if login_form.is_valid():
            #  获取所有数据
            user = login_form.cleaned_data.get('user')




class RegisterView(View):
    # 注册
    def get(self, request):
        return render(request, 'user/reg.html')

    def post(self, request):
        # 接收
        data = request.POST
        # 处理
        # 验证是否合法
        form = RegisterModelForm(data)
        if form.is_valid():
            # 处理,保存到数据库
            data = form.cleaned_data
            # 密码需要加密
            password = data.get('password2')

            password = set_password(password)

            User.objects.create(phone=data.get('phone'),password=password)
            return redirect('user:login')
        else:
            # 传递错误信息
            context = {
                "errors": form.errors
            }
        # 响应
        return render(request, 'user/reg.html', context)


class ForgetPasswordView(View):
    # 忘记密码
    def get(self, request):
        return render(request, 'user/forgetpassword.html')

    def post(self, request):
        return


class MemeberView(View):
    # 个人中心
    def get(self, request):
        return render(request, 'user/member.html')

    def post(self, request):
        return


class InforView(View):
    def get(self, request):
        return render(request, 'user/infor.html')

    def post(self, request):
        return


class Index(View):
    def get(self, request):
        return render(request, 'user/index.html')

    def post(self, request):
        return
