from datetime import timezone

from django.shortcuts import render, redirect

# Create your views here.
from seat.models import Seat
from ticket.models import User_Ticket
from train_schedules.models import TrainSchedule
from ticket.models import Guest_Ticket


def final_check(request):
    departure_station = request.session.get('DepartureStation', None)
    arrival_station = request.session.get('ArrivalStation', None)
    train_number = request.session.get('Train_Number', None)
    train_type = request.session.get('Train_Type', None)
    departure_date = request.session.get('Departure_Date', None)
    room_num = request.session.get('Room_Num', None)
    departure_time = request.session.get('Departure_Time', None)
    arrival_time = request.session.get('Arrival_Time', None)
    seat_num = request.session.get('Seat_num', None)
    price = request.session.get('Price', None)
    departure_schedule_id = request.session.get('Departure_schedule_id', None)
    arrival_schedule_id = request.session.get('Arrival_schedule_id', None)
    passenger_cnt = request.session.get('Passenger_CNT_Input', None)


    if request.method == 'GET':
        context = {
            'departure_station': departure_station,  # 출발역
            'arrival_station': arrival_station,  # 도착역
            'train_number': train_number,  # 열차번호
            'train_type': train_type,  # 열차종류
            'room_num' : room_num, # 호차번호
            'seat_num' : seat_num, # 좌석 번호
            'departure_date' : departure_date, # 출발일
            'departure_time' : departure_time,
            'arrival_time' : arrival_time,
            'price' : price
        }
        return render(request, 'ticket/final_check.html', context)


    elif request.method == 'POST':
        # departure_schedule = TrainSchedule.objects.get(schedule_id=departure_schedule_id)
        # seat = Seat.objects.get(seat_num=seat_num, train_schedule=departure_schedule)
        # #회원일 경우
        if request.user.is_authenticated:
        #     # 훈련 스케줄과 좌석을 가져옵니다
        #
        #
        #     # User_Ticket 객체 생성 및 저장
        #     user_ticket = User_Ticket(
        #         user_id=int(request.user),  # 로그인된 유저
        #         departure_schedule=int(departure_schedule),
        #         seat_id=int(seat),
        #         passenger=int(passenger_cnt),
        #         created_at=timezone.now(),  # 현재 시간
        #         updated_at=timezone.now()
        #     )
        #
        #     user_ticket.save()  # DB에 저장

            # 승차권 저장 후 다른 페이지로 리다이렉트
            return redirect('/')
        # 비회원일 경우
        else:
            guest_user_id = request.session.get('guest_user_id', None)

            # guest_ticket = Guest_Ticket(
            #     user_id=request.user,
            #     departure_schedule=departure_schedule,
            #     seat_id=seat,
            #     passenger=passenger_cnt,
            #     created_at=timezone.now(),  # 현재 시간
            #     updated_at=timezone.now()
            # )

            # guest_ticket.save()  # DB에 저장

            return redirect('/')

from .models import User_Ticket
def my_ticket(request):
    room_num = request.session.get('Room_Num', None)
    seat_num = request.session.get('Seat_num', None)
    departure_station = request.session.get('DepartureStation', None)
    arrival_station = request.session.get('ArrivalStation', None)
    train_number = request.session.get('Train_Number', None)
    train_type = request.session.get('Train_Type', None)
    departure_schedule_id = request.session.get('Departure_schedule_id', None)
    departure_time = request.session.get('Departure_Time', None)
    arrival_time = request.session.get('Arrival_Time', None)
    arrival_schedule_id = request.session.get('Arrival_schedule_id', None)
    passenger_count = request.session.get('Passenger_CNT', None)
    if passenger_count != None:
        passenger_cnt = list(map(int, passenger_count.split(',')))
        total_passenger = sum(passenger_cnt)

    else:
        total_passenger = 1
    context = {
        'departure_station': departure_station,  # 출발역
        'arrival_station': arrival_station,  # 도착역
        'train_number': train_number,  # 열차번호
        'train_type': train_type,  # 열차종류
        'room_num': room_num,  # 호차 번호
        'total_psg': total_passenger,  # 총 승객 인원
        "seat_num" :seat_num,
        'departure_time' :departure_time,
        'arrival_time' : arrival_time

    }

    if request.method == 'GET':
        if request.user.is_authenticated:
            user_tickets = User_Ticket.objects.filter(user_id=request.user)
            return render(request, 'ticket/user_tickets.html', context)

        else:
            return render(request, 'ticket/pas.html',context)

    # elif request.method == 'POST':


def t(requset):
    return render(requset, "ticket/user_ticket2.html")

def tg(requset):
    return render(requset, "ticket/t3.html")