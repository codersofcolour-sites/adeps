from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core import blocks

from wagtail.embeds.blocks import EmbedBlock



class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    

    banner_title = models.CharField(max_length=100, blank=False, null=True)
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
        FieldPanel('intro', classname="full"),   
    ]

    def get_context(self, request):
        # Update context to include only published posts,
        # in reverse chronological order
        context = super(BlogIndexPage, self).get_context(request)
        live_blogpages = self.get_children().live().specific()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        return context
  

class BlogPage(Page):

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('embed', EmbedBlock(icon="media")),
    ])
    image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
        ]


  

    