from django.shortcuts import render

class AppError(Exception):
    pass   

def staff_dashboard(req):
    if not request.user.is_staff:
        raise AppError('Only staff can access this page.')

    return render(req, 'dashboard.html', {})
