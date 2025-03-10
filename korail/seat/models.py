from django.db import models
from train_schedules.models import TrainSchedule

class Room(models.Model):
    # 호차 (Room) 모델
    room_id = models.AutoField(primary_key=True)  # 호차 ID (Primary Key)
    schedule_id = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE,db_column='schedule_id', related_name='rooms',)
    room_num = models.PositiveIntegerField()  # 호차 번호

    class Meta:
        db_table = 'room'  # 데이터베이스 테이블 이름
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Seat(models.Model):
    # 좌석 (Seat) 모델
    seat_id = models.AutoField(primary_key=True)  # 좌석 ID (Primary Key)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE,db_column='room_id', related_name='seat',)
    seat_num = models.CharField(max_length=10)  # 좌석 번호 (e.g., 1A, 2B)
    seat_status = models.CharField(
        max_length=20,  # 좌석 상태 (예: 'Available', 'Reserved')
        choices=[
            ('Available', 'Available'),
            ('Reserved', 'Reserved'),
        ],
        default='Available',
    )

    class Meta:
        db_table = 'seat'  # 데이터베이스 테이블 이름
        verbose_name = 'Seat'
        verbose_name_plural = 'Seats'

