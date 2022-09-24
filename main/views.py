from django.shortcuts import render, redirect
from .models import *


def home_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        birth = request.POST.get("birth")
        image = request.FILES.get("image")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        Student.objects.create(
            name=name,
            birth=birth,
            image=image,
            phone=phone,
            email=email,
            address=address,
        )
        return redirect('home_view')
    context = {
        'student': Student.objects.all()
    }
    return render(request, 'home.html', context)
