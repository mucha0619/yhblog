from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)  #블로그와는 다르게 django 2.0 부터는 ForeignKey 항목에 on_delete 인자 필수
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now() # published_date 에 현시간을 할당
        self.save() # 변경된 데이터베이스를 저장

    def hide(self):
        self.published_date = None
        self.save()