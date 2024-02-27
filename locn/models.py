from django.db import models

class AttLocnMast(models.Model):
    locn_code = models.IntegerField(primary_key=True)
    locn_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.locn_name

    class Meta:
        managed = False
        db_table = 'att_locn_mast'


 
class AttMastGatTat(models.Model):
    empno = models.IntegerField(primary_key=True)
    locn_cd = models.ForeignKey(AttLocnMast, models.DO_NOTHING, db_column='locn_cd', blank=True, null=True)
    zone = models.CharField(max_length=5, blank=True, null=True)
    dept = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True, choices=[
        ('Not Reported', 'Not Reported'),
        ('Resigned', 'Resigned'),
        ('Transferred', 'Transferred')
    ])

    def __str__(self):
        return f"{self.empno} - {self.zone} - {self.dept}"

    class Meta:
        managed = False
        db_table = 'att_mast_gat_tat'


class AttDetGatTat(models.Model):
    empno = models.ForeignKey('AttMastGatTat', models.DO_NOTHING, db_column='empno', blank=True, null=True)
 
    name = models.CharField(primary_key=True,max_length=30, blank=True, null=True)
    att_dt = models.DateField(blank=True, null=True)
    att_typ = models.CharField(max_length=2, blank=True, null=True, choices=[
        ('P', 'Present'),
        ('A', 'Absent'),
        ('CL', 'Casual Leave'),
        ('SL', 'Sick Leave'),
        ('OO', 'Weekly Off'),
        ('H', 'Holiday'),
        ('OH', 'Optional Holiday')
    ])

    def __str__(self):
        return f"{self.name} - {self.att_dt} - {self.get_att_typ_display()}"

    class Meta:
        managed = False
        db_table = 'att_det_gat_tat'

