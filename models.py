# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AttDetGatTat(models.Model):
    empno = models.ForeignKey('AttMastGatTat', models.DO_NOTHING, db_column='empno', blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    att_dt = models.DateField(blank=True, null=True)
    att_typ = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_det_gat_tat'


class AttLocnMast(models.Model):
    locn_code = models.IntegerField(primary_key=True)
    locn_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_locn_mast'


class AttMastGatTat(models.Model):
    empno = models.IntegerField(primary_key=True)
    locn_cd = models.ForeignKey(AttLocnMast, models.DO_NOTHING, db_column='locn_cd', blank=True, null=True)
    zone = models.CharField(max_length=5, blank=True, null=True)
    dept = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_mast_gat_tat'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Crick(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crick'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Football(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'football'


class LocnAttLocnMast(models.Model):
    locn_code = models.IntegerField(primary_key=True)
    locn_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locn_att_locn_mast'


class LocnAttMastGatTat(models.Model):
    empno = models.IntegerField(primary_key=True)
    zone = models.CharField(max_length=5, blank=True, null=True)
    dept = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    locn_cd = models.ForeignKey(LocnAttLocnMast, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'locn_att_mast_gat_tat'


class LocnAttdetgattat(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    att_dt = models.DateField()
    att_typ = models.CharField(max_length=2, blank=True, null=True)
    empno = models.ForeignKey(LocnAttMastGatTat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'locn_attdetgattat'
