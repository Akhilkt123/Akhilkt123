from django.shortcuts import render,redirect
from . models import task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class tasklistview(ListView):
    model=task
    template_name='home.html'
    context_object_name='obj'


class taskdetailview(DetailView):
    model=task
    template_name='details.html'
    context_object_name='res'

class taskupdateview(UpdateView):
    model=task
    template_name='update.html'
    context_object_name='result'
    fields=('name','priority','date')
    
    def get_success_url(self):
        return reverse_lazy('cdvdetails',kwargs={'pk':self.object.id}) 

class taskdeleteview(DeleteView):
    model=task
    template_name='delete.html'
    success_url=reverse_lazy('clvhome')


def add(request):
    res=task.objects.all()
    if request.method =='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        obj=task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'home.html',{'obj':res})

def delete(request,taskid):
    x=task.objects.get(id=taskid)
    if request.method =='POST':
        x.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    x=task.objects.get(id=id)
    f=todoform(request.POST or None, instance=x)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'x':x,'f':f})