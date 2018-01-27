from django.db import models

# Create your models here.
from django.db.models import TextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page


class TravelIndexPage(Page):
    text = TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),

    ]


class JourneyPage(Page):
    maintext = TextField(blank=True)

    info1 = TextField(blank=True)

    info2 = TextField(blank=True)

    info3 = TextField(blank=True)





    # what does a journey need

    # - map

    content_panels = Page.content_panels + [
        FieldPanel('maintext', classname="full"),
        FieldPanel('info1', classname="full"),
        FieldPanel('info2', classname="full"),
        FieldPanel('info3', classname="full"),

    ]
