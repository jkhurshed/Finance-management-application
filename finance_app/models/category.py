from django.db import models

class Category(models.Model):

    '''CATEGORY_CHOICES = (
        ('car', 'Car'),
        ('clothing', 'Clothing'),
        ('domiciliary', 'Domiciliary'),
        ('health and beauty', 'Health and Beauty'),
        ('kids', 'Kids'),
        ('leisure', 'Leisure'),
        ('sport', 'Sport'),
        ('supermarket', 'Supermarket'),
        ('transport', 'Transport'),
        ('travels', 'Travels'),
        ('not categorized', 'Not categorized'),
    )'''

    title = models.CharField("Title", max_length=70)
    parent = models.ForeignKey("self", 
                               on_delete=models.CASCADE, 
                               blank=True, 
                               null=True,
                               related_name="subcategories", 
                               verbose_name="Parent category")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    