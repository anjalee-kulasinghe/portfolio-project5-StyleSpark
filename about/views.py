from django.shortcuts import render

# Create your views here.
def about_us(request):
    """ A view to return the about us page. """
    
    return render(request, 'about/about_us.html')