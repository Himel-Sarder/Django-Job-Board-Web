from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import JobPosting

# Create your views here.
def index(request):
    #job_postings = JobPosting.objects.all()
    active_job_postings = JobPosting.objects.filter(is_active=True)
    context = {'job_postings': active_job_postings}
    #print(job_postings)
    #return HttpResponse('<h1>Job Board</h1>')
    return render(request, 'job_board/index.html', context)

def job_details(request, pk):
    job_posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {'posting': job_posting}
    return render(request, 'job_board/detail.html', context)