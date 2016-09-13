from django.shortcuts import render
from .models import Post
from django.utils import timezone


def units(request):
    all_units = Post.objects.order_by('published_date')
    return render(request, 'main/units.html', {'all_units': all_units})
