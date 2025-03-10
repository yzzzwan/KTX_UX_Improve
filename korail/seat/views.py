from django.shortcuts import render, redirect

# Create your views here.
from .models import TrainSchedule, Room, Seat

def seat_view(request, room_num):
    if request.method == 'GET':
        departure_station = request.session.get('DepartureStation', None)
        arrival_station = request.session.get('ArrivalStation', None)
        train_number = request.session.get('Train_Number', None)
        train_type = request.session.get('Train_Type', None)
        departure_schedule_id = request.session.get('Departure_schedule_id', None)
        arrival_schedule_id = request.session.get('Arrival_schedule_id', None)
        passenger_count = request.session.get('Passenger_CNT', None)

        seat_num1 = ["1A", "2A", "3A", "4A", "5A",] # 좌석번호
        seat_num2 = [ "1B", "2B", "3B", "4B", "5B"]
        seats_status1= [True, True, True, True, True,] # 누적 좌석 상태
        seats_status2 = [ True, True, True, True, True]
        passenger_cnt = list(map(int, passenger_count.split(',')))
        total_passenger = sum(passenger_cnt)
        seat_status1 = [True, True, True, True, True, ]  # 현재 호차의 좌석상태
        seat_status2 = [True, True, True, True, True]
        # +30마다 다음역임.
        for schedule_id in range(int(departure_schedule_id), int(arrival_schedule_id), 30):


            # 스케줄에 해당하는 열차의 호차 3개 중 선택한 호차
            room = Room.objects.filter(schedule_id=schedule_id,room_num=room_num)
            # 선택한 호차의 좌석들
            seats = Seat.objects.filter(room_id__in=room)


            i=0
            print("new")
            roomd_ids=seats[0].room_id.room_id
            print(seats[0].seat_id)

            for seat in seats:
                print("@",seat.seat_id)
                print("@",seat.seat_status)

                if i<5:
                    if seat.seat_status == 'Available':
                        seat_status1[i] = True
                    else:
                        seat_status1[i] = False
                else:
                    a=i-5
                    if seat.seat_status == 'Available':
                        seat_status2[a] = True
                    else:
                        seat_status2[a] = False
                i+=1

            # 둘 다 true일때만 true -> &연산
            print("!1.",  seat_status1)
            seats_status1 = [a and b for a, b in zip(seats_status1, seat_status1)]
            seats_status2 = [a and b for a, b in zip(seats_status2, seat_status2)]
            print("@!!!",seats_status1)
            request.session['Room_ID'] = roomd_ids



        # print(seats_status)


        seats_data1 = zip(seats_status1, seat_num1)
        seats_data2 = zip(seats_status2, seat_num2)

        context = {
            'departure_station': departure_station,  # 출발역
            'arrival_station': arrival_station,  # 도착역
            'train_number': train_number,  # 열차번호
            'train_type' : train_type, # 열차종류
            'seats_data1': seats_data1, # 좌석 상태 리스트와 좌석 번호
            'seats_data2': seats_data2,  # 좌석 상태 리스트와 좌석 번호
            'room_num': room_num, # 호차 번호
            'total_psg' : total_passenger # 총 승객 인원
        }

        return render(request, 'seat/seat.html', context)

    elif request.method == 'POST':
        request.session['Room_Num'] = request.POST.get('Room_Num')
        request.session['Seat_num'] = request.POST.get('Seat_num')

        roomid = request.session.get('Room_ID', None)
        seatnum = request.session.get('Seat_num', None)
        seat = Seat.objects.get(room_id=roomid, seat_num=seatnum)
        print(roomid, seatnum)
        seat.seat_status = 'Reserved'
        seat.save()  # 상태 변경 후 저장




        return redirect('/final_check')


