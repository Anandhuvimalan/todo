from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView

# Create your views here.
class TaskView(ListView):
    model=Todo
    template_name='home.html'
    context_object_name='task_detail'

class TaskDetail(DetailView):
    model=Todo
    template_name='detail.html'
    context_object_name='task_detail'

class TaskUpdate(UpdateView):
    model=Todo
    template_name='classupdate.html'
    context_object_name='task_detail'
    fields=('name','priority','date')
    
    def get_success_url(self):
        return reverse_lazy('classdetail',kwargs={'pk':self.object.id})

class TaskDelete(DeleteView):
    model=Todo
    template_name='delete.html'
    success_url= reverse_lazy('classhome')


def add_task(request):
    task=Todo.objects.all()
    if request.method=='POST':
        task_name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        td=Todo(name=task_name,priority=priority,date=date)
        td.save()
    return render(request,'home.html',{'task_detail':task})

def delete_task(request,id):
    task=Todo.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update_task(request,id):
    task=Todo.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    context={
        'form':form,
        'task':task
    }
    return render(request,'update.html',context)