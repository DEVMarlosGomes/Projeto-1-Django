from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Em minutos")

    def __str__(self):
        return self.title

## MEDIA_ROOT/recipes/
image = models.ImageField(upload_to='recipes/images/', blank=True, null=True)

def __str__(self):
        return self.title

class Meta:
     
     verbose_name_plural = 'Recipes'