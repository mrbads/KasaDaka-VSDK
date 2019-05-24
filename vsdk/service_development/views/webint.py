from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from ..models import UserInputCategory, SpokenUserInput

class IndexView(generic.ListView):
    """docstring for IndexView."""
    template_name = 'webint.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return UserInputCategory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = UserInputCategory.objects.filter(name__contains='orders')
        context['supply'] = UserInputCategory.objects.filter(name__contains='supply')
        return context

# def index(request):
#     category_list = UserInputCategory.objects.all()
#     context = { 'category_list': category_list, }
#     return render(request, 'webint.html', context)

class DetailView(generic.DetailView):
    """docstring for DetailView."""
    model = UserInputCategory
    template_name = 'detail.html'

    def get_queryset(self):
        return UserInputCategory.objects.all()

# def detail(request, category_name):
#     category = get_object_or_404(UserInputCategory, name=category_name)
#     return render(request, 'detail.html', {
#         'category': category,
#         'name': category_name
#         })

def delete(request, category_id):
    category = get_object_or_404(UserInputCategory, pk=category_id)
    try:
        selected_order = category.category.get(pk=request.POST['order'])
    except (KeyError, SpokenUserInput.DoesNotExist):
        return render(request, 'detail.html', {
            'userinputcategory': category,
            'error_message': "You didn't select a order"
        })
    else:
        selected_order.delete()
        return HttpResponseRedirect(reverse('service-development:detail', args=(category.id)))
