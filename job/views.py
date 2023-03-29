from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Job
# Create your views here.

def all_jobs(request):
    all_jobs=Job.objects.all()
    paginator = Paginator(all_jobs, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}
    return render(request,'jobs/jobs.html',context)


def show_job(request,id):
    job=Job.objects.get(id=id)
    context={'job':job}
    return render(request,'jobs/job_details.html',context)