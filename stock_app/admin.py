# # admin.py

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
# from .models import Stock

# class StockAdmin(admin.ModelAdmin):
#     list_display = ('id', 'symbol')

# admin.site.register(Stock, StockAdmin)

# admin.site.unregister(User)  # Unregister the default User admin
# class CustomUserAdmin(UserAdmin):
#     list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')
#     search_fields = ('username', 'email', 'first_name', 'last_name')
#     ordering = ('-date_joined',)

# admin.site.register(User, CustomUserAdmin)


from django.contrib import admin
from .models import Stock, Watchlist

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol')

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_stocks')

    def get_stocks(self, obj):
        return ", ".join([stock.symbol for stock in obj.stocks.all()])

admin.site.register(Stock, StockAdmin)
admin.site.register(Watchlist, WatchlistAdmin)