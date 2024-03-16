from django.contrib import admin
from .models import New, Category, Tag, About, Contact, Ads
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    list_display_links=('id', 'name')
    prepopulated_fields={'slug': ['name']}



class NewAdmin (admin.ModelAdmin):
    list_display=('id', 'title', 'category', 'views')
    list_display_links=('id', 'title')
    prepopulated_fields={"slug": ['title']}
    readonly_fields=('views',)
    filter_horizontal=('tags',)


class AdsAdmin(admin.ModelAdmin):
    list_display=('id', 'link', 'position', 'is_active')
    list_editable=('is_active', 'position')


admin.site.register(New, NewAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Ads, AdsAdmin)