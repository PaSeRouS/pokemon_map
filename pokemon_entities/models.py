from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pokemons',
        verbose_name='Предыдущая эволюция')
    title = models.CharField(
        max_length=200,
        verbose_name='Имя на русском'
    )
    title_en = models.CharField(
        max_length=200,
        verbose_name='Имя на английском'
    )
    title_jp = models.CharField(
        max_length=200,
        verbose_name='Имя на японском'
    )
    photo = models.ImageField(
        upload_to='pokemon',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, 
        on_delete=models.CASCADE,
        verbose_name='Покемон'
    )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появился')
    disappeared_at = models.DateTimeField(
        verbose_name='Исчез',
        blank=True
    )
    level = models.IntegerField(
        verbose_name='Уровень',
        blank=True
    )
    health = models.IntegerField(
        verbose_name='Здоровье',
        blank=True
    )
    strength = models.IntegerField(
        verbose_name='Сила',
        blank=True
    )
    defence = models.IntegerField(
        verbose_name='Защита',
        blank=True
    )
    stamina = models.IntegerField(
        verbose_name='Выносливость',
        blank=True
    )