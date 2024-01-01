#-*- coding: utf-8 -*-
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Fighter

def fighter_list(request):
    filters = {
        'sport': request.GET.get('sport'),
        'country': request.GET.get('country'),
        'champion': request.GET.get('champion'),
        'weight_class': request.GET.get('weight_class'),
        'gender': request.GET.get('gender'),
    }

    # Remove None values from filters
    filters = {k: v for k, v in filters.items() if v is not None}

    fighters = Fighter.objects.filter(**filters)
    return render(request, 'fighter/list.html', {'fighters': fighters})


#def fighter_list(request):
#    fighters = Fighter.objects.all()
#    return render(request, 'fighter/list.html', {'fighters': fighters})

def fighter_detail(request, id):
    fighter = Fighter.objects.get(id=id)
    return render(request, 'fighter/detail.html', {'fighter': fighter})




"""from django.http import JsonResponse

def get_fighters(request):
    fighters = Fighter.objects.all().values('id', 'name')  
    data = list(fighters)
    return JsonResponse(data, safe=False)



def get_fighter(request, id):
    fighter = Fighter.objects.get(id = id)
    data = {
        'name': fighter.name,
        'weight': fighter.weight,
        #  other fields 
    }
    return JsonResponse(data)



class Index_view(generic.ListView):
    fighters = Fighter.objects.all()
    template_name = 'fighter/index.html'
    def get_queryset(self):
        return Fighter.objects.all()
    

class archive_view(generic.DetailView):
    fighters = Fighter.objects.all()
    template_name = 'fighter/archive.html'
    def get_queryset(self):
        return Fighter.objects.all()

def fighter_list(request):
    fighters = Fighter.objects.all()
    return render(request, 'fighter/fighter_list.html', {'fighters': fighters})


from django.shortcuts import get_object_or_404

def fighter_detail(request, fighter_id):
    fighter = get_object_or_404(Fighter, pk=fighter_id)
    return render(request, 'fighter/fighter_detail.html', {'fighter': fighter})
class DetailView(generic.DetailView):
    model = Fighter
    template_name = 'fighter/detail.html'


class ResultsView(generic.DetailView):
    model = Fighter
    template_name = 'fighter/results.html'


def vote(request, fighter_id):
    p = get_object_or_404(Fighter, pk=fighter_id)
    
    return render(request, 'fighter/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    
    return HttpResponseRedirect(reverse('fighter:results', args=(p.id,)))
"""