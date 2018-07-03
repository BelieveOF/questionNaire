from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from .models import Userinfo
import gvcode
# Create your views here.

# 验证码
def get_code(request):
    base64_code,str_code=gvcode.base64()
    request.session['str_code']=str_code
    return HttpResponse(base64_code)

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # 验证密码
        verifypassword = (password == password2)
        # 验证用户名
        userExist = Userinfo.objects.filter(username=username).first()
        # 验证码
        str_code=request.session.get('str_code')
        verify_code =request.POST.get('verify_code')
        if userExist:
            msg='用户已存在'
        elif sex is None or age is None or password is None or password2 is None or verify_code is None:
            msg='有空没填'
        elif int(age) <=0:
            msg='年龄必须大于0'
        elif not verifypassword:
            msg='密码不相同'
        elif str_code.lower()!=verify_code.lower():
            msg='验证码错误'
        else:
            user = Userinfo(username=username,sex=sex,age=age,password=make_password(password))
            user.save()
            msg='注册成功'
            return render(request,'user/register_login.html',{"msg":msg})
        return render(request, 'user/register_login.html', {"msg": msg})


def Userlogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=Userinfo.objects.filter(username=username).first()
        # user=authenticate(username,password)
        if user is None:
            return HttpResponse("用户不存在")
        elif not check_password(password,user.password):
            return HttpResponse("密码错误")
        else:
            # login(request,user)
            return HttpResponse("success")
    elif request.method=='GET':
        return render(request,'user/register_login.html')