from django.db import models
from django.utils.text import slugify


# Create your models here.
# open header-model
class Header(models.Model):
    mobile_name = models.CharField(max_length=50, verbose_name='نام موبایل به انگلیسی')
    mobile_name_fa = models.CharField(max_length=50, verbose_name='نام موبایل به فارسی')
    short_description = models.CharField(max_length=500, verbose_name='توضیحات کوتاه')
    image = models.ImageField(default='', upload_to='media/', null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.mobile_name

    class Meta:
        verbose_name = 'هدر سایت'
        verbose_name_plural = 'بخش مربوط به هدر سایت'



class Brands(models.Model):
    Brand_Name = models.CharField(max_length=50, verbose_name="نام برند")
    Brand_Image = models.ImageField(upload_to='media/', null=True, blank=True)
    slug = models.SlugField( default='',null=False , db_index=True)

    def __str__(self):
        return self.Brand_Name

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "نام برند"


class Categories(models.Model):
    Category_Name = models.CharField(max_length=50, verbose_name="دسته بندی")
    Category_Image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='تصویر')
    Category_Date = models.DateTimeField(auto_now_add=True , null=True, blank=True)
    Category_Slug = models.SlugField( null=False , db_index=True)



    def __str__(self):
        return self.Category_Name
    # def save(self, *args, **kwargs):
    #     self.Category_Slug = slugify(self.Category_Name)
    #     return super(Categories, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'دسته بندی محصولات'

class Mobile_Network(models.Model):
    Networks = models.CharField(max_length=5 , verbose_name="شبکه موبایل")
    def __str__(self):
        return self.Networks
    class Meta:
        verbose_name = "شبکه موبایل"
        verbose_name_plural = "شبکه موبایل"

class Mobile(models.Model):
    Name = models.CharField(max_length=50, verbose_name="نام موبایل")
    Name_fa = models.CharField(max_length=50, verbose_name="نام موبایل به فارسی")
    Size = models.CharField(max_length=10, verbose_name="اندازه ی محصول")
    Network = models.ForeignKey(Mobile_Network , null=True , blank=False , on_delete=models.CASCADE , related_name='Pro_Network' , verbose_name="شبکه")
    Ram = models.CharField(max_length=10, verbose_name="اندازه ی حافظه رم")
    Color = models.BooleanField(default=False, verbose_name="رنگ بندی")
    Guarantee = models.BooleanField(default=True, verbose_name="گارانتی")
    Special_opportunity = models.BooleanField(default=False, verbose_name="فرصت ویژه")
    Camera_resolution = models.CharField(max_length=100, verbose_name="رزولوشن دوربین")
    Price = models.CharField(max_length=10,verbose_name='قیمت محصول')
    Price_discount = models.BooleanField(default=False, verbose_name="تخفیف")
    PriceByDiscount = models.CharField(max_length=10,null=True , blank=True,verbose_name= 'قیمت تخفیف خورده ')
    Is_active = models.BooleanField(default=True, verbose_name='موجود')
    Image = models.ImageField(default='', upload_to='media/', null=True, blank=True, verbose_name='تصویر محصول')
    Brand = models.ForeignKey(Brands, null=True, blank=False, on_delete=models.CASCADE, related_name='Pro_Brand',
                              verbose_name='برند')
    Category = models.ForeignKey(Categories, null=True, blank=False, on_delete=models.CASCADE,
                                 related_name='Pro_Category', verbose_name="دسته بندی ")
    Slug = models.SlugField(default='', null=False, db_index=True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(str(self.Name))
        return super(Mobile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "موبایل"
        verbose_name_plural = "موبایل"

class Mobile_Accessory(models.Model):
    Name = models.CharField(max_length=50, verbose_name="نام محصول")
    # Name_fa = models.CharField(max_length=50, verbose_name="نام موبایل به فارسی")
    # Size = models.CharField(max_length=10, verbose_name="اندازه ی محصول")
    # Network = models.ForeignKey(Mobile_Network , null=True , blank=False , on_delete=models.CASCADE , related_name='Pro_Network' , verbose_name="شبکه")
    # Ram = models.CharField(max_length=10, verbose_name="اندازه ی حافظه رم")
    Color = models.BooleanField(default=False, verbose_name="رنگ بندی")
    Guarantee = models.BooleanField(default=True, verbose_name="گارانتی")
    Special_opportunity = models.BooleanField(default=False, verbose_name="فرصت ویژه")
    # Camera_resolution = models.CharField(max_length=100, verbose_name="رزولوشن دوربین")
    Price = models.CharField(max_length=10,verbose_name='قیمت محصول')
    Price_discount = models.BooleanField(default=False, verbose_name="تخفیف")
    PriceByDiscount = models.CharField(max_length=10,null=True , blank=True,verbose_name= 'قیمت تخفیف خورده ')
    Is_active = models.BooleanField(default=True, verbose_name='موجود')
    Image = models.ImageField(default='', upload_to='media/', null=True, blank=True, verbose_name='تصویر محصول')
    # Brand = models.ForeignKey(Brands, null=True, blank=False, on_delete=models.CASCADE, related_name='Pro_Brand',verbose_name='برند')
    Category = models.ForeignKey(Categories, null=True, blank=False, on_delete=models.CASCADE,
                                 related_name='Acces_Category', verbose_name="دسته بندی ")
    Slug = models.SlugField(default='', null=False, db_index=True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(str(self.Name))
        return super(Mobile_Accessory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "لوازم جانبی"
        verbose_name_plural = "لوازم جانبی"






