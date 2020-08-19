from django.contrib import admin
from dictionarysite import models

admin.AdminSite.empty_value_display = '- (° ͜ʖ͡°) -'


@admin.register(models.Word)
class WordAdminForm(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'creation_date_time'
    list_display = ['word', 'user', 'language', 'is_not_display']
    list_display_links = ['word', ]
    filter_horizontal = ['groups', ]
    # radio_fields = {"language": admin.VERTICAL}
    list_editable = ['is_not_display', 'language']
    list_filter = ['language', 'groups', 'user', 'is_not_display', 'creation_date_time']
    readonly_fields = ['user', 'creation_date_time', 'slug', ]
    # list_max_show_all = 200
    list_per_page = 20
    save_on_top = True
    search_fields =['word', 'translation', 'note']
    fieldsets = (
        (None, {
            'fields': ('user', ('word', 'translation'), 'language', 'groups')
        }),
        ('Description', {
            'fields': ('note', ),
            'classes': ('collapse ', ),
        }),
        ('Advanced', {
            'fields': ('priority', 'rank', 'slug'),
            'classes': ('collapse ',),
        }),
        ('', {
            'fields': ('is_not_display', )
        })
    )

    class Meta:
        model = models.Word
        fields = '__all__'


admin.site.register(models.Group)
admin.site.register(models.Language)
