from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index=True) #Имя категории
    slug = models.SlugField(max_length=100, unique=True) #Представление для url в виде наименования, а не id

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория' #Translate to rus
        verbose_name_plural = 'Категории' #Plural
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) #Привязка категории товара к классу категорий

    name = models.CharField(max_length = 100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #Добавление изображения (флаг blank подтвержает, что изображение может не быть)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) #Создание цены с двумя знаками после запятой
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) #Создается дата создания
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
