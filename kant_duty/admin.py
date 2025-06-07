from django.contrib import admin
from .models import Concept, HistoricalContext, Quote, Source

@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(HistoricalContext)
class HistoricalContextAdmin(admin.ModelAdmin):
    list_display = ('concept', 'period')
    list_filter = ('concept',)
    search_fields = ('period', 'description')

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'source', 'concept')
    list_filter = ('concept', 'author')
    search_fields = ('text', 'author', 'source')

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'concept')
    list_filter = ('concept', 'year')
    search_fields = ('title', 'author', 'description')
