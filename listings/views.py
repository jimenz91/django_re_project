from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import price_choices, state_choices, bedroom_choices


def index(request):
    """Main Listings page
    We get all the listings from the DB, ordered by list date and checking if they have been published.
    """
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # Logic behind the pagination on the listings page. The number lets you know how many listings per page to show.
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """Single listing page"""
    # Getting the single listing from the DB
    listing = get_object_or_404(Listing, pk=listing_id)
    # Adding the listing to the context view
    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    """Search page within listings app."""
    # Getting all the listings from the DB, ordered by list date.
    queryset_list = Listing.objects.order_by('-list_date')
    # Each field of the form is executed only if the user has put information in said field. Otherwise, the query is executed with the other ones used
    # Keywords form field. The filter with "icontains" means that the keyword exists as a part of a whole.
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City form field. The filter with "iexact" matches an option exactly with what is stored.
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # City form field. The filter with "iexact" matches an option exactly with what is stored.
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Bedrooms form field. The filter with "iexact" matches an option exactly with what is stored.
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Price form field. The filter with "iexact" matches an option exactly with what is stored.
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
