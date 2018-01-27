from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.models import TextField
from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    welcomeheading = models.CharField(blank=True, max_length=30)
    subforhighlight = models.CharField(blank=True, max_length=30)
    subhighlight = models.CharField(blank=True, max_length=30)
    subafterhighlight = models.CharField(blank=True, max_length=30)

    card1heading = models.CharField(blank=True, max_length=30)
    card1text = TextField(blank=True)
    card1symbol = models.CharField(blank=True, max_length=30)
    card2heading = models.CharField(blank=True, max_length=30)
    card2text = TextField(blank=True)
    card2symbol = models.CharField(blank=True, max_length=30)
    card3heading = models.CharField(blank=True, max_length=30)
    card3text = TextField(blank=True)
    card3symbol = models.CharField(blank=True, max_length=30)


    imagemidsub = models.CharField(blank=True, max_length=80)

    para1heading = models.CharField(blank=True, max_length=30)
    para1sub = models.TextField(blank=True)

    imageendsub = models.CharField(blank=True, max_length=80)

    para2heading = models.CharField(blank=True, max_length=30)
    para2sub = models.TextField(blank=True)

    backgroundimage = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('welcomeheading'),
            MultiFieldPanel([
                FieldPanel('subforhighlight'),
                FieldPanel('subhighlight'),
                FieldPanel('subafterhighlight'),
            ], heading="Welcome Sub Message"),
        ], heading="Welcome Message"),

        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('card1heading'),
                FieldPanel('card1text', classname="full"),
                FieldPanel('card1symbol'),
            ], heading="Card 1"),

            MultiFieldPanel([
                FieldPanel('card2heading'),
                FieldPanel('card2text', classname="full"),
                FieldPanel('card2symbol'),
            ], heading="Card 2"),

            MultiFieldPanel([
                FieldPanel('card3heading'),
                FieldPanel('card3text', classname="full"),
                FieldPanel('card3symbol'),
            ], heading="Card 3"),

        ], heading="Cards"),

        FieldPanel('imagemidsub', classname="full"),

        MultiFieldPanel([
            FieldPanel('para1heading'),
            FieldPanel('para1sub', classname="full"),
        ], heading="Paragraph 1"),

        FieldPanel('imageendsub', classname="full"),

        MultiFieldPanel([
            FieldPanel('para2heading'),
            FieldPanel('para2sub', classname="full"),
        ], heading="Paragraph 2"),

        ImageChooserPanel('backgroundimage'),
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
