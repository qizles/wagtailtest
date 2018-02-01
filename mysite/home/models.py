from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.models import TextField
from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import TextBlock

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.wagtailforms.models import AbstractFormField, AbstractEmailForm
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
    body = RichTextField(blank=True)
    intro = TextField(blank=True)
    heading1 = models.CharField(blank=True, max_length=80)
    text1 = TextField(blank=True)

    heading2 = models.CharField(blank=True, max_length=80)
    text2 = TextField(blank=True)

    heading3 = models.CharField(blank=True, max_length=80)
    text3 = TextField(blank=True)

    heading4 = models.CharField(blank=True, max_length=80)
    text4 = TextField(blank=True)

    heading5 = models.CharField(blank=True, max_length=80)
    text5 = TextField(blank=True)

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
        FieldPanel('body', classname="full"),
        FieldPanel('intro', classname="full"),
        MultiFieldPanel([
            FieldPanel('heading1'),
            FieldPanel('text1', classname="full"),
        ], heading="Block 1"),

        MultiFieldPanel([
            FieldPanel('heading2'),
            FieldPanel('text2', classname="full"),
        ], heading="Block 2"),

        MultiFieldPanel([
            FieldPanel('heading3'),
            FieldPanel('text3', classname="full"),
        ], heading="Block 3"),

        MultiFieldPanel([
            FieldPanel('heading4'),
            FieldPanel('text4', classname="full"),
        ], heading="Block 4"),

        MultiFieldPanel([
            FieldPanel('heading5'),
            FieldPanel('text5', classname="full"),
        ], heading="Block 5"),

        ImageChooserPanel('imageone'),
        ImageChooserPanel('imagetwo'),
    ]


class AGBsPage(Page):
    text = TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),

    ]


class GenericPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
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


class StreamFieldTestPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('text', blocks.TextBlock()),
        ('image', ImageChooserBlock()),
    ])
    text = TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        StreamFieldPanel('body'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldPanel('to_address', classname="full"),
            FieldPanel('from_address', classname="full"),
            FieldPanel('subject', classname="full"),
        ], "Email")
    ]
