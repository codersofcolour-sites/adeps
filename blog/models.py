from django.db import models
from wagtail.core import blocks
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


from wagtail.embeds.blocks import EmbedBlock

'''
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField([
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('embed', EmbedBlock(icon="media")),
])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    def get_context(self, request):
        # Update context to include only published posts, 
        # in reverse chronological order
        context = super(BlogIndexPage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        return context
    '''

class BlogPage(Page):
    date = models.DateField("Post date")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('image'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]




    