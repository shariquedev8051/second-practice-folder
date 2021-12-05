from django.shortcuts import render

# Create your views here.
from .models import Job, Subscriber, Subscription


def get_jobs(request):
    jobs = Job.objects.filter(status=True)
    return render(request, 'jobs.html', {'jobs':jobs})


def get_single_job(request, id):
    job_obj = Job.objects.get(pk=id)
    return render(request, 'job.html',{'job':job_obj})


from .signals import new_subscriber

def subscribe(request, id):
    job = Job.objects.get(pk=id)
    subscriber = Subscriber(email=request.POST['email'])
    subscriber.save()

    subscription = Subscription(user=subscriber, job=job)
    subscription.save()

    # Add this line that sends our custom signal
    new_subscriber.send(sender=subscription, job=job, subscriber=subscriber)

    payload = {
      'job': job,
      'email': request.POST['email']
    }
    return render(request, 'subscribed.html', {'payload': payload})