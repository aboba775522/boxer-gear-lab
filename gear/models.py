from django.db import models

class Category(models.Model):
    """Категория экипировки (Перчатки, Шлемы, Капы, Бинты)"""
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL-метка")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

class EquipmentItem(models.Model):
    """Конкретная экипировка в каталоге"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название товара")
    brand = models.CharField(max_length=100, verbose_name="Бренд")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб.)")
    oz_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="Диапазон унций (для перчаток)")
    description = models.TextField(verbose_name="Характеристики и описание")
    affiliate_link = models.URLField(max_length=500, verbose_name="Реферальная ссылка для покупки")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на картинку")

    def __str__(self):
        return f"{self.brand} - {self.name}"

class UserQuizResult(models.Model):
    """Результаты прохождения теста пользователем (сохранение сессии/опроса)"""
    session_key = models.CharField(max_length=100, verbose_name="Ключ сессии")
    weight = models.PositiveIntegerField(verbose_name="Вес спортсмена (кг)")
    experience_level = models.CharField(max_length=50, verbose_name="Уровень подготовки")
    training_focus = models.CharField(max_length=100, verbose_name="Цель тренировок")
    budget = models.PositiveIntegerField(verbose_name="Бюджет (руб.)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата прохождения")

    def __str__(self):
        return f"Тест от {self.created_at.strftime('%Y-%m-%d %H:%M')} (Вес: {self.weight} кг)"