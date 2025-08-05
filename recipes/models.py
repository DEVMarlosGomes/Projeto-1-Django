# recipes/models.py
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    cooking_time = models.IntegerField(help_text="Tempo em minutos")
    ingredients = models.TextField()
    instructions = models.TextField()
    # Novo campo para a imagem da receita
    # upload_to='recipes/' significa que as imagens serão salvas em MEDIA_ROOT/recipes/
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        # Define o nome da tabela no plural para o painel de administração
        verbose_name_plural = "Recipes"
