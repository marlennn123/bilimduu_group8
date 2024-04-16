from modeltranslation.translator import register, TranslationOptions
from .models import Car


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('category', 'marka', 'model', 'city', 'country', 'color', 'description')
