from django.db import models

# Create your models here.
class Link_Profile(models.Model):
    photo = models.ImageField(upload_to="")
    name=models.CharField(max_length=15)
    one_line=models.CharField(max_length=30)
    content=models.CharField(max_length=30) #사용자가 버튼을 누르면, 필드가 더 추가되고 지워지고... 어떻게 구현?

    def __str__(self):
        return self.name
