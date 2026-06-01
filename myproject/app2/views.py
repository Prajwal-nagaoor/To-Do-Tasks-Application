from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=username, password=password)
        print(u)
        if u:
            login(request, u)
            return redirect('home')
        else:
            return render(request, 'login.html', {'status':True})
    return render(request, 'login.html')
def reg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        try:
            u = User.objects.get(username = username)
            return render(request, 'reg.html', {'username_exist':True, 'username':u})
        except:
            u = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username
            )
            u.set_password(password)
            u.save()
            return redirect('login_')
    return render(request, 'reg.html')
@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')
@login_required(login_url='login_')
def profile(request):
    return render(request, 'profile.html',{'profile':True})
@login_required(login_url='login_')
def reser_pass(request):
    user = request.user

    if request.method == 'POST':

        # STEP 1 - verify old password
        if request.POST.get("step") == "old_pass":
            old_pass = request.POST.get('old_pass')
            if authenticate(username=user.username, password=old_pass):
                return render(request, 'reset_pass.html', {'newpass': True})
            else:
                return render(request, 'reset_pass.html', {'oldpass': True})

        # STEP 2 - set new password
        elif request.POST.get("step") == "new_pass":
            new_pass = request.POST.get('new_pass')
            user.set_password(new_pass)
            user.save()
            return redirect('login_')

    return render(request, 'reset_pass.html')
def update_pro(request,pk):
    a = User.objects.get(id = pk)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        a.first_name = first_name,
        a.last_name = last_name,
        a.email = email,
        a.username = username,
        a.save()
        return redirect('profile')
    return render(request, 'update_pro.html', {'profile':a})
        
