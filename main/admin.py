from django.contrib import admin

# Register your models here.
from main.models import GloboVideo, City

class CityInline(admin.TabularInline):
    model = City


class GloboVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'has_subtitle', 'exhibited_at', 'error_on_clean']
    search_fields = ['title', 'subtitle_content', 'exhibited_at', 'error_on_clean']
    list_filter = ['error_on_clean']
    inlines = [
        CityInline
    ]


admin.site.register(GloboVideo, GloboVideoAdmin)


class NullListFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        return (
            ('1', 'Não',),
            ('0', 'Sim',),
        )

    def queryset(self, request, queryset):
        if self.value() in ('0', '1'):
            kwargs = {'{0}__isnull'.format(self.parameter_name): self.value() == '1'}
            return queryset.filter(**kwargs)
        return queryset


class TratedSubtitleNullListFilter(NullListFilter):
    title = u'Has treated subtitle?'
    parameter_name = u'treated_subtitle_part'



class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'uf', 'video', 'has_treated_subtitle', 'has_analysis']
    search_fields = ['name', 'uf', 'treated_subtitle_part', ]
    list_filter = [TratedSubtitleNullListFilter, ]
    # autocomplete_fields = ['subtitle_keyword']
    exclude = ['content3']
    # radio_fields = {'keyword_sentiment': admin.HORIZONTAL}

    pass


admin.site.register(City, CityAdmin)


