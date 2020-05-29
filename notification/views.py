from django.shortcuts import render

# Create your views here.
def notificationindex(request):
    return render(request, 'notification/index.html')