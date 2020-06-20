from django.db import models

"""Donate page."""
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class DonatePage(Page):

    template = "donate/donate_page.html"

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    # @todo add streamfields
    #content = StreamField()

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

class Meta:
        verbose_name = "Donate Page"
        verbose_name_plural = "Donate Pages"

# Create your models here.
