from django.shortcuts import render

def units(request):
    return render(request, 'main/units.html', {})
