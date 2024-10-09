from django.db import models

# Create your models here.
#header model
class Header(models.Model):
    mobile_name = models.CharField(max_length=50 , verbose_name='نام موبایل به انگلیسی')
    mobile_name_fa = models.CharField(max_length=50 , verbose_name='نام موبایل به فارسی')
    short_description = models.CharField(max_length=500 , verbose_name='توضیحات کوتاه')
    image = models.ImageField(default='' , upload_to='media/' , null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.mobile_name
    class Meta:
        verbose_name = 'هدر سایت'
        verbose_name_plural = 'بخش مربوط به هدر سایت'