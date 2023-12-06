from django.shortcuts import render
from .models import Tabel
from django.contrib import messages
# Create your views here.
def main_function(request):
    if request.method =='POST':
        usern = request.POST.get('username')
        pasw = request.POST.get('password')

        #Validation From
        if not usern or not pasw:
            messages.error(request, 'Requead Uername and Password 💀', fail_silently=True)
            return render(request, 'Login-From.html')

        #User Exitis
        if Tabel.objects.filter(username=usern).exists():   
            messages.error(request, "Users Already exits 🥲")
            return render(request, 'Login-From.html')
        else:
            user_deta = Tabel(username=usern, password=pasw)
            user_deta.save()
            messages.success(request, 'Login Successfully 😊')
            return render(request, 'Login-From.html')
        
    else:
        return render(request, 'Login-From.html')
    return render(request, 'Login-From.html')



