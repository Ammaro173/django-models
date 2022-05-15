from django.contrib import admin
from .models import Snack

# Register your models here.


# OR admin.site.register(Thing{.models !!})


@admin.register(Snack)
class AdminThing(admin.ModelAdmin):
    list_display = ("name", "purchaser", "description")
    search_fields = [
        "name",
    ]

    # list_display = ("name", "purchaser", "description")
    # search_fields = ("name", "purchaser", "description")
    # list_filter = ("name", "purchaser", "description")
