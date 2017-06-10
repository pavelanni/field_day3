from django.db import models


# As per https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/
# we set blank=True in the model fields to make them non-required in
# the model form

class Visitor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    call_sign = models.SlugField(max_length=10, blank=True)
    nfarl_member = models.BooleanField()
    contact_me = models.BooleanField()
    email = models.EmailField(blank=True)
    first_time = models.BooleanField(default=False)
    younger_than_18 = models.BooleanField(default=False)
# TODO add date and time of registration

    def __str__(self):
        return self.last_name
