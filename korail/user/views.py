from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

# 회원가입 모듈
from user.models import Guest


def signup(request):
    if request.method == "GET":
        signupForm = UserCreationForm()
        context = {'signupForm' : signupForm}
        return render(request, 'user/signup.html', context)

    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)

        # 값이 있는지 체크
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()
            print("success")
        else:
            # 폼에 오류가 있으면 다시 렌더링하고 오류 메시지를 포함
            return render(request, 'user/signup.html', {'signupForm': signupForm})

        return redirect('/')
# 로그인 모듈
def login(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        context = {'loginForm' : loginForm}
        return render(request, 'user/login.html', context)

    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)

        # 값이 있는지 체크
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
            request.session['user_type'] = 'user'
        return redirect('/')

# 로그아웃 모듈
def logout(request):
    auth_logout(request)
    return redirect('/')

# 비회원 로그인 모듈
def guest(request):
    if request.method == "GET":

        return render(request, 'user/guest.html')

    elif request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')


        guest = Guest(name=name, phone=phone, password=password)
        guest.save()

        # 세션에 비회원 정보 저장
        request.session['user_type'] = 'guest'
        request.session['guest_name'] = name
        request.session['guest_phone'] = phone
        request.session['guest_password'] = password
        request.session['guest_user_id'] = guest.id


        return redirect('/train_schedules')


