from django.contrib import admin

# Register your models here.
from .models import Audio,Video,Artiste

class tc(admin.ModelAdmin):
    list_display = ("artiste","identification_code","title","description","audio_file","cover_picture",)
    list_filter = ("title","artiste",)


class tc2(admin.ModelAdmin):
    list_display = ("artiste","identification_code","title","description","video_file",)
    list_filter = ("title","artiste",)

class tc3(admin.ModelAdmin):
    list_display = ("artiste","identification_code","description","artiste_picture",)
    list_filter = ("artiste",)



admin.site.register(Audio,tc)
admin.site.register(Video,tc2)
admin.site.register(Artiste,tc3)



# from .models import Payment

# Register your models here.

# class show(admin.ModelAdmin):
#      list_display=("verified","email","amount","ref","date_created",)
#      list_filter=("email",)
#
# admin.site.register(Payment, show)