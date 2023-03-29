from django.shortcuts import render

from .models import Job
# Create your views here.

def all_jobs(request):
    all_jobs=Job.objects.all()
    context={'jobs':all_jobs}
    return render(request,'jobs/jobs.html',context)


def show_job(request,id):
    job=Job.objects.get(id=id)
    context={'job':job}
    return render(request,'jobs/job_details.html',context)