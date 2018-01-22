from django import template
from ..models import Footer , Navbar

register = template.Library()


@register.inclusion_tag('footer.html', takes_context=True)
def getFooter(context):
    footer = ""
    if Footer.objects.first() is not None:
        footer = Footer.objects.first().body

    return {
        'footer': footer,
    }


@register.inclusion_tag('navbar.html', takes_context=True)
def getNavbar(context):
    navbar = ""
    logo = ""
    if Navbar.objects.first() is not None:
        navbar = Navbar.objects.first().name
        logo = Navbar.objects.first().logo

    return {
        'navbar': navbar,
        'logo': logo,
    }
