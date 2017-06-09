from django.db import models


class Visitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    call_sign = models.SlugField(max_length=10)
    nfarl_member = models.BooleanField()
    contact_me = models.BooleanField()
    email = models.EmailField()
    first_time = models.BooleanField(default=False)
    younger_than_18 = models.BooleanField(default=False)
# TODO add date and time of registration

    def __str__(self):
        return self.last_name
