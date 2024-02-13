from django.shortcuts import render

# Create your views hede

def show(request):
    return render(request, 'post_details.html')