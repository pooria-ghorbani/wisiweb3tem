from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from app_data import AppDataForm
from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _


class FighterConfig(AppHookConfig):
    paginate_by = models.PositiveIntegerField(
        _('Paginate size'),
        blank=False,
        default=10,
    )


class FighterConfigForm(AppDataForm):
    title = forms.CharField()
setup_config(FighterConfigForm, FighterConfig)