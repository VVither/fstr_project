from django.db import models

class Coords(models.Model):
    """
    Модель координат перевала
    """
    latitude = models.FloatField(help_text="Широта")
    longitude = models.FloatField(help_text="Долгота")
    height = models.IntegerField(help_text="Высота")

class User(models.Model):
    """
    Модель данных о пользователе
    """
    email = models.CharField(max_length=255, unique=True, help_text="Электронная почта пользователя")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Номер телефона пользователя")
    first_name = models.CharField(max_length=255, blank=True, null=True, help_text="Имя пользователя")
    last_name = models.CharField(max_length=255, blank=True, null=True, help_text="Фамилия пользователя")
    otc = models.CharField(max_length=255, blank=True, null=True, help_text="Отчество пользователя")

class pereval_added(models.Model):
    """
    Модель данных о перевале
    """
    beautyTitle = models.CharField(max_length=255, help_text="Название перевала")
    title = models.CharField(max_length=255, help_text="Краткое название перевала")
    other_titles = models.CharField(max_length=255, blank=True, null=True, help_text="Другие названия перевала")
    connect = models.CharField(max_length=255, blank=True, null=True, help_text="Связь между перевалами")
    add_time = models.DateField(auto_now_add=True, help_text="Дата добавления перевала")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Пользователь добавивший перевал")
    coords_id = models.ForeignKey(Coords, on_delete=models.CASCADE, help_text="Координаты перевала")
    winter_level = models.CharField(max_length=4, help_text="Зимняя категория сложности")
    summer_level = models.CharField(max_length=4, help_text="Летняя категория сложности")
    autumn_level = models.CharField(max_length=4, help_text="Осенняя категория сложности")
    spring_level = models.CharField(max_length=4, help_text="Весенняя категория сложности")
    status = models.CharField(max_length=50, default="new", help_text="Статус перевала")

class images(models.Model):
    """
    Модель изображений
    """
    image_url = models.URLField(help_text="Ссылка на изображение")
    image_title = models.CharField(max_length=255, blank=True, null=True, help_text="Описание изображения")

class PerevalImage(models.Model):
    """
    Связка модель изображения и перевала
    """
    pereval = models.ForeignKey(pereval_added, on_delete=models.CASCADE, help_text="Перевал")
    images = models.ForeignKey(images, on_delete=models.CASCADE, help_text="Изображение")