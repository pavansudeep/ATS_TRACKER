from django.core.management.base import BaseCommand
from jobs.models import Job

class Command(BaseCommand):
    help = 'Populates the database with dummy job data'

    def handle(self, *args, **kwargs):
        jobs_data = [
            # IT Jobs
            {
                'title': 'Senior Python Developer',
                'category': 'IT',
                'city': 'Pune',
                'description': 'Looking for an experienced Python developer to build scalable backend systems using Django and REST APIs.',
                'skills_required': 'Python, Django, REST API, SQL, Git, Linux'
            },
            {
                'title': 'Frontend React Engineer',
                'category': 'IT',
                'city': 'Bangalore',
                'description': 'We need a creative frontend engineer proficient in React, Redux, and modern CSS frameworks like Bootstrap or Tailwind.',
                'skills_required': 'React, Redux, JavaScript, HTML, CSS, Bootstrap'
            },
            {
                'title': 'Data Scientist',
                'category': 'IT',
                'city': 'Delhi',
                'description': 'Join our analytics team to build predictive models and analyze large datasets using Pandas and Scikit-Learn.',
                'skills_required': 'Python, Machine Learning, Data Science, Pandas, SQL'
            },
            {
                'title': 'DevOps Engineer',
                'category': 'IT',
                'city': 'Mumbai',
                'description': 'Seeking a DevOps engineer to manage our cloud infrastructure on AWS, automate deployments using Jenkins and Docker.',
                'skills_required': 'AWS, Docker, Jenkins, Kubernetes, Linux, CI/CD, Python'
            },
            # Non-IT Jobs
            {
                'title': 'Marketing Manager',
                'category': 'NON-IT',
                'city': 'Mumbai',
                'description': 'Experienced marketing professional needed to lead our digital campaigns, SEO strategies, and brand positioning.',
                'skills_required': 'Marketing, SEO, Content Creation, Leadership, Communication'
            },
            {
                'title': 'Human Resources Specialist',
                'category': 'NON-IT',
                'city': 'Pune',
                'description': 'HR Specialist responsible for recruitment, employee relations, and managing company policies.',
                'skills_required': 'HR Management, Recruitment, Communication, Microsoft Office'
            },
            {
                'title': 'Financial Analyst',
                'category': 'NON-IT',
                'city': 'Bangalore',
                'description': 'Analyze financial data, prepare reports, and assist in budget planning for our corporate division.',
                'skills_required': 'Finance, Excel, Accounting, Data Analysis, Reporting'
            },
            {
                'title': 'Operations Executive',
                'category': 'NON-IT',
                'city': 'Delhi',
                'description': 'Oversee daily business operations, manage vendor relations, and ensure process efficiency.',
                'skills_required': 'Operations Management, Logistics, Vendor Management, Communication'
            }
        ]

        Job.objects.all().delete() # clear existing jobs for idempotency
        
        for job_data in jobs_data:
            Job.objects.create(**job_data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(jobs_data)} jobs.'))
