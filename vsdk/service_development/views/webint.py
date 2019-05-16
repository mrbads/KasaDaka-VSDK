from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from ..models import UserInputCategory, SpokenUserInput

def index(request):
    category_list = UserInputCategory.objects.all()
    context = { 'category_list': category_list, }
    return render(request, 'webint.html', context)

def detail(request, category_name):
    category = get_object_or_404(SpokenUserInput, pk=category_name)
    return render(request, 'detail.html', {'category': category})
