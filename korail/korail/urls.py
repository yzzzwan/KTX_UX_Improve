"""
URL configuration for korail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import home.views
import train_schedules.views
import ms.views
import user.views
import seat.views
import ticket.views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home.views.index, name='index'), # 메인 홈

    # path('', train_schedules.views.roomdb), # db 데이터 넣을때 사용
    path('train_schedules', train_schedules.views.pr, name='train_schedules'), # 열차 스케쥴표

    # path('test', home.views.test,name="test"),
    # path('ms', ms.views.testms, name="using_session"),

    # user 관련 url
    path('user/signup', user.views.signup), # 회원가입
    path('user/login', user.views.login), # 로그인
    path('user/logout', user.views.logout), # 로그아웃
    path('user/guest', user.views.guest),  # 게스트 로그인

    # path('seats/', seat.views.seat_view, name='seat_view'),
    path('seat_view/<int:room_num>/', seat.views.seat_view, name='seat_view'),


    path('final_check/', ticket.views.final_check),
    path('myticket/', ticket.views.my_ticket),
    path('ticket/t', ticket.views.t),
    path('myticket/gf', ticket.views.tg)

]
