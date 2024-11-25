from django.db import models

class Model1(models.Model):
    set_number = models.CharField(max_length=100, verbose_name='Set #')
    reps = models.IntegerField(verbose_name='Reps')
    min_in_w_o = models.IntegerField(verbose_name='Min in W/O')

    def __str__(self):
        return f'Set: {self.set_number}, Reps: {self.reps}, Min: {self.min_in_w_o}'