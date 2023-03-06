# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin'


class Comment(models.Model):
    comment = models.TextField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    post_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'


class Post(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'post'


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    school_division = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    cgpa = models.CharField(max_length=255)
    official_id = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    subscription = models.IntegerField()
    created_id = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
