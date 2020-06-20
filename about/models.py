"""About page."""
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class AboutPage(Page):

    template = "about/about_page.html"

    # @todo add streamfields
    # content timezone= StreamField()

    banner_title = models.CharField(max_length=20, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )


 
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
    
    ]

class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
