from django.db import models


class Goods(models.Model):

    TYPES = ((1, 'Laptops'),
             (2, 'Tablets'))

    name = models.CharField(max_length=256)
    type = models.IntegerField(choices=TYPES)
    description = models.TextField(max_length=2048)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(default='', upload_to='image')

    def __str__(self):
        return f' {self.id} {self.name} {self.description} '
