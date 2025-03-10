from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # 해싱된 비밀번호를 저장할 필드

    def save(self, *args, **kwargs):
        # 비밀번호가 평문이라면 해싱 처리
        if not self.pk or not self.password.startswith('$'):  # 이미 해시된 비밀번호라면 다시 해시하지 않음
            self.password = make_password(self.password)  # 비밀번호 해싱
        super().save(*args, **kwargs)
