from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ServiceRequest

def service_request_list(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'service_requests/list.html', {'requests': requests})

def add_service_request(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        ServiceRequest.objects.create(title=title, description=description)
        return render(request, 'service_requests/partials/request_list.html', {'requests': ServiceRequest.objects.all()})
    return HttpResponse(status=400)