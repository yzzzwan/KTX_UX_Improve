from django.shortcuts import render, redirect

# Create your views here.
from .models import TrainSchedule, Train
from seat.models import Room, Seat
from django.db import transaction
from django.http import HttpResponse
from datetime import datetime

def pr(request):
    if request.method == 'GET':
        departure_station = request.session.get('DepartureStation', None)
        arrival_station = request.session.get('ArrivalStation', None)
        departure_date = request.session.get('Departure_Date', None)
        passenger_count = request.session.get('Passenger_CNT', None)

        adult_price = 1000
        child_price = 700
        infant_price = 200
        old_price = 100

        passenger_cnt = list(map(int,passenger_count.split(',')))
        price = adult_price * passenger_cnt[0] + child_price * passenger_cnt[1] + infant_price * passenger_cnt[2] + old_price * passenger_cnt[3]
        request.session['Price'] = price

        # departure_station = request.GET.get('DepartureStation_Input')
        # arrival_station = request.GET.get('ArrivalStation_Input')
        # departure_date = request.GET.get('Departure_Date_Input')
        # passenger_count = request.GET.get('Passenger_CNT_Input')

        selected_date = request.session.get('Departure_Date')  # '2024년 12월 2일 (월요일)'
        format_date = ""
        for sd in selected_date:
            if sd=='년':
                format_date = format_date + '-'
                continue
            elif sd=='월':
                format_date = format_date + '-'
                continue
            elif sd==' ':
                continue
            elif sd == '일':
                break
            format_date = format_date + sd


        format_date = datetime.strptime(format_date, '%Y-%m-%d').date()


        # 출발역과 도착역에 해당하는 TrainSchedule 데이터를 가져옴
        departure_schedules = TrainSchedule.objects.filter(station=departure_station, departure_date=format_date)
        arrival_schedules = TrainSchedule.objects.filter(station=arrival_station, departure_date=format_date)

        # 두 스케줄에서 동일한 열차 ID를 가진 항목만 찾기
        common_schedules = []
        for dep_schedule in departure_schedules:
            for arr_schedule in arrival_schedules:
                if dep_schedule.train_id == arr_schedule.train_id:
                    # 정차 순서를 기준으로 출발지 > 도착지 순으로 정렬
                    if dep_schedule.stop_order < arr_schedule.stop_order:
                        # 출발 시간과 도착 시간을 계산
                        dep_time = datetime.combine(datetime.today(), dep_schedule.departure_time)
                        arr_time = datetime.combine(datetime.today(), arr_schedule.departure_time)

                        # 소요 시간 계산 (도착 시간 - 출발 시간)
                        time_diff = arr_time - dep_time
                        hours = time_diff.seconds // 3600
                        minutes = (time_diff.seconds // 60) % 60
                        time_required = f"{hours}시간 {minutes}분"

                        common_schedules.append({
                            'train_id': dep_schedule.train_id, # 열차 아이디
                            'train_number': dep_schedule.train_id.train_number, # 열차번호
                            'departure_station': departure_station, # 출발역
                            'departure_time': dep_schedule.departure_time.strftime('%H:%M'), # 출발시간 12시간제 -> 24시간제,
                            'arrival_station': arrival_station, # 도착역
                            'arrival_time': arr_schedule.departure_time.strftime('%H:%M'), # 도착시간 12시간제 -> 24시간제
                            'train_type': dep_schedule.train_id.train_type,  # 열차 종류,
                            "time_required": time_required, # 소요시간,
                            'departure_schedule_id' : dep_schedule.schedule_id,
                            'arrival_schedule_id': arr_schedule.schedule_id

                        })


        # html파일로 전달할 데이터들
        context = {
            'common_schedules': common_schedules, # 출발역 - 도착역 으로 갈 수 있는 조회된 열차 리스트
            'departure_station': departure_station, # 출발역
            'arrival_station': arrival_station, # 도착역
            'departure_date' : departure_date,
            'price' : price
        }

        return render(request, 'train_schedules/train_schedules.html', context)

    elif request.method == 'POST':
        request.session['Train_Number'] = request.POST.get('Train_Number')
        request.session['Train_Type'] = request.POST.get('Train_Type')
        request.session['Departure_Time'] = request.POST.get('Departure_Time')
        request.session['Arrival_Time'] = request.POST.get('Arrival_Time')
        request.session['Departure_schedule_id'] = request.POST.get('Departure_schedule_id')
        request.session['Arrival_schedule_id'] = request.POST.get('Arrival_schedule_id')

        # tn = request.session.get('Train_Number', None)
        # tt = request.session.get('Train_Type', None)
        return redirect('/seat_view/1')





#
#
# def db(request):
#     print("STARTTTTTTTTTTTTTT")
#
#     # scs = TrainSchedule.objects.all()
#     # 데이터 출력
#     # for sc in scs:
#     #     print(f"{sc.station},{sc.departure_time},{sc.stop_order},{sc.train_id_id}")
#
#     data = [['대전', '05:28:00', 1, 44, '2024-11-01'], ['대전', '05:28:00', 1, 44, '2024-11-02'], ['대전', '05:28:00', 1, 44, '2024-11-03'], ['대전', '05:28:00', 1, 44, '2024-11-04'],
#     # 데이터 처리
#     bulk_data = []
#     for row in data:
#         print(type(row[4]))
        # ForeignKey로 연결된 Train 객체 가져오기
        train = Train.objects.get(train_id=row[3])

        # TrainSchedule 객체 생성
        bulk_data.append(
            TrainSchedule(
                train_id=train,  # ForeignKey로 연결된 Train 객체
                station=row[0],  # 정차역
                departure_time=row[1],  # 출발 시간
                stop_order=row[2],  # 정차 순서
                departure_date=row[4],  # 출발일
            )
        )
    TrainSchedule.objects.bulk_create(bulk_data)
#     print(f"{len(bulk_data)}개의 데이터가 성공적으로 삽입되었습니다!")
#
#     return render(request, 'train_schedules/train_schedules.html')

# def roomdb(request):
#     seats_to_create = []
#     rooms = Room.objects.all()
#
#     for room in rooms:
#         for row in range(1, 6):  # 1A, 2A, 3A, 4A, 5A
#             for col in ['A', 'B']:
#                 seat_num = f"{row}{col}"
#                 seat = Seat(room_id=room, seat_num=seat_num, seat_status='Available')
#                 seats_to_create.append(seat)
#
#     batch_size = 500  # 배치 크기를 500으로 설정 (실제 크기는 조정 가능)
#
#     # 배치 크기로 나누어 bulk_create 호출
#     with transaction.atomic():  # 트랜잭션을 묶어 처리
#         for i in range(0, len(seats_to_create), batch_size):
#             Seat.objects.bulk_create(seats_to_create[i:i + batch_size])
#     return render(request, 'train_schedules/train_schedules.html')
# #
