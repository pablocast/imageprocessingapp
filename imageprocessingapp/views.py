from django.shortcuts import render

# Create your views here.
def submit(request):
    return render(request, 'submit.html')