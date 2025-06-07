from django.db import models

# Create your models here.

class Concept(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название концепции")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Концепция"
        verbose_name_plural = "Концепции"

class HistoricalContext(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='historical_contexts')
    period = models.CharField(max_length=100, verbose_name="Исторический период")
    description = models.TextField(verbose_name="Описание исторического контекста")
    
    def __str__(self):
        return f"{self.concept.title} - {self.period}"

    class Meta:
        verbose_name = "Исторический контекст"
        verbose_name_plural = "Исторические контексты"

class Quote(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='quotes')
    author = models.CharField(max_length=200, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст цитаты")
    source = models.CharField(max_length=200, verbose_name="Источник")
    
    def __str__(self):
        return f"{self.author} - {self.text[:50]}..."

    class Meta:
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"

class Source(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='sources')
    title = models.CharField(max_length=200, verbose_name="Название источника")
    author = models.CharField(max_length=200, verbose_name="Автор")
    year = models.IntegerField(verbose_name="Год публикации")
    description = models.TextField(verbose_name="Описание")
    url = models.URLField(blank=True, null=True, verbose_name="Ссылка")
    
    def __str__(self):
        return f"{self.author} - {self.title}"

    class Meta:
        verbose_name = "Источник"
        verbose_name_plural = "Источники"
