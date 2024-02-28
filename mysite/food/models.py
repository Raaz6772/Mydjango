from django.db import models

class item(models.Model):
    
    def __str__(self):
        return self.item_name

    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=50000,default="data:image/jpeg;base64,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")
