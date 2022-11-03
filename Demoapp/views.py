from django.shortcuts import render, redirect

# Create your views here.
from Demoapp.forms import todoForm
from Demoapp.models import todo


def frontpg(request):
    return render(request,'index2.html')

def add_todo(request):
    # global dob
    form = todoForm()
    print(form)
    if request.method == 'POST':
        form = todoForm(request.POST)
        # date = request.POST.get('date')
        if form.is_valid():
            form.save()
            return redirect('frontpg')
    return render(request,'Add.html',{'form':form})

def viewf(request):
    data = todo.objects.all()
    return render(request, 'view.html', {'data': data})

def update(request,id):
    todos = todo.objects.get(id=id)
    form =todoForm(instance=todos)
    if request.method =='POST':
        form= todoForm(request.POST,instance=todos)
        if form.is_valid():
            form.save()
            return redirect('frontpg')
    return render(request,'update.html',{'form':form})

def delete(request,id):
        data=todo.objects.get(id=id)
        data.delete()
        return redirect('viewf')




