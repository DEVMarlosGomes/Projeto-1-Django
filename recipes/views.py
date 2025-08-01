from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("<h1>Bem-vindo à página de receitas</h1>")

from django.shortcuts import render, get_object_or_404
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
def recipe_detail(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
