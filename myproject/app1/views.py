from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app1.models import tasklist
from django.db.models import Q

# Create your views here.
@login_required(login_url='login_')

def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        print(q)
        task_details=tasklist.objects.filter(Q(title__contains=q) & Q(host=request.user) |Q(desc__contains=q)& Q(host=request.user))
        print(task_details)
    else:
        task_details=tasklist.objects.filter(Q(is_del=False) & Q(host=request.user))
    context = {
        'completed':True,
        'task_details':task_details
    }
    return render(request, 'home.html',context)
@login_required(login_url='login_')
def add(request):
    if request.method == 'POST':
        title = request.POST['task_name']
        desc = request.POST['task_desc']

        tasklist.objects.create(
            title = title,
            desc = desc,
            host = request.user
        )
        return redirect('home')

    return render(request, 'add.html', {'add_task':True})
def save_add(request):
    if request.method == 'POST':
        title = request.POST['task_name']
        desc = request.POST['task_desc']

        tasklist.objects.create(
            title = title,
            desc = desc,
            host = request.user
        )
        return redirect('add')

    return render(request, 'add.html', {'add_task':True})
@login_required(login_url='login_')
def details(request,pk):
    a = tasklist.objects.get(id = pk)
    return render(request, 'details.html',{'task_detail':a})
@login_required(login_url='login_')
def update(request,pk):
    a = tasklist.objects.get(id = pk)
    if request.method == 'POST':
        title = request.POST['task_name']
        desc = request.POST['task_desc']

        a.title = title
        a.desc = desc
        a.save()
        return redirect('home')
    return render(request, 'update.html',{'update':a})
@login_required(login_url='login_')
def delete_(request,pk):
    t = tasklist.objects.get(id = pk)
    t.is_del= True
    t.save()
    return redirect('home')
def completed(request,pk):
    t = tasklist.objects.get(id = pk)
    t.completed = True
    t.save()
    return redirect('comppleted')
@login_required(login_url='login_')
def history(request):
    a = tasklist.objects.filter(host=request.user)
    return render(request, 'history.html',{'task_details':a})
def comppleted(request):
    a = tasklist.objects.filter(host=request.user)
    context = {
        'completed':True,
        'task_details':a
    }
    return render(request, 'completed.html',context)
def uncompleted(request,pk):
    if 'q' in request.GET:
        q = request.GET['q']
        print(q)
        task_details=tasklist.objects.filter(Q(title__contains=q) & Q(host=request.user) |Q(desc__contains=q)& Q(host=request.user))
        print(task_details)
    else:
        task_details=tasklist.objects.filter(Q(is_del=False) & Q(host=request.user))
    t = tasklist.objects.get(id = pk)
    t.completed = False
    t.save()
    return redirect('home')
def restore(request,pk):
    t = tasklist.objects.get(id = pk)
    t.is_del = False
    t.save()
    return redirect('home')

def restore_all(request):
    t = tasklist.objects.all()
    for i in t:
        i.is_del = False
        i.save()
    return redirect('home')
def clear_all(request):
    t = tasklist.objects.all()
    t.delete()
    return redirect('history')
def delete_hist(request,pk):
    t = tasklist.objects.get(id = pk)
    t.delete()
    return redirect('home')