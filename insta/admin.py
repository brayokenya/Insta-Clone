from django.contrib import admin
from .models import User,Update,tags,Category,Location
# Register your models here.
class UpdateAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


admin.site.register(User)
admin.site.register(Update, UpdateAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(tags)