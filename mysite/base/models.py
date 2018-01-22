from django.db import models

# Create your models here.
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


@register_snippet
class Footer(models.Model):
    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer"

    class Meta:
        verbose_name_plural = 'Footer'


@register_snippet
class Navbar(models.Model):
    name = models.CharField(max_length=25)
    body = RichTextField()
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('body'),
        ImageChooserPanel('logo'),
    ]

    def __str__(self):
        return "Navbar"

    class Meta:
        verbose_name_plural = 'Navbar'
