from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from backend.fighter.models import  Fighter,  FighterPluginModel 
#from .views import create_fighter_page
from django.shortcuts import render
from django.urls import include, path
from django import forms
from django.db.models import Q
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool



class FighterPluginForm(forms.ModelForm):
    class Meta:
        model = FighterPluginModel
        fields = ['country', 'weight_class', 'sport', 'champion', 'gender']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['country', 'weight_class', 'sport', 'champion', 'gender']:
            choices = list(Fighter.objects.values_list(field, field).distinct())
            choices.insert(0, (None, 'None'))  # Add "None" option at the beginning
            self.fields[field].choices = choices


#############      
            
@plugin_pool.register_plugin
class FighterListPlugin(CMSPluginBase):
    model = FighterPluginModel
    name = _("Fighter List Plugin")
    render_template = "fighter/fighter_list_plugin.html"
    form = FighterPluginForm

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        filters = {
            'country': instance.country,
            'weight_class': instance.weight_class,
            'sport': instance.sport,
            'champion': instance.champion,
            'gender': instance.gender,
        }
        # Remove None values from filters
        filters = {k: v for k, v in filters.items() if v is not None}
        context['filters'] = filters
        return context
    

"""" 

class FighterListPlugin(CMSPluginBase):
    model = FighterPluginModel
    form = FighterPluginForm
    name = _("FighterListPlugin")
    render_template = "fighter/fighter_list_plugin.html"
    #child_classes = ['FighterDetailPlugin']
    allow_children = True
    def render(self, context, instance, placeholder):
        fighters = Fighter.objects.all()
        if instance.country:
            fighters = fighters.filter(country=instance.country)
        if instance.sport:
            fighters = fighters.filter(sport=instance.sport)
        if instance.gender:
            fighters = fighters.filter(gender=instance.gender)
        if instance.champion:
            fighters = fighters.filter(champion=instance.champion)
        if instance.weight_class:
            fighters = fighters.filter(weight_class=instance.weight_class)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'fighters': fighters,
        })
        return context

class FighterDetailPlugin(CMSPluginBase):
    model = FighterPluginModel
    name = _("Fighter Detail Plugin")
    render_template = "fighter/fighter_detail_plugin.html"
    #parent_classes = ['FighterListPlugin']

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(FighterDetailPlugin)

class FighterPlugin(CMSPluginBase):
    model = FighterPluginModel
    name = _("Fighter Plugin")
    render_template = "fighter_detail.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['fighter'] = instance.fighter
        return context

plugin_pool.register_plugin(FighterPlugin)













class SelectedFighterPlugin(CMSPluginBase):
    model = FighterPluginModel
    name = _("Selected Fighter")
    render_template = "fighter/selected_fighter.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context



plugin_pool.register_plugin(SelectedFighterPlugin)



class FighterPagePlugin(CMSPluginBase):
    model = FighterPluginModel
    name = _("FighterPlugin")
    render_template = "fighter/fighter_page_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(FighterPagePlugin)














class FighterPlugin(CMSPluginBase):
    model = FighterPluginModel
    name = _("FighterPlugin")
    render_template = "fighter/fighter_plugin.html"
    parent_classes = ['FighterListPlugin']
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'fight_card': instance.fighter,
        })
plugin_pool.register_plugin(FighterPlugin)



class FighterPagePlugin(CMSPluginBase):
    model = FighterPluginModel
    name = _("FighterPlugin")
    render_template = "fighter/fighter_page_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(FighterPagePlugin)


class FighterPluginDetail(CMSPluginBase):
    model = FighterPluginModel
    form = FighterPluginForm
    name = _("FighterPluginDetails")
    render_template = "fighter/fighter_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
plugin_pool.register_plugin(FighterPluginDetail)

##########










class FighterPluginDetail(CMSPluginBase):
    model = FighterPluginModel
    form = FighterPluginForm
    name = _("FighterPlugin")
    render_template = "fighter/fighter_plugin.html"

    def render(self, context, instance, placeholder):
        fighters = Fighter.objects.all()
        if instance.country:
            fighters = fighters.filter(country=instance.country)
        if instance.sport:
            fighters = fighters.filter(sport=instance.sport)
        if instance.gender:
            fighters = fighters.filter(gender=instance.gender)
        if instance.champion:
            fighters = fighters.filter(champion=instance.champion)
        if instance.weight_class:
            fighters = fighters.filter(weight_class=instance.weight_class)
        fighter_urls = [create_fighter_page(fighter).get_absolute_url() for fighter in fighters]

        context.update({
            'instance': instance,
            'fighter_urls': fighter_urls,
        })

        return context

plugin_pool.register_plugin(FighterPluginDetail)








    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].widget = forms.Select(choices=Fighter.objects.values_list('country', 'country').distinct())
        self.fields['weight_class'].widget = forms.Select(choices=Fighter.objects.values_list('weight_class', 'weight_class').distinct())
        self.fields['sport'].widget = forms.Select(choices=Fighter.objects.values_list('sport', 'sport').distinct())
        self.fields['champion'].widget = forms.Select(choices=Fighter.objects.values_list('champion', 'champion').distinct())
        self.fields['gender'].widget = forms.Select(choices=Fighter.objects.values_list('gender', 'gender').distinct())





class FighterCategoryWeightClassPlugin(CMSPluginBase):
    model = FighterCategoryWeightClassModel
    form = FighterPluginForm
    name = _("Fighter WeightClass Category Plugin")
    render_template = "fighter/fighter_plugin.html"

    def render(self, context, instance, placeholder):
        fighters = Fighter.objects.all()
        if instance.weight_class:
            fighters = fighters.filter(weight_class=instance.weight_class)
        if instance.gender:
            fighters = fighters.filter(gender=instance.gender)
        context.update({'instance': instance, 'fighters': fighters})
        return context
        


############

class FighterSportPlugin(CMSPluginBase):
    model = FighterCategorySportModel
    form = FighterPluginForm
    name = _("Fighter Sport Plugin")
    render_template = "fighter/fighter_plugin.html"

    def render(self, context, instance, placeholder):
        fighters = Fighter.objects.all()
        if instance.sport:
            fighters = fighters.filter(sport_style=instance.sport_style)
        if instance.champion:
            fighters = fighters.filter(champion=instance.champion)
        context.update({'instance': instance, 'fighters': fighters})
        return context


##############

class FighterChampionPlugin(CMSPluginBase):
    model = FighterPluginModel
    form = FighterPluginForm
    name = _("Fighter Champion Plugin")
    render_template = "fighter/fighter_plugin.html"

    def render(self, context, instance, placeholder):
        fighters = Fighter.objects.all()
        if instance.champion:
            fighters = fighters.filter(champion=instance.champion)
        if instance.weight_class:
            fighters = fighters.filter(weight_class=instance.weight_class)
        if instance.gender:
            fighters = fighters.filter(gender=instance.gender)
        context.update({'instance': instance, 'fighters': fighters})
        return context


#############

class FighterGenderPlugin(CMSPluginBase):
    model = FighterGenderModel
    form = FighterPluginForm
    name = _("Fighter Gender Plugin")
    render_template = "fighter/fighter_plugin.html"

    def render(self, context, instance, placeholder):
        fighters = Fighter.objects.all()
        if instance.gender:
            fighters = fighters.filter(gender=instance.gender)
        context.update({'instance': instance, 'fighters': fighters})
        return context

        




###############

class FightCardPluginForm(forms.ModelForm):
    fight_card = forms.ModelChoiceField(
        queryset=FightCard.objects.all(),
        required=False,
        empty_label="None"
    )

    class Meta:
        model = FightCardPluginModel
        fields = ['fight_card']

class FightCardPlugin(CMSPluginBase):
    model = FightCardPluginModel
    form = FightCardPluginForm
    name = _('Fight Card Plugin')
    render_template = 'fighter/fight_card_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'fight_card': instance.fight_card,
        })
        return context

plugin_pool.register_plugin(FightCardPlugin)
    




class EventPlugin(CMSPluginBase):
    model = EventPluginModel  # Replace with your Event plugin model
    name = _("Event Plugin")
    render_template = "fighter/event_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
    
plugin_pool.register_plugin(EventPlugin)



    


class EventPluginForm(forms.ModelForm):
    class Meta:
        model = EventPluginModel  # Replace with your Event plugin model
        fields = ['location', 'sport', 'weight_class', 'country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget = forms.Select(choices=Event.objects.values_list('location', 'location').distinct())
        self.fields['sport'].widget = forms.Select(choices=Event.objects.values_list('sport', 'sport').distinct())
        self.fields['weight_class'].widget = forms.Select(choices=Event.objects.values_list('weight_class', 'weight_class').distinct())
        self.fields['country'].widget = forms.Select(choices=Event.objects.values_list('country', 'country').distinct())


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
class SearchPlugin(CMSPluginBase):
    model = CMSPlugin  # Use the base CMSPlugin model
    name = _("Search Plugin")
    render_template = "fighter/search_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'form': SearchForm(),
        })
        return context


"""