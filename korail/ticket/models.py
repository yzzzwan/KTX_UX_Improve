from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from seat.models import Seat
from train_schedules.models import TrainSchedule
from user.models import Guest


class User_Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)  # 승차권 ID (PK, 자동 증가)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저 ID (FK)
    departure_schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE)  # 출발스케줄 ID (FK)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)  # 좌석 ID (FK)
    passenger = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # 승차권 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 승차권 수정 시간

    class Meta:
        db_table = 'user_ticket'  # 데이터베이스 테이블 이름

class Guest_Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)  # 승차권 ID (PK, 자동 증가)
    guest_id= models.ForeignKey(Guest, on_delete=models.CASCADE)  # 유저 ID (FK)
    departure_schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE)  # 출발스케줄 ID (FK)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)  # 좌석 ID (FK)
    passenger = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # 승차권 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 승차권 수정 시간

    class Meta:
        db_table = 'guest_ticket'  # 데이터베이스 테이블 이름

