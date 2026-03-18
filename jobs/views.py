from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):
    jobs = Job.objects.all().order_by('-created_at')
    
    # Filter functionality
    category = request.GET.get('category')
    city = request.GET.get('city')
    
    if category:
        jobs = jobs.filter(category=category)
    if city:
        jobs = jobs.filter(city__icontains=city)
        
    cities = Job.objects.values_list('city', flat=True).distinct()
    
    context = {
        'jobs': jobs,
        'cities': cities,
        'selected_category': category,
        'selected_city': city
    }
    return render(request, 'jobs/home.html', context)

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})
