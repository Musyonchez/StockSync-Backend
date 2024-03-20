from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    current = models.FloatField(default=0)
    reorder_level = models.FloatField(default=0, db_column='reorderLevel')
    unit_cost = models.FloatField(default=0, db_column='unitCost')
    selling_price = models.FloatField(default=0, db_column='sellingPrice')
    tax_information = models.FloatField(default=0, db_column='taxInformation')
    image_url = models.CharField(max_length=255, default='null', db_column='imageURL')
    supplier = models.CharField(max_length=255, default='null')
    active = models.BooleanField(default=True)
    first_record_action = models.BooleanField(default=False, db_column='firstRecordAction')
    bar_code = models.FloatField(default=0, db_column='barCode')

    class Meta:
        db_table = 'Products'
