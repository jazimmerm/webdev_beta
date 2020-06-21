from django.shortcuts import redirect, render

def userRedirect(request):
    groups = request.user.groups.all()
    if any(role.name == 'doctor' for role in groups):
        return redirect('drview:homepage')
    elif any(role.name == 'patient' for role in groups):
        return redirect('patientview:homepage')
    else:
        return render(request, 'drview/not_authorized.html')