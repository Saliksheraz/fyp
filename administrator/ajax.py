from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def adminPanelAjax(request):
    call = request.POST.get('call', None)

    data = {
        'check': 'check'
    }
    return JsonResponse(data)
