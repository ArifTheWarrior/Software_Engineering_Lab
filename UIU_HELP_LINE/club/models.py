from django.db import models

# Create your models here.
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
