from django.shortcuts import render, redirect, get_object_or_404

from .forms import TravelAdviceForm
from .models import TravelAdvice, Location, Category


from django.db.models import Q
from django.core.paginator import Paginator
from marketing.models import Signup, Reports
from marketing.forms import NewsletterForm, ContactForm
# Create your views here.



from django.contrib import messages


def index(request):
    contact_form = ContactForm()
    if request.method == "POST":
        if contact_form.is_valid():
            contact_form = ContactForm(request.POST)
            contact_form.save()
            messages.success(request, 'Form submitted successfully!')
        else:
            messages.error(request, 'Error submitting form.')


    signup_form = NewsletterForm()
    
    if request.method == "POST":
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'you have successfully subscribed for our newsletter!')
        else:
            messages.error(request, 'Error submitting form.')

    
    
    context = {"contact_form": contact_form, 
               "messages": list(request._messages),
               "signup_form":signup_form
               }
    
    return render(request, 'mytravel/index.html', context)





# @login_required


def travel_advice(request):  

    
    travel_advice_posts = TravelAdvice.objects.all()
    
    category = Category.objects.all()[:3]

    locations = Location.objects.all()
    

    if request.GET.get('search'):
        search_term = request.GET.get('search')
        travel_advice_posts = travel_advice_posts.filter(
            Q(title__icontains=search_term) | 
            Q(description__icontains=search_term)
        )

    if request.GET.get('location'):
        location_name = request.GET.get('location')
        travel_advice_posts = travel_advice_posts.filter(location__name=location_name)

    if request.GET.get('category'):
        category_name = request.GET.get('category')
        travel_advice_posts = travel_advice_posts.filter(categories__name=category_name)

    paginator = Paginator(travel_advice_posts, 5)
    page_number = request.GET.get('page')
    travel_advice_posts = paginator.get_page(page_number)

    context = {
        
        'travel_advice_posts': travel_advice_posts,
        'locations': locations,
        'category': category,
    }

    return render(request, 'mytravel/travel_advice.html', context)

def travel_advice_detail(request, advice_id):
    travel_advice = get_object_or_404(TravelAdvice, pk=advice_id)
    location_advice_detail = travel_advice.advice_location
    print('this is location detail ', location_advice_detail)
    
    context = {
        'travel_advice':travel_advice,
        'location_advice_detail':location_advice_detail
    }


    return render(request, 'mytravel/travel_advice_detail.html', context)


def destinations(request):

    context = {'home_lamba': 'this is the travel advice page. '}

    return render(request, 'mytravel/destinations.html', context)

def tourServices(request):

    context = {'home_lamba': 'this is the travel advice page. '}

    return render(request, 'mytravel/tour_services.html', context)

def jobs(request):

    context = {'home_lamba': 'this is the travel advice page. '}

    return render(request, 'mytravel/jobs.html', context)



def aboutUs(request):

    context = {'home_lamba': 'this is the travel advice page. '}

    return render(request, 'mytravel/about_us.html', context)
