from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275065',
        'name': 'Rebecca Zaneta Octoria Hutajulu',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
