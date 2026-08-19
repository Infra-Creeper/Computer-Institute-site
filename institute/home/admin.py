from django.contrib import admin
from .models import Admission, Contact, Notice


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = (
        'ref_id', 'name', 'course_name', 'contact_number',
        'category', 'gender', 'submitted_at',
    )
    list_filter = ('category', 'gender', 'course_name', 'submitted_at')
    search_fields = ('ref_id', 'name', 'guardian', 'contact_number', 'course_name')
    readonly_fields = ('ref_id', 'submitted_at')
    date_hierarchy = 'submitted_at'
    ordering = ('-submitted_at',)

    fieldsets = (
        ('Application', {
            'fields': ('ref_id', 'course_name', 'submitted_at')
        }),
        ('Applicant Details', {
            'fields': (
                'name', 'guardian', 'dob', 'gender',
                'nationality', 'category', 'highest_qualification',
            )
        }),
        ('Contact', {
            'fields': ('contact_number', 'address')
        }),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_or_phone', 'short_message', 'is_read', 'submitted_at')
    list_filter = ('is_read', 'submitted_at')
    search_fields = ('name', 'email_or_phone', 'message')
    readonly_fields = ('submitted_at',)
    date_hierarchy = 'submitted_at'
    ordering = ('-submitted_at',)
    list_editable = ('is_read',)
    actions = ['mark_as_read', 'mark_as_unread']

    def short_message(self, obj):
        return (obj.message[:60] + '…') if len(obj.message) > 60 else obj.message
    short_message.short_description = 'Message'

    @admin.action(description="Mark selected messages as read")
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Mark selected messages as unread")
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'published_at')
    search_fields = ('title', 'message')
    readonly_fields = ('number', 'published_at')
    date_hierarchy = 'published_at'
    ordering = ('-number',)