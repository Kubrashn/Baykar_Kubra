from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Kullanici_login(request):
    if request.method == 'POST':
        tc_no = request.POST.get("tc_no")  
        password = request.POST.get("password")

        user = authenticate(request, username=tc_no, password=password)  

        if user is not None:
            login(request, user)
            return redirect("uretim_paneli") 
        else:
            messages.error(request, "Geçersiz TC Kimlik No veya şifre")  # Hata mesajı

    return render(request, "login.html")


def Kullanici_logout(request):
    logout(request)
    return redirect('login')
