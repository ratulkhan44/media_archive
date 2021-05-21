from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django_admin_listfilter_dropdown.filters import (ChoiceDropdownFilter,
                                                      DropdownFilter,
                                                      RelatedDropdownFilter)

from .models import Category, Entry, Source, Tag


# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display=('category','tag','source','date','title','content_file','content_url')
    list_filter=(('category',RelatedDropdownFilter),('source',RelatedDropdownFilter),('tag',RelatedDropdownFilter),('date',DateFieldListFilter))
    search_fields=('title',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Source)



admin.site.register(Entry,EntryAdmin)
