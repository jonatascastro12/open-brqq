from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    region = models.CharField(max_length=30, null=True, blank=True)
    video = models.ForeignKey('main.GloboVideo', on_delete=models.SET_NULL, null=True, blank=True)
    treated_subtitle_part = models.TextField(null=True, blank=True)

    content1 = models.TextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)

    def has_treated_subtitle(self):
        return self.treated_subtitle_part is not None

    has_treated_subtitle.short_description = 'Has Treated Subtitle?'
    has_treated_subtitle.boolean = True

    def has_analysis(self):
        return self.keywordanalysis_set.count() > 0

    has_analysis.short_description = 'Has Analysis?'
    has_analysis.boolean = True

    def __str__(self):
        return str(self.name + '-' + self.uf)

    class Meta:
        ordering = ['uf', 'name']


class GloboVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    globo_id = models.IntegerField(null=True, blank=True)
    video_info = models.TextField(null=True, blank=True)

    exhibited_at = models.DateField(null=True, blank=True)

    subtitle_url = models.CharField(max_length=255)
    subtitle_content = models.TextField(null=True, blank=True)
    subtitle_cleaned_content = models.TextField(null=True, blank=True)

    error_on_clean = models.BooleanField(default=False)

    def __str__(self):
        return str(self.globo_id)

    def has_subtitle(self):
        return self.subtitle_url != ''

    has_subtitle.short_description = 'Has Subtitle?'
    has_subtitle.boolean = True


