from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.models import TextField
from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    text = TextField(blank=True)
    backgroundimageone = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    backgroundimagetwo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    backgroundimagethree = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('text', classname="full"),
        ImageChooserPanel('backgroundimageone'),
        ImageChooserPanel('backgroundimagetwo'),
        ImageChooserPanel('backgroundimagethree'),
    ]


class ImpressumPage(Page):
    text = TextField(blank=True)
    imageone = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    imagetwo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        ImageChooserPanel('imageone'),
        ImageChooserPanel('imagetwo'),
    ]


class AGBsPage(Page):
    text = TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),

    ]


class AboutUsPage(Page):
    text = TextField(blank=True)
    imageone = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    imagetwo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        ImageChooserPanel('imageone'),
        ImageChooserPanel('imagetwo'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class AboutUsGalleryImage(Orderable):
    page = ParentalKey(AboutUsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
