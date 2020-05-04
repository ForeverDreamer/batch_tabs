from django.db import models


class Url(models.Model):
    # id，AutoField/IntegerFieldValues from -2147483648 to 2147483647
    # are safe in all databases supported by Django.
    # 每天增加1000条记录，一辈子3万天id也才自增到3千万
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.url
