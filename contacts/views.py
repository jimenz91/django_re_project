from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages, auth

from .models import Contact


def contact(request):
    """Logic for retrieving information from contact form in single listing page"""
    # Check if the method is a POST and obtaining all the fields from the inquiry.
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Checking if the registered user has already submitted an inquirt for the listing
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id)
            if has_contacted:
                messages.error(
                    request, 'You have already submitted an inquiry for this listing, a realtor will contact you soon.')
            return redirect('/listings/'+listing_id)
        # Creating the contact inquiry in the DB.
        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing +
        #     '. Sign into the admin panel for more',
        #     'email@gmail.com',
        #     [realtor_email,],
        #     fail_silently=False
        # )

        # Informing the user of the correct submission.
        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')

    return redirect('/listings/'+listing_id)
