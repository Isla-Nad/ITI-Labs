from django.shortcuts import render


def contact_us(request):
    return render(request, 'contacts/contact_us.html')


def about_us(request):
    return render(request, 'contacts/about_us.html')
