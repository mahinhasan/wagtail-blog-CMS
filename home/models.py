from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,PageChooserPanel
from wagtail.images.edit_handlers import ImageFieldComparison
from wagtail.fields import RichTextField



class HomePage(Page):
    templates = 'home/home_page.html'
    banner_ttile = models.CharField(max_length=200,null=True,blank=True)
    banner_subtitle = RichTextField()
    # banner_image = models.ForeignKey(
    #     "wagtailimages.Image",
    #     null=True,
    #     blank=False,
    #     on_delete=models.SET_NULL,
    #     related_name="banner",
    # )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
         null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="banner",
    )
    content_panels = Page.content_panels + [
        FieldPanel("banner_ttile"),
        FieldPanel("banner_subtitle"),
        # FieldPanel("banner_image"),
        PageChooserPanel("banner_cta")
    ]
