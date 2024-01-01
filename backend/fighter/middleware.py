# middleware.py
from django.shortcuts import redirect
from .models import Fighter

class FighterDetailMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'fighters/' in request.path:
            fighter_id = request.path.split('/')[-1]
            try:
                fighter = Fighter.objects.get(pk=fighter_id)
                return redirect(fighter.page.get_absolute_url())
            except Fighter.DoesNotExist:
                pass
        return self.get_response(request)