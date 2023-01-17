from django.shortcuts import render

def custom_error_403(request, exception):
    return render(request, 'errors/403.html')