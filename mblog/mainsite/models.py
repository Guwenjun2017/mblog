from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)  #标题
    slug = models.CharField(max_length = 200)   #网址
    body = models.TextField()                   #内容
    pub_date = models.DateTimeField(default = timezone.now)     #发表时间

    class Mete:
        ordering = ('-pub_date',)

    def __unicode__(self):              #使用unicode以支持中文标题
        return self.title
