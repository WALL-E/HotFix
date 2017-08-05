from django.contrib import admin

from .models import System, Category, App, Version, Patch, Release


class SystemAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']

class AppAdmin(admin.ModelAdmin):
    fields = ['name', 'category_id', 'system_id', 'key', 'secret', 'rsa']
    list_display = ('name', 'category_id', 'system_id', 'key', 'secret', 'rsa')
    list_filter = ['name', 'category_id', 'system_id']
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']

class VersionAdmin(admin.ModelAdmin):
    fields = ['name', 'app_id']
    list_display = ('name', 'app_id', 'create_time')
    list_filter = ['name', 'app_id__name', 'create_time']
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']

class PatchAdmin(admin.ModelAdmin):
    fields = ['serial_number', 'version_id', 'size', 'desc']
    list_display = ('serial_number', 'version_id', 'size', 'desc', 'upload_time')
    list_filter = ['size', 'upload_time', 'version_id__name']
    search_fields = ['serial_number']

    def get_ordering(self, request):
        return ['serial_number']

class ReleaseAdmin(admin.ModelAdmin):
    fields = ['patch_id', 'is_enable', 'update_time', 'download_count', 'apply_count', 'is_gray', 'pool_size']
    list_display = ('patch_id', 'is_enable', 'is_gray', 'create_time')
    list_filter = [
        'patch_id__serial_number', 
        'is_enable', 
        'is_gray', 
        'create_time',
    ]
    search_fields = ['name']

admin.site.register(System, SystemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Patch, PatchAdmin)
admin.site.register(Release, ReleaseAdmin)
