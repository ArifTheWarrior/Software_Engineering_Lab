# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Registration(models.Model):
    name = models.CharField(db_column='Name', max_length=220)  # Field name made lowercase.
    university_email = models.CharField(db_column='University Email', max_length=220)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    department = models.CharField(db_column='Department', max_length=200)  # Field name made lowercase.
    student_id = models.IntegerField(db_column='Student ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', max_length=220)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=220)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=100)  # Field name made lowercase.
    post_code = models.CharField(db_column='Post-Code', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_number = models.CharField(db_column='Phone Number', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    n_id_card = models.IntegerField(db_column='N-ID Card')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'registration'
