from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock

from streams import blocks

class AboutPage(Page):
   body = RichTextField(blank=True)