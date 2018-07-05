from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from .models import User
import gvcode
# Create your views here.


def index(request):
    return render(request,'user/index.html')

# 验证码
def get_code(request):
    base64_code,str_code=gvcode.base64()
    request.session['str_code']=str_code
    return HttpResponse(base64_code)

# 注册
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
        userExist = User.objects.filter(username=username).first()
        # 验证码
        str_code=request.session.get('str_code')
        verify_code =request.POST.get('verify_code')

        if username =="":
            msg='请输入用户名'
        elif userExist:
            msg='用户已存在'
        elif age== "" :
            msg='请输入年龄'
        elif password== "":
            msg="请输入密码"
        elif int(age) <=0:
            msg='年龄必须大于0'
        elif not verifypassword:
            msg='密码不相同'
        elif str_code.lower()!=verify_code.lower():
            msg='验证码错误'
        else:
            user = User(username=username,sex=sex,age=age,password=make_password(password))
            user.save()
            msg='注册成功'
            return render(request,'user/register_login.html',{"msg":msg})
        return render(request, 'user/register_login.html', {"msg": msg})

# 登录
def Userlogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=User.objects.filter(username=username).first()
        # user=authenticate(username,password)
        if username =='':
            msg="请输入用户名"
        elif user is None:
            msg="用户不存在"
        elif not check_password(password,user.password):
            msg="密码错误"
        else:
            login(request,user)
            msg="登录成功"
            return redirect(index)
        return render(request, 'user/register_login.html', {"msg": msg})
    elif request.method=='GET':
        return render(request,'user/register_login.html')

# 注销
def Userlogout(request):
    logout(request)
    msg="已注销,请重新登录"
    return render(request,'user/register_login.html',{"msg":msg})