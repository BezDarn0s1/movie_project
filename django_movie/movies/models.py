from django.db import models
from datetime import date 


class Category(models.Model):
    '''Модель для категорий'''
    category_name = models.CharField(max_length=50, verbose_name="Название категории") 
    description = models.TextField(max_length=255, verbose_name="Описание категории")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.category_name

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    '''Модель для актёров и режиссёров'''
    name = models.CharField(max_length=50, verbose_name="Имя человека")
    age =  models.PositiveSmallIntegerField(default=0, verbose_name="Возраст человека")
    description = models.TextField(max_length=255, verbose_name="Описание человека")
    image = models.ImageField(upload_to="actors/", verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Актёры и режиссёры"
        verbose_name_plural = "Актёры и режиссёры"


class Genre(models.Model):
    '''Модель для жанров'''
    genre_title = models.CharField(max_length=50, verbose_name="Жанр")
    description = models.TextField(max_length=255, verbose_name="Описание жанра")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.genre_title

    class Meta():
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    '''модель для фильма'''
    movie_title = models.CharField(max_length=100, verbose_name="Название фильма")
    tagline = models.CharField(max_length=50, verbose_name="Слоган", default="")
    description = models.TextField(max_length=255, verbose_name="Описание фильма")
    poster = models.ImageField(upload_to="movies/", verbose_name="Постер фильма")
    release_year = models.PositiveSmallIntegerField(default=2022, verbose_name="Год выхода")
    country = models.CharField(max_length=50, verbose_name="Страна")
    directors = models.ManyToManyField(Actor, verbose_name="Режиссёр", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актёры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры фильма")
    warld_date_premiere = models.DateField(default=date.today, verbose_name="Премьера в мире")
    budhet = models.PositiveIntegerField(default=0, help_text="Указать сумму в долларах", verbose_name="Бюджет фильма")
    fees_in_usa = models.PositiveIntegerField(
        default=0, help_text="Указать сумму в долларах", verbose_name="Сборы в США"
    )
    fees_in_world = models.PositiveIntegerField(
        default=0, help_text="Указать сумму в долларах", verbose_name="Сборы в мире"
    )
    category_name = models.ForeignKey(Category, verbose_name="Категория фильма", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(default=False, verbose_name="Черновик")

    def __str__(self):
        return self.movie_title

    class Meta():
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    '''Модель для кадров из фильма'''
    shot_title = models.CharField(max_length=100, verbose_name="Заголовок кадра")
    description = models.TextField(max_length=255, verbose_name="Описание кадра")
    image = models.ImageField(upload_to="movie_shots/", verbose_name="Изображение кадра")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.shot_title

    class Meta():
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    '''Звезда рейтинга'''
    value = models.SmallIntegerField(verbose_name="Значение рейтинга", default=0)

    def __str__(self):
        return self.value

    class Meta():
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звёзды рейтинга"


class Rating(models.Model):
    '''Рейтинг'''
    ip = models.CharField(verbose_name="IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return f":{self.star} - {self.movie}"

    class Meta():
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    '''Отзовы'''
    email = models.EmailField()
    name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    feedback = models.TextField(max_length=1000, verbose_name="Отзыв")
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f":{self.name} - {self.movie}"

    class Meta():
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"










