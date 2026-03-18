from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from jobs.models import Job
from .models import Application
from .utils import extract_text_from_pdf, calculate_ats_score

@login_required
def apply_for_job(request, job_id):
    if not request.user.is_student:
        return redirect('home')

    job = get_object_or_404(Job, pk=job_id)
    
    # Check if already applied
    if Application.objects.filter(student=request.user, job=job).exists():
        return render(request, 'ats_scorer/already_applied.html', {'job': job})

    if request.method == 'POST' and request.FILES.get('resume'):
        resume_file = request.FILES['resume']
        
        # Read text from PDF
        resume_text = extract_text_from_pdf(resume_file)
        
        # Calculate Logic
        score = calculate_ats_score(resume_text, job.skills_required)
        
        # Save application
        Application.objects.create(
            student=request.user,
            job=job,
            resume=resume_file,
            ats_score=score
        )
        
        # Email Logic based on Score
        candidate_name = request.user.first_name if request.user.first_name else request.user.username
        candidate_email = request.user.email if request.user.email else f"{request.user.username}@hirehubats.local"
        
        if score >= 70:
            subject = f"Application Update: {job.title} - You're Shortlisted! 🎉"
            message = f"Hi {candidate_name},\n\nCongratulations! Your ATS match score for {job.title} was an outstanding {score}%. You have been shortlisted for the next round of interviews.\n\nOur hiring team will be in touch with you shortly to schedule your interview.\n\nBest regards,\nHireHub ATS Team"
        elif score >= 40:
            subject = f"Application Update: {job.title} - Under Review 🔍"
            message = f"Hi {candidate_name},\n\nThank you for applying to the {job.title} position. Your resume successfully passed our initial screen with an ATS match score of {score}%. Your application is currently under manual review by our hiring team.\n\nWe will update you once a decision has been made.\n\nBest regards,\nHireHub ATS Team"
        else:
            subject = f"Application Update: {job.title} - Status Update 😔"
            message = f"Hi {candidate_name},\n\nThank you for taking the time to apply to the {job.title} position. Unfortunately, your ATS match score of {score}% did not meet our minimum threshold required for this role.\n\nWe encourage you to update your resume to better match job descriptions or apply to other open positions that better fit your current skillset.\n\nBest regards,\nHireHub ATS Team"
            
        # Dispatch email
        send_mail(subject, message, 'noreply@hirehubats.com', [candidate_email], fail_silently=True)

        # AJAX Support
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.headers.get('Accept', '').find('application/json') >= 0
        if is_ajax:
            return JsonResponse({
                'status': 'success', 
                'message': 'Application submitted successfully!', 
                'score': score
            })

        return redirect('student_dashboard')

    return render(request, 'ats_scorer/apply.html', {'job': job})

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        return redirect('home')
    applications = Application.objects.filter(student=request.user).order_by('-applied_at')
    return render(request, 'ats_scorer/student_dashboard.html', {'applications': applications})

@login_required
def admin_dashboard(request):
    if not request.user.is_admin_user and not request.user.is_superuser:
        return redirect('home')
    jobs = Job.objects.all()
    applications = Application.objects.select_related('student', 'job').order_by('-applied_at')
    return render(request, 'ats_scorer/admin_dashboard.html', {'jobs': jobs, 'applications': applications})
