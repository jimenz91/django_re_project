from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, state_choices, bedroom_choices

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    """Listings main page"""
    # Getting all the listings from the DB, ordering them by date and veryfying that they are published
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    # Adding the listings and the form field options to the context of the view
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    """Website about page, showing all the registered realtors and the seller of the month"""
    # Get realtors from database and organizing them by the date they were hired. Also getting the seller of the month
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    # Adding all the realtors and the best sellers to the context of the view.
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
