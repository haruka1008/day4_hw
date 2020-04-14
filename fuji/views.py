from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import DayCreateForm
from .models import Day

# Create your views here.

def Index(requests):
    return render(requests, 'fuji/day_list.html')

class AddView(generic.CreateView):
    template_name = 'fuji/day_form.html'
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('fuji:index')