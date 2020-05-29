from django.shortcuts import render

# Create your views here.
def authenticationindex(request):
    return render(request, 'authentication/index.html')