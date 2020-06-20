"""About page."""
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class AboutPage(Page):

    template = "about/about_page.html"

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    # @todo add streamfields
    #content = StreamField()

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
