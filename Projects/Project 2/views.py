from django.shortcuts import render

def greeting_page(request):
    return render(request, 'greetings/index.html')
