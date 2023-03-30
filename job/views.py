from django.core.paginator import Paginator
from django.shortcuts import render , redirect
from django.urls import reverse
from .models import Job
from .form import ApplyForm , Addjob
# Create your views here.

def all_jobs(request):
    all_jobs=Job.objects.all()
    paginator = Paginator(all_jobs, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}
    return render(request,'jobs/jobs.html',context)


def show_job(request,slug):
    job=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job
            myform.save()
            return redirect('jobs')
    else:
        form=ApplyForm()
    context={'job':job , 'form':form}
    return render(request,'jobs/job_details.html',context)



def add_job(request):
    if request.method=='POST':
        form=Addjob(request.POST , request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owmer=request.user
            myform.save()
            return redirect('jobs')
    else:
       form=Addjob()
       return render(request,'jobs/add_job.html', context={'form':form})
