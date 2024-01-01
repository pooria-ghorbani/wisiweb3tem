
from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django_countries.fields import CountryField
from filer.fields.image import FilerImageField
import random
import uuid
from uuid import UUID
from django.utils import timezone
from djangocms_attributes_field.fields import AttributesField
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from cms.models.fields import PlaceholderField


   
def fighter_placeholder_slotname(instance):
    return 'placeholder_fighter'


def create_random_7_digit_number():
    return random.randint(100, 9999999)  # Generate a random 5-digit number



class FighterManager(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, verbose_name="fighter manager", default='Unknown')

class FighterCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, verbose_name="fighter category", default='Unknown')


class Fighter(models.Model):
    WEIGHT_CHOICES = (
        ('SUPER_HEAVY', 'Super Heavy'),
        ('HEAVY', 'Heavy'),
        ('CRUISER', 'Cruiser'),
        ('LIGHT_HEAVY', 'Light Heavy'),
        ('SUPER_MIDDLE', 'Super Middle'),
        ('MIDDLE', 'Middle'),
        ('SUPER_WELTER', 'Super Welter'),
        ('WELTER', 'Welter'),
        ('SUPER_LIGHT', 'Super Light'),
        ('LIGHT', 'Light'),
        ('SUPER_FEATHER', 'Super Feather'),
        ('FEATHER', 'Feather'),
        ('SUPER_BANTAM', 'Super Bantam'),
        ('BANTAM', 'Bantam'),
        ('SUPER_FLY', 'Super Fly'),
        ('FLY', 'Fly'),
        ('LIGHT_FLY', 'Light Fly'),
        ('MINIMUM', 'Minimum'),
        ('ATOM', 'Atom'),
        ('OTHER', 'Other'),
    )
    CHAMPION_CHOICES = (
        ('UFC', 'UFC'),
        ('MMA', 'MMA'),
        ('KICKBOXING_PRO', 'Kickboxing Pro'),
        ('KICKBOXING_AMATEUR', 'Kickboxing Amateur'),
        ('MUAY_THAI', 'Muay Thai'),
        ('FREE_FIGHTING', 'Free Fighting'),
        ('BOXING_PRO', 'Boxing Pro'),
        ('BOXING_AMATEUR', 'Boxing Amateur'),
        ('KARATE', 'Karate'),
        ('OTHER', 'Other'),
        ('NOT_HAVE', 'Not Have'),
    )
    SPORT_C= (
        ('UFC', 'UFC'),
        ('MMA', 'MMA'),
        ('KICKBOXING_PRO', 'Kickboxing Pro'),
        ('KICKBOXING_AMATEUR', 'Kickboxing Amateur'),
        ('MUAY_THAI', 'Muay Thai'),
        ('FREE_FIGHTING', 'Free Fighting'),
        ('BOXING_PRO', 'Boxing Pro'),
        ('BOXING_AMATEUR', 'Boxing Amateur'),
        ('KARATE', 'Karate'),
        ('OTHER', 'Other'),
    )

    
    TITLE_CHOICES = (
        ('NOT_HAVE', 'Not Have'),
        ('M  |UFC', 'M | UFC'),
        ('F|UFC', 'F | UFC'),
        ('M|U.S.REGIONAL MMA', 'M | U.S. Regional MMA'),
        ('F|U.S.REGIONAL MMA', 'F | U.S. Regional MMA'),
        ('F|UFC', 'F | UFC'),
        ('M|IBF African', 'M | IBF African'),
        ('M|IBF Asia', 'M | IBF Asia'),
        ('M|IBF Asia Oceania', 'M | IBF Asia Oceania'),
        ('M|IBF Australasian', 'M | IBF Australasian'),
        ('M|IBF European', 'M | IBF European'),
        ('M|IBF European E/W', 'M | IBF European E/W'),
        ('M|IBF Inter-Continental', 'M | IBF Inter-Continental'),
        ('f|IBF Inter-Continental', 'f | IBF Inter-Continental'),
        ('M|IBF Interi M World', 'M | IBF Interi M World'),
        ('f|IBF Interi M World', 'f | IBF Interi M World'),
        ('M|IBF International', 'M | IBF International'),
        ('M|IBF Latino', 'M | IBF Latino'),
        ('M|IBF Mediterranean', 'M | IBF Mediterranean'),
        ('M|IBF North A Merican', 'M | IBF North A Merican'),
        ('M|IBF Pan Pacific', 'M | IBF Pan Pacific'),
        ('M|IBF USBA', 'M | IBF USBA'),
        ('M|IBF USBA Atlantic Coast Region', 'M | IBF USBA Atlantic Coast Region'),
        ('M|IBF USBA Southern Region', 'M | IBF USBA Southern Region'),
        ('M|IBF World', 'M | IBF World'),
        ('f|IBF World', 'f | IBF World'),
        ('M|IBF Youth', 'M | IBF Youth'),
        #IBO
        ('M|IBO All-Africa', 'M | IBO All-Africa'),
        ('M|IBO A Mericas', 'M | IBO A Mericas'),
        ('M|IBO Asia Pacific', 'M | IBO Asia Pacific'),
        ('M|IBO Continental', 'M | IBO Continental'),
        ('M|IBO European', 'M | IBO European'),
        ('M|IBO IberoA Merican', 'M | IBO IberoA Merican'),
        ('M|IBO Inter-Continental', 'M | IBO Inter-Continental'),
        ('f|IBO Inter-Continental', 'f | IBO Inter-Continental'),
        ('M|IBO International', 'M | IBO International'),
        ('f|IBO International', 'f | IBO International'),
        ('M|IBO Mediterranean', 'M | IBO Mediterranean'),
        ('M|IBO Oceania-Orient', 'M | IBO Oceania-Orient'),
        ('M|IBO World', 'M | IBO World'),
        ('f|IBO World', 'f | IBO World'),
        ('M|IBO World Youth', 'M | IBO World Youth'),
        ('f|IBO World Youth', 'f | IBO World Youth'),
        #WBO
        ('M|WBA Fedebol', 'M | WBA Fedebol'),
        ('M|WBA Fedecaribe', 'M | WBA Fedecaribe'),
        ('M|WBA Fedecentro', 'M | WBA Fedecentro'),
        ('M|WBA Fedelatin', 'M | WBA Fedelatin'),
        ('f|WBA Fedelatin', 'f | WBA Fedelatin'),
        ('M|WBA Gold World', 'M | WBA Gold World'),
        ('f|WBA Gold World', 'f | WBA Gold World'),
        ('M|WBA Inter-Continental', 'M | WBA Inter-Continental'),
        ('f|WBA Inter-Continental', 'f | WBA Inter-Continental'),
        ('M|WBA Interi M World', 'M | WBA Interi M World'),
        ('f|WBA Interi M World', 'f | WBA Interi M World'),
        ('M|WBA Super World', 'M | WBA Super World'),
        ('f|WBA Super World', 'f | WBA Super World'),
        ('M|WBA World', 'M  |WBA World'),
        ('f|WBA World', 'f | WBA World'),
        #WBC
        ('M|WBC Asian', 'M | WBC Asian'),
        ('M|WBC Asian Continental', 'M | WBC Asian Continental'),
        ('M|WBC Asian Silver', 'M|WBC Asian Silver'),
        ('M|WBC CISBB', 'M | WBC CISBB'),
        ('M|WBC Continental A Mericas', 'M | WBC Continental A Mericas'),
        ('M|WBC Dia Mond', 'M | WBC Dia Mond'),
        ('f|WBC Dia Mond', 'f  |WBC Dia Mond'),
        ('M|WBC FECARBOX', 'M | WBC FECARBOX'),
        ('M|WBC FECONSUR', 'M | WBC FECONSUR'),
        ('f|WBC FECONSUR', 'f | WBC FECONSUR'),
        ('M|WBC Francophone', 'M | WBC Francophone'),
        ('f|WBC Francophone', 'f | WBC Francophone'),
        ('M|WBC Interi M World', 'M | WBC Interi M World'),
        ('f|WBC Interi M World', 'f | WBC Interi M World'),
        ('M|WBC International', 'M | WBC International'),
        ('f|WBC International', 'f | WBC International'),
        ('M|WBC International Silver', 'M | WBC International Silver'),
        ('M|WBC Latino', 'M | WBC Latino'),
        ('f|WBC Latino', 'f | WBC Latino'),
        ('M|WBC Mediterranean', 'M | WBC Mediterranean'),
        ('M|WBC Silver', 'M | WBC Silver'),
        ('f|WBC Silver', 'f | WBC Silver'),
        ('M|WBC USA', 'M | WBC USA'),
        ('M|WBC USA Silver', 'M | WBC USA Silver'),
        ('M|WBC World', 'M | WBC World'),
        ('f|WBC World', 'f | WBC World'),
        ('M|WBC Youth Intercontinental', 'M | WBC Youth Intercontinental'),
        ('M|WBC Youth Silver', 'M | WBC Youth Silver'),
        ('M|WBC Youth World', 'M | WBC Youth World'),
        ('f|WBC Youth World', 'f | WBC Youth World'),
        #WBO
        ('M|WBO Africa', 'M | WBO Africa'),
        ('M|WBO Asia Pacific', 'M | WBO Asia Pacific'),
        ('W|WBO Asia Pacific', 'W | WBO Asia Pacific'),
        ('M|WBO Asia Pacific Youth', 'M | WBO Asia Pacific Youth'),
        ('M|WBO Chinese', 'M | WBO Chinese'),
        ('M|WBO European', 'M | WBO European'),
        ('M|WBO Global', 'M | WBO Global'),
        ('M|WBO Inter-Continental', 'M | WBO Inter-Continental'),
        ('M|WBO Interi M World', 'M | WBO Interi M World'),
        ('f|WBO Interi M World', 'f | WBO Interi M World'),
        ('M|WBO International', 'M | WBO International'),
        ('M|WBO Latino', 'M | WBO Latino'),
        ('M|WBO NABO', 'M | WBO NABO'),
        ('M|WBO NABO Youth', 'M | WBO NABO Youth'),
        ('1 M|WBO Oriental', '1 M | WBO Oriental'),
        ('M|WBO Oriental Youth', 'M | WBO Oriental Youth'),
        ('M|WBO World', 'M | WBO World'),
        ('f|WBO World', 'f | WBO World'),
        ('M|WBO Youth', 'M | WBO Youth'),
        #
        ('M|Asian Boxing Federation', 'M  |Asian Boxing Federation'),
        ('f|Asian Boxing Federation', 'f | Asian Boxing Federation'),
        ('M|Australasian', 'M | Australasian'),
        ('f|Australasian', 'f | Australasian'),
        ('Australian National Boxing Federation NeW South Wales', 'Australian National Boxing Federation NeW South Wales'),
        ('M|Australian National Boxing Federation NeW South Wales', 'M | Australian National Boxing Federation NeW South Wales'),
        ('f|Australian National Boxing Federation NeW South Wales', 'f | Australian National Boxing Federation NeW South Wales'),
        ('Australian National Boxing Federation Queensland', 'Australian National Boxing Federation Queensland'),
        ('M|Australian National Boxing Federation Queensland', 'M | Australian National Boxing Federation Queensland'),
        ('f|Australian National Boxing Federation Queensland', 'f | Australian National Boxing Federation Queensland'),
        ('Belgian Boxing FederationW', 'Belgian Boxing FederationW'),
        ('f|Belgian Boxing Federation', 'f | Belgian Boxing Federation'),
        ('M|Belgian', 'M | Belgian'),
        ('Boxing South Africa', 'Boxing South Africa'),
        ('M|South African', 'M | South African'),
        ('f|South African', 'f | South African'),
        ('Boxing Union of Ireland', 'Boxing Union of Ireland'),
        ('M|Celtic', 'M | Celtic'),
        ('M|Irish', 'M  |Irish'),
        ('British Boxing Board of Control', 'British Boxing Board of Control'),
        ('M|BBBofC British', 'M | BBBofC British'),
        ('f|BBBofC British', 'f | BBBofC British'),
        ('M|BBBofC Celtic', 'M | BBBofC Celtic'),
        ('f|BBBofC Celtic', 'f | BBBofC Celtic'),
        ('M|BBBofC Central Area', 'M | BBBofC Central Area'),
        ('f|BBBofC Central Area', 'f | BBBofC Central Area'),
        ('M|BBBofC English', 'M | BBBofC English'),
        ('f|BBBofC English', 'f | BBBofC English'),
        ('M|BBBofC Midlands Area', 'M | BBBofC Midlands Area'),
        ('f|BBBofC Midlands Area', 'f | BBBofC Midlands Area'),
        ('M|BBBofC Northern Area', 'M | BBBofC Northern Area'),
        ('f|BBBofC Northern Area', 'f | BBBofC Northern Area'),
        ('M|BBBofC Northern Ireland Area', 'M | BBBofC Northern Ireland Area'),
        ('f|BBBofC Northern Ireland Area', 'f | BBBofC Northern Ireland Area'),
        ('M|BBBofC Scottish Area', 'M | BBBofC Scottish Area'),
        ('f|BBBofC Scottish Area', 'f | BBBofC Scottish Area'),
        ('M|BBBofC Southern Area', 'M | BBBofC Southern Area'),
        ('f|BBBofC Southern Area', 'f |BBBofC Southern Area'),
        ('M|BBBofC Welsh Area', 'M | BBBofC Welsh Area'),
        ('f|BBBofC Welsh Area', 'f | BBBofC Welsh Area'),
        ('M|BBBofC Western Area', 'M | BBBofC Western Area'),
        #
        ('M|BDB Ger Man', 'M | BDB Ger Man'),
        ('M|BDB International', 'M | BDB International'),
        ('M|Co M MonWealth Boxing Council', 'M | Co M MonWealth Boxing Council'),
        ('f|Co M MonWealth Boxing Council', 'f | Co M MonWealth Boxing Council'),
        ('M|Eurasian Boxing Parlia Ment', 'M | Eurasian Boxing Parlia Ment'),
        ('f|Eurasian Boxing Parlia Ment', 'f | Eurasian Boxing Parlia Ment'),
        ('M|EBU European', 'M | EBU European'),
        ('f|EBU European', 'f | EBU European'),
        ('M|EBU European Union', 'M | EBU European Union'),
        ('M|EBU External', 'M | EBU External'),
        ('M|EBU Silver', 'M | EBU Silver'),
        ('M|Argentinian', 'M | Argentinian'),
        ('f|Argentinian', 'f | Argentinian'),
        ('M|French', 'M | French'),
        ('f|French', 'f | French'),
        ('M|Federazione Pugilistica Italiana', 'M | Federazione Pugilistica Italiana'),
        ('f|Federazione Pugilistica Italiana', 'f | Federazione Pugilistica Italiana'),
        ('M|International', 'M | International'),
        ('M|National', 'M | National'),
        ('M|Intercontinental', 'M | Intercontinental'),
        ('M|World', 'M | World'),
        ('f|World', 'f | World'),
        ('M|World Youth', 'M | World Youth'),
        #
        ('M|WKF', 'M | WKF'),
        ('f|WKF', 'f | WKF'),
        ('M|WAKO', 'M | WAKO'),
        ('W|WAKO', 'W | WAKO'),
        ('M|ONE Champion', 'M | ONE Champion'),
        ('W|ONE Champion', 'W | ONE Champion'),
        ('M|WKA', 'M | WKA'),
        ('W|WKA', 'W | WKA'),
        ('M|GLORY', 'M | GLORY'),
        ('W|GLORY', 'W | GLORY'),
        ('M|RING20 KB', 'M | RING20 KB'),
        ('W|RING20 KB', 'W | RING20 KB'),
        ('M|WKB', 'M | WKB'),
        ('W|WKB', 'W | WKB'),
        ('M|WMC', 'M | WMC'),
        ('W|WMC', 'W | WMC'),
        ('M|WMF', 'M | WMF'),
        ('W|WMF', 'W | WMF'),
        ('M|WBC', 'M | WBC'),
        ('W|WBC', 'W  |WBC'),
        ('M|IFMA', 'M | IFMA'),
        ('W|IFMA', 'W | IFMA'),
        ('M|RING20 MT', 'M | RING20 MT'),
        ('W|RING20 MT', 'W | RING20 MT'),
        ('M|WMT', 'M | WMT'),
        ('W|WMT', 'W | WMT'),
        ('M|IKS', 'M  |IKS'),
        ('W|IKS', 'W | IKS'),
        ('M|WKF', 'M | WKF'),
        ('W|WKF', 'W | WKF'),
        ('M|IKF', 'M | IKF'),
        ('W|IKF', 'W | IKF'),
        ('M|ISKA', 'M | ISKA'),
        ('W|ISKA', 'W | ISKA'),
        ('M|RING20 K', 'M | RING20 K'),
        ('W|RING20 K', 'W | RING20 K'),
        ('OTHER', 'other'),
       
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    
    
    attributes = AttributesField()
    #fighter_placeholder = PlaceholderField('placeholder_fighter')
    id = models.AutoField(primary_key=True)
    fighter_uuids = models.UUIDField(default=uuid.uuid4, unique=True),
    fighters_id = models.PositiveIntegerField(unique=True,)
    is_active = models.BooleanField(default=True)
    is_crown = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    fighter_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    career_years = models.CharField(max_length=9, null=True, blank=True, default='2023-2023')
    name = models.CharField(max_length=100, unique=True, verbose_name="fighter name", default='Unknown')
    image = FilerImageField(on_delete=models.PROTECT, verbose_name="fighter image")
    score = models.IntegerField(verbose_name="fighter score", default=0,)
    weight_class = models.CharField(max_length=20, choices=WEIGHT_CHOICES, verbose_name="weight class", default='LIGHT')
    height = models.CharField(max_length=20,blank=True, verbose_name="height")
    weight = models.IntegerField(verbose_name="fighter weight", default=0, blank=True, null=True)
    sport = models.CharField(max_length=100, choices=SPORT_C, verbose_name="sport", default='UFC')
    champion = models.CharField(max_length=20, choices=CHAMPION_CHOICES, verbose_name="Champion", default='UFC')
    champion_des = models.CharField(max_length=20,verbose_name="champion description", default='Unknown')
    country = CountryField(blank_label='(select country)', null=True, default='US')
    nationality = CountryField(blank_label='(select country)', null=True, default='US')
    residence = CountryField(blank_label='(select country)', null=True, default='US')
    titles = models.CharField(max_length=100, choices=TITLE_CHOICES, verbose_name="fighter titles", default='Not Have')
    bouts = models.IntegerField(blank=True, verbose_name="fighter bouts", default=0)
    rounds = models.IntegerField(blank=True, verbose_name="fighter rounds", default=0)
    wins = models.IntegerField(blank=True, verbose_name="fighter win", default=0)
    losses = models.IntegerField(blank=True, verbose_name="fighter losses", default=0)
    draws = models.IntegerField(blank=True, verbose_name="fighter draws", default=0)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, verbose_name="fighter gender", default='M')
    age = models.IntegerField(blank=True, verbose_name="fighter age", default=0)
    star_rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        validators=[MinValueValidator(Decimal('0.0')), MaxValueValidator(Decimal('5.0'))],
        default=Decimal('0.0')
    )
    category = models.ForeignKey(FighterCategory, on_delete=models.CASCADE, null=True)
    fighter_manager = models.ForeignKey(FighterManager, on_delete=models.CASCADE, null=True)
    #fighter_placeholder = models.ForeignKey(fighter_placeholder_slotname, on_delete=models.CASCADE, default='fighter')
    
    @property
    def ranking_score(self):
        # This is a more complex example that considers multiple factors.
        # The weights for each factor (0.5, 0.3, 0.2 in this example) should add up to 1.
        # You can adjust these weights based on how important you think each factor is.
        return self.wins * 0.5 - self.losses * 0.3 + self.draws * 0.2
    
    def __str__ (self):
        return f'{self.id} - {self.fighter_uuids} - {self.name} - {self.ranking_score} - {self.star_rating}'
    


class FighterPluginModel(CMSPlugin):
    fighter_instance = models.ForeignKey(Fighter, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    weight_class = models.CharField(max_length=255, blank=True)
    sport = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=10)
    champion = models.CharField(max_length=255, blank=True)

class FighterDetailPluginModel(CMSPlugin):
    fighter_instance = models.ForeignKey(Fighter, on_delete=models.CASCADE, null=True)

############################
"""
class FightCard(models.Model):
    SPORT_C = (
        ('UFC', 'UFC'),
        ('MMA', 'MMA'),
        ('KICKBOXING_PRO', 'Kickboxing Pro'),
        ('KICKBOXING_AMATEUR', 'Kickboxing Amateur'),
        ('MUAY_THAI', 'Muay Thai'),
        ('FREE_FIGHTING', 'Free Fighting'),
        ('BOXING_PRO', 'Boxing Pro'),
        ('BOXING_AMATEUR', 'Boxing Amateur'),
        ('KARATE', 'Karate'),
        ('OTHER', 'Other'),    
    )
    WEIGHT_CHOICES = (
        ('SUPER_HEAVY', 'Super Heavy'),
        ('HEAVY', 'Heavy'),
        ('CRUISER', 'Cruiser'),
        ('LIGHT_HEAVY', 'Light Heavy'),
        ('SUPER_MIDDLE', 'Super Middle'),
        ('MIDDLE', 'Middle'),
        ('SUPER_WELTER', 'Super Welter'),
        ('WELTER', 'Welter'),
        ('SUPER_LIGHT', 'Super Light'),
        ('LIGHT', 'Light'),
        ('SUPER_FEATHER', 'Super Feather'),
        ('FEATHER', 'Feather'),
        ('SUPER_BANTAM', 'Super Bantam'),
        ('BANTAM', 'Bantam'),
        ('SUPER_FLY', 'Super Fly'),
        ('FLY', 'Fly'),
        ('LIGHT_FLY', 'Light Fly'),
        ('MINIMUM', 'Minimum'),
        ('ATOM', 'Atom'),
        ('OTHER', 'Other'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    attributes = AttributesField()
    fighter1 = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name='fighter1')
    fighter2 = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name='fighter2')
    fight_name = models.CharField(max_length=100,)
    sport = models.CharField(max_length=100, choices=SPORT_C, verbose_name="sport", default='UFC')
    weight_class = models.CharField(max_length=20, choices=WEIGHT_CHOICES, verbose_name="weight class", default='LIGHT')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, verbose_name="weight class", default='LIGHT')
    date_time = models.DateTimeField()
    location = CountryField(blank_label='(select country)', null=True, default='US')
    result = models.CharField(max_length=10, choices=[('W', 'Winner Fighter 1'), ('L', 'Winner Fighter 2'), ('D', 'Draw'),('N/A', 'Not Specified'),('C', 'Cancled')])
    def __str__(self):
        return f'{self.fighter1} - {self.fighter2} -  {self.date_time}'


class FightCardPluginModel(CMSPlugin):
    fight_card = models.ForeignKey(FightCard, on_delete=models.CASCADE, null=True)
    
    


#####################
class Event(models.Model):
    WEIGHT_CHOICES = (
            ('SUPER_HEAVY', 'Super Heavy'),
            ('HEAVY', 'Heavy'),
            ('CRUISER', 'Cruiser'),
            ('LIGHT_HEAVY', 'Light Heavy'),
            ('SUPER_MIDDLE', 'Super Middle'),
            ('MIDDLE', 'Middle'),
            ('SUPER_WELTER', 'Super Welter'),
            ('WELTER', 'Welter'),
            ('SUPER_LIGHT', 'Super Light'),
            ('LIGHT', 'Light'),
            ('SUPER_FEATHER', 'Super Feather'),
            ('FEATHER', 'Feather'),
            ('SUPER_BANTAM', 'Super Bantam'),
            ('BANTAM', 'Bantam'),
            ('SUPER_FLY', 'Super Fly'),
            ('FLY', 'Fly'),
            ('LIGHT_FLY', 'Light Fly'),
            ('MINIMUM', 'Minimum'),
            ('ATOM', 'Atom'),
            ('OTHER', 'Other'),
        )
        
    CHAMPION_CHOICES = (
            ('UFC', 'UFC'),
            ('MMA', 'MMA'),
            ('KICKBOXING_PRO', 'Kickboxing Pro'),
            ('KICKBOXING_AMATEUR', 'Kickboxing Amateur'),
            ('MUAY_THAI', 'Muay Thai'),
            ('FREE_FIGHTING', 'Free Fighting'),
            ('BOXING_PRO', 'Boxing Pro'),
            ('BOXING_AMATEUR', 'Boxing Amateur'),
            ('OTHER', 'Other'),
        )
    TITLE_CHOICES = (
        ('NOT_HAVE', 'Not Have'),
        ('M  |UFC', 'M | UFC'),
        ('F|UFC', 'F | UFC'),
        ('M|U.S.REGIONAL MMA', 'M | U.S. Regional MMA'),
        ('F|U.S.REGIONAL MMA', 'F | U.S. Regional MMA'),
        ('F|UFC', 'F | UFC'),
        ('M|IBF African', 'M | IBF African'),
        ('M|IBF Asia', 'M | IBF Asia'),
        ('M|IBF Asia Oceania', 'M | IBF Asia Oceania'),
        ('M|IBF Australasian', 'M | IBF Australasian'),
        ('M|IBF European', 'M | IBF European'),
        ('M|IBF European E/W', 'M | IBF European E/W'),
        ('M|IBF Inter-Continental', 'M | IBF Inter-Continental'),
        ('f|IBF Inter-Continental', 'f | IBF Inter-Continental'),
        ('M|IBF Interi M World', 'M | IBF Interi M World'),
        ('f|IBF Interi M World', 'f | IBF Interi M World'),
        ('M|IBF International', 'M | IBF International'),
        ('M|IBF Latino', 'M | IBF Latino'),
        ('M|IBF Mediterranean', 'M | IBF Mediterranean'),
        ('M|IBF North A Merican', 'M | IBF North A Merican'),
        ('M|IBF Pan Pacific', 'M | IBF Pan Pacific'),
        ('M|IBF USBA', 'M | IBF USBA'),
        ('M|IBF USBA Atlantic Coast Region', 'M | IBF USBA Atlantic Coast Region'),
        ('M|IBF USBA Southern Region', 'M | IBF USBA Southern Region'),
        ('M|IBF World', 'M | IBF World'),
        ('f|IBF World', 'f | IBF World'),
        ('M|IBF Youth', 'M | IBF Youth'),
        #IBO
        ('M|IBO All-Africa', 'M | IBO All-Africa'),
        ('M|IBO A Mericas', 'M | IBO A Mericas'),
        ('M|IBO Asia Pacific', 'M | IBO Asia Pacific'),
        ('M|IBO Continental', 'M | IBO Continental'),
        ('M|IBO European', 'M | IBO European'),
        ('M|IBO IberoA Merican', 'M | IBO IberoA Merican'),
        ('M|IBO Inter-Continental', 'M | IBO Inter-Continental'),
        ('f|IBO Inter-Continental', 'f | IBO Inter-Continental'),
        ('M|IBO International', 'M | IBO International'),
        ('f|IBO International', 'f | IBO International'),
        ('M|IBO Mediterranean', 'M | IBO Mediterranean'),
        ('M|IBO Oceania-Orient', 'M | IBO Oceania-Orient'),
        ('M|IBO World', 'M | IBO World'),
        ('f|IBO World', 'f | IBO World'),
        ('M|IBO World Youth', 'M | IBO World Youth'),
        ('f|IBO World Youth', 'f | IBO World Youth'),
        #WBO
        ('M|WBA Fedebol', 'M | WBA Fedebol'),
        ('M|WBA Fedecaribe', 'M | WBA Fedecaribe'),
        ('M|WBA Fedecentro', 'M | WBA Fedecentro'),
        ('M|WBA Fedelatin', 'M | WBA Fedelatin'),
        ('f|WBA Fedelatin', 'f | WBA Fedelatin'),
        ('M|WBA Gold World', 'M | WBA Gold World'),
        ('f|WBA Gold World', 'f | WBA Gold World'),
        ('M|WBA Inter-Continental', 'M | WBA Inter-Continental'),
        ('f|WBA Inter-Continental', 'f | WBA Inter-Continental'),
        ('M|WBA Interi M World', 'M | WBA Interi M World'),
        ('f|WBA Interi M World', 'f | WBA Interi M World'),
        ('M|WBA Super World', 'M | WBA Super World'),
        ('f|WBA Super World', 'f | WBA Super World'),
        ('M|WBA World', 'M  |WBA World'),
        ('f|WBA World', 'f | WBA World'),
        #WBC
        ('M|WBC Asian', 'M | WBC Asian'),
        ('M|WBC Asian Continental', 'M | WBC Asian Continental'),
        ('M|WBC Asian Silver', 'M|WBC Asian Silver'),
        ('M|WBC CISBB', 'M | WBC CISBB'),
        ('M|WBC Continental A Mericas', 'M | WBC Continental A Mericas'),
        ('M|WBC Dia Mond', 'M | WBC Dia Mond'),
        ('f|WBC Dia Mond', 'f  |WBC Dia Mond'),
        ('M|WBC FECARBOX', 'M | WBC FECARBOX'),
        ('M|WBC FECONSUR', 'M | WBC FECONSUR'),
        ('f|WBC FECONSUR', 'f | WBC FECONSUR'),
        ('M|WBC Francophone', 'M | WBC Francophone'),
        ('f|WBC Francophone', 'f | WBC Francophone'),
        ('M|WBC Interi M World', 'M | WBC Interi M World'),
        ('f|WBC Interi M World', 'f | WBC Interi M World'),
        ('M|WBC International', 'M | WBC International'),
        ('f|WBC International', 'f | WBC International'),
        ('M|WBC International Silver', 'M | WBC International Silver'),
        ('M|WBC Latino', 'M | WBC Latino'),
        ('f|WBC Latino', 'f | WBC Latino'),
        ('M|WBC Mediterranean', 'M | WBC Mediterranean'),
        ('M|WBC Silver', 'M | WBC Silver'),
        ('f|WBC Silver', 'f | WBC Silver'),
        ('M|WBC USA', 'M | WBC USA'),
        ('M|WBC USA Silver', 'M | WBC USA Silver'),
        ('M|WBC World', 'M | WBC World'),
        ('f|WBC World', 'f | WBC World'),
        ('M|WBC Youth Intercontinental', 'M | WBC Youth Intercontinental'),
        ('M|WBC Youth Silver', 'M | WBC Youth Silver'),
        ('M|WBC Youth World', 'M | WBC Youth World'),
        ('f|WBC Youth World', 'f | WBC Youth World'),
        #WBO
        ('M|WBO Africa', 'M | WBO Africa'),
        ('M|WBO Asia Pacific', 'M | WBO Asia Pacific'),
        ('W|WBO Asia Pacific', 'W | WBO Asia Pacific'),
        ('M|WBO Asia Pacific Youth', 'M | WBO Asia Pacific Youth'),
        ('M|WBO Chinese', 'M | WBO Chinese'),
        ('M|WBO European', 'M | WBO European'),
        ('M|WBO Global', 'M | WBO Global'),
        ('M|WBO Inter-Continental', 'M | WBO Inter-Continental'),
        ('M|WBO Interi M World', 'M | WBO Interi M World'),
        ('f|WBO Interi M World', 'f | WBO Interi M World'),
        ('M|WBO International', 'M | WBO International'),
        ('M|WBO Latino', 'M | WBO Latino'),
        ('M|WBO NABO', 'M | WBO NABO'),
        ('M|WBO NABO Youth', 'M | WBO NABO Youth'),
        ('1 M|WBO Oriental', '1 M | WBO Oriental'),
        ('M|WBO Oriental Youth', 'M | WBO Oriental Youth'),
        ('M|WBO World', 'M | WBO World'),
        ('f|WBO World', 'f | WBO World'),
        ('M|WBO Youth', 'M | WBO Youth'),
        #
        ('M|Asian Boxing Federation', 'M  |Asian Boxing Federation'),
        ('f|Asian Boxing Federation', 'f | Asian Boxing Federation'),
        ('M|Australasian', 'M | Australasian'),
        ('f|Australasian', 'f | Australasian'),
        ('Australian National Boxing Federation NeW South Wales', 'Australian National Boxing Federation NeW South Wales'),
        ('M|Australian National Boxing Federation NeW South Wales', 'M | Australian National Boxing Federation NeW South Wales'),
        ('f|Australian National Boxing Federation NeW South Wales', 'f | Australian National Boxing Federation NeW South Wales'),
        ('Australian National Boxing Federation Queensland', 'Australian National Boxing Federation Queensland'),
        ('M|Australian National Boxing Federation Queensland', 'M | Australian National Boxing Federation Queensland'),
        ('f|Australian National Boxing Federation Queensland', 'f | Australian National Boxing Federation Queensland'),
        ('Belgian Boxing FederationW', 'Belgian Boxing FederationW'),
        ('f|Belgian Boxing Federation', 'f | Belgian Boxing Federation'),
        ('M|Belgian', 'M | Belgian'),
        ('Boxing South Africa', 'Boxing South Africa'),
        ('M|South African', 'M | South African'),
        ('f|South African', 'f | South African'),
        ('Boxing Union of Ireland', 'Boxing Union of Ireland'),
        ('M|Celtic', 'M | Celtic'),
        ('M|Irish', 'M  |Irish'),
        ('British Boxing Board of Control', 'British Boxing Board of Control'),
        ('M|BBBofC British', 'M | BBBofC British'),
        ('f|BBBofC British', 'f | BBBofC British'),
        ('M|BBBofC Celtic', 'M | BBBofC Celtic'),
        ('f|BBBofC Celtic', 'f | BBBofC Celtic'),
        ('M|BBBofC Central Area', 'M | BBBofC Central Area'),
        ('f|BBBofC Central Area', 'f | BBBofC Central Area'),
        ('M|BBBofC English', 'M | BBBofC English'),
        ('f|BBBofC English', 'f | BBBofC English'),
        ('M|BBBofC Midlands Area', 'M | BBBofC Midlands Area'),
        ('f|BBBofC Midlands Area', 'f | BBBofC Midlands Area'),
        ('M|BBBofC Northern Area', 'M | BBBofC Northern Area'),
        ('f|BBBofC Northern Area', 'f | BBBofC Northern Area'),
        ('M|BBBofC Northern Ireland Area', 'M | BBBofC Northern Ireland Area'),
        ('f|BBBofC Northern Ireland Area', 'f | BBBofC Northern Ireland Area'),
        ('M|BBBofC Scottish Area', 'M | BBBofC Scottish Area'),
        ('f|BBBofC Scottish Area', 'f | BBBofC Scottish Area'),
        ('M|BBBofC Southern Area', 'M | BBBofC Southern Area'),
        ('f|BBBofC Southern Area', 'f |BBBofC Southern Area'),
        ('M|BBBofC Welsh Area', 'M | BBBofC Welsh Area'),
        ('f|BBBofC Welsh Area', 'f | BBBofC Welsh Area'),
        ('M|BBBofC Western Area', 'M | BBBofC Western Area'),
        #
        ('M|BDB Ger Man', 'M | BDB Ger Man'),
        ('M|BDB International', 'M | BDB International'),
        ('M|Co M MonWealth Boxing Council', 'M | Co M MonWealth Boxing Council'),
        ('f|Co M MonWealth Boxing Council', 'f | Co M MonWealth Boxing Council'),
        ('M|Eurasian Boxing Parlia Ment', 'M | Eurasian Boxing Parlia Ment'),
        ('f|Eurasian Boxing Parlia Ment', 'f | Eurasian Boxing Parlia Ment'),
        ('M|EBU European', 'M | EBU European'),
        ('f|EBU European', 'f | EBU European'),
        ('M|EBU European Union', 'M | EBU European Union'),
        ('M|EBU External', 'M | EBU External'),
        ('M|EBU Silver', 'M | EBU Silver'),
        ('M|Argentinian', 'M | Argentinian'),
        ('f|Argentinian', 'f | Argentinian'),
        ('M|French', 'M | French'),
        ('f|French', 'f | French'),
        ('M|Federazione Pugilistica Italiana', 'M | Federazione Pugilistica Italiana'),
        ('f|Federazione Pugilistica Italiana', 'f | Federazione Pugilistica Italiana'),
        ('M|International', 'M | International'),
        ('M|National', 'M | National'),
        ('M|Intercontinental', 'M | Intercontinental'),
        ('M|World', 'M | World'),
        ('f|World', 'f | World'),
        ('M|World Youth', 'M | World Youth'),
        #
        ('M|WKF', 'M | WKF'),
        ('f|WKF', 'f | WKF'),
        ('M|WAKO', 'M | WAKO'),
        ('W|WAKO', 'W | WAKO'),
        ('M|ONE Champion', 'M | ONE Champion'),
        ('W|ONE Champion', 'W | ONE Champion'),
        ('M|WKA', 'M | WKA'),
        ('W|WKA', 'W | WKA'),
        ('M|GLORY', 'M | GLORY'),
        ('W|GLORY', 'W | GLORY'),
        ('M|RING20 KB', 'M | RING20 KB'),
        ('W|RING20 KB', 'W | RING20 KB'),
        ('M|WKB', 'M | WKB'),
        ('W|WKB', 'W | WKB'),
        ('M|WMC', 'M | WMC'),
        ('W|WMC', 'W | WMC'),
        ('M|WMF', 'M | WMF'),
        ('W|WMF', 'W | WMF'),
        ('M|WBC', 'M | WBC'),
        ('W|WBC', 'W  |WBC'),
        ('M|IFMA', 'M | IFMA'),
        ('W|IFMA', 'W | IFMA'),
        ('M|RING20 MT', 'M | RING20 MT'),
        ('W|RING20 MT', 'W | RING20 MT'),
        ('M|WMT', 'M | WMT'),
        ('W|WMT', 'W | WMT'),
        ('M|IKS', 'M | IKS'),
        ('W|IKS', 'W | IKS'),
        ('M|WKF', 'M  |WKF'),
        ('W|WKF', 'W | WKF'),
        ('M|IKF', 'M | IKF'),
        ('W|IKF', 'W | IKF'),
        ('M|ISKA', 'M | ISKA'),
        ('W|ISKA', 'W | ISKA'),
        ('M|RING20 K', 'M | RING20 K'),
        ('W|RING20 K', 'W | RING20 K'),
        ('OTHER', 'other'),
       
    )
    attributes = AttributesField()
    weight_class = models.CharField(max_length=20, choices=WEIGHT_CHOICES, verbose_name="event weight class")
    sport = models.CharField(max_length=20, blank=True,choices=CHAMPION_CHOICES, verbose_name="event sport style")
    sport_org = models.CharField(max_length=100, blank=True, choices=CHAMPION_CHOICES, verbose_name="event sport style")
    fight_card = models.ForeignKey(FightCard, on_delete=models.CASCADE, related_name='fightCard')
    match_name = models.CharField(max_length=50, blank=True, verbose_name="event name")
    image = FilerImageField(on_delete=models.PROTECT,blank=True, verbose_name="event image")
    broadcast = models.CharField(max_length=50, blank=True, verbose_name="event broadcast")
    promotion = models.CharField(max_length=50, blank=True, verbose_name="event promotion")
    ownership = models.CharField(max_length=50, blank=True, verbose_name="event ownership")
    venue = models.CharField(max_length=50, blank=True, verbose_name="event venue")
    country = CountryField(blank_label='(select country)', null=True, default='US')
    location = models.CharField(max_length=50, blank=True, verbose_name="event location")
    up_coming_date = models.DateTimeField(blank=True, verbose_name="event date")
    up_coming_bio = models.TextField(blank=True, verbose_name="event bio")
    social_media = models.URLField(max_length=200, blank=True, verbose_name="event social media")
    result_event = models.CharField(max_length=10,blank=True, choices=[('W', 'Winner Fighter 1'), ('L', 'Winner Fighter 2'), ('D', 'Draw'),('N/A', 'Not Specified'),('C', 'Cancled')], verbose_name="event result")
    def __str__(self):
        return f'{self.match_name} - {self.up_coming_date}'

class EventPluginModel(CMSPlugin):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="event")
    #location = models.CharField(max_length=200)
    #sport = models.CharField(max_length=200)
    #weight_class = models.CharField(max_length=200)
    #country = models.CharField(max_length=200)
"""