from django.db import models

class MyField(models.Model):
    access_modifier = models.CharField(max_length=30)
    data_type = models.CharField(max_length=30)
    field_name = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}: {}'.format(self.access_modifier,
                                  self.data_type,
                                  self.field_name)

class MyArgument(models.Model):
    data_type = models.CharField(max_length=30)
    field_name = models.CharField(max_length=30)

    def __str__(self):
        return '{}: {}'.format(self.data_type,
                               self.field_name)

class MyMethod(models.Model):
    method_name = models.CharField(max_length=30)
    # method_args = models.CharField(max_length=100)
    method_return = models.CharField(max_length=30)

    def __str__(self):
        return '{}: {}'.format(self.method_name, self.method_return)

class MyClass(models.Model):
    class_name =