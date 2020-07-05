from django-modeltranslation import register, TranslationOptions
from .models import Article

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('body')