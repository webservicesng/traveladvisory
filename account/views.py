
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .forms import RegistrationForm
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout


from django.contrib import messages

# Create your views here.




def register_user(request):
    form = RegistrationForm(request.POST or None)
    
    email_exist = False
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = User.objects.get(email=form.email)
            # user = User.objects.filter(email=form.email).first()
            if user:
                email_exist = True
                messages.error(request, 'This user already exists. Check your email or login.') 

                print('this is the :', user.email, form.email)
            else:
                form.save() 
                messages.success(request, 'Successfully loged in ')
                
                return redirect('account:login')
            
        
        else:
            if email_exist ==True:
                messages.error(request, 'This user already exists. Check your email or login.') 
            else:
                messages.error(request, 'unsuccessful signup check your data or login to if you already have account ')
            

    context = {'form':form}
    return render(request, 'account/register.html', context)




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully loged in ')
            return redirect(reverse('mytravel:index'))
        else:
            messages.error(request, 'user not found')    
    return render(request, 'account/login.html')




def logout_user(request):
    logout(request)
    # return redirect(reverse('login'))
    return redirect("mytravel:index")
