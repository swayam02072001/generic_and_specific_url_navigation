from django.shortcuts import render

# Create your views here.
def two(request):
    return render(request, 'two.html')