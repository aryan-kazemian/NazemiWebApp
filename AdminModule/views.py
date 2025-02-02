from django.shortcuts import render

# Create your views here.


def admin_panel(request):
    context = {}
    return render(request, 'admin/dashboard.html', context)
