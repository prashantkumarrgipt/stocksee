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