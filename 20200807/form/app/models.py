from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=20, verbose_name='Mã')
    name = models.CharField(max_length=100, verbose_name='Tên')
    price = models.FloatField(verbose_name='Giá')
    image = models.ImageField(upload_to='static/images'
                        ,blank=True, verbose_name='Ảnh')
    def __str__(self):
        return self.name
