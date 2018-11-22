from django.conf.urls import url

from user.views import (LoginView,
                        RegisterView,
                        ForgetPasswordView,
                        InforView,
                        MemeberView,
                        Index,)

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),  # 绑定登陆路由
    url(r'^register/', RegisterView.as_view(), name='register'),  # 绑定注册路由
    url(r'^forget/', ForgetPasswordView.as_view(), name='forget'),  # 绑定忘记密码路由
    url(r'^infor/', InforView.as_view(), name='infor'),  # 绑定个人资料路由
    url(r'^memeber/', MemeberView.as_view(), name='memeber'),  # 绑定个人资料路由
    url(r'^$', Index.as_view(), name='index'),  # 绑首页
]
