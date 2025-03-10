from django.db import models

# Create your models here.
from django.db import models

class Train(models.Model):
    train_id = models.AutoField(primary_key=True)  # 열차 아이디 (PK)
    train_type = models.CharField(max_length=100)  # 열차 종류 (예: KTX, 무궁화 등)
    train_number = models.CharField(max_length=20)  # 열차 번호 (예: 101, 102, ...)

    class Meta:
        db_table = 'train'  # 테이블 이름
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'

class TrainSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)  # 자동 증가하는 스케줄 ID (PK)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)  # 열차 아이디 (FK)
    station = models.CharField(max_length=100)  # 정차역
    departure_date = models.DateField()  # 출발일
    departure_time = models.TimeField()  # 출발 시간
    stop_order = models.IntegerField()  # 정차 순서 (예: 첫 번째 정차역은 1, 두 번째는 2...)

    class Meta:
        db_table = 'train_schedule'  # 테이블 이름
        verbose_name = 'Train Schedule'
        verbose_name_plural = 'Train Schedules'