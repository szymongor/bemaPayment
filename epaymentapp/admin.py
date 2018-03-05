from django.contrib import admin
from .models import Post, SiteUser, Bill, Payment


class BillAdmin(admin.ModelAdmin):
    # Klasa do wyświetlania płatności powiązanych z rachunkiem
    class PaymentsInline(admin.TabularInline):
        model = Payment
        extra = 1 #Tylko jeden form do dodawania nowej płatności, domyślnie są 3 (lol)

    inlines = [
        PaymentsInline,
    ]


admin.site.register(SiteUser)
admin.site.register(Post)
admin.site.register(Bill, BillAdmin)
admin.site.register(Payment)