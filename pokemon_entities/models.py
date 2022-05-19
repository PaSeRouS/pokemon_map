from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    from_evolved = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    photo = models.ImageField(
        upload_to='pokemon',
        null=True,
        blank=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()