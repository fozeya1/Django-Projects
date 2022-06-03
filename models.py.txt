# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Golfcourse(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.TextField()
    course_total_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GolfCourse'


class Golfer(models.Model):
    golfer_id = models.IntegerField(primary_key=True)
    golfer_name = models.TextField()
    golfer_birthdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'Golfer'


class Golferroundscores(models.Model):
    grs_id = models.IntegerField(primary_key=True)
    grs_tourn_golfer = models.ForeignKey('Tourngolfer', models.DO_NOTHING)
    grs_round = models.ForeignKey('Round', models.DO_NOTHING)
    grs_total_score = models.IntegerField()
    grs_hole1_score = models.IntegerField()
    grs_hole2_score = models.IntegerField()
    grs_hole3_score = models.IntegerField()
    grs_hole4_score = models.IntegerField()
    grs_hole5_score = models.IntegerField()
    grs_hole6_score = models.IntegerField()
    grs_hole7_score = models.IntegerField()
    grs_hole8_score = models.IntegerField()
    grs_hole9_score = models.IntegerField()
    grs_hole10_score = models.IntegerField()
    grs_hole11_score = models.IntegerField()
    grs_hole12_score = models.IntegerField()
    grs_hole13_score = models.IntegerField()
    grs_hole14_score = models.IntegerField()
    grs_hole15_score = models.IntegerField()
    grs_hole16_score = models.IntegerField()
    grs_hole17_score = models.IntegerField()
    grs_hole18_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GolferRoundScores'


class Hole(models.Model):
    hole_id = models.IntegerField(primary_key=True)
    hole_course = models.ForeignKey(Golfcourse, models.DO_NOTHING)
    hole_number = models.IntegerField()
    hole_par = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Hole'


class Round(models.Model):
    round_id = models.IntegerField(primary_key=True)
    round_tourn = models.ForeignKey('Tournament', models.DO_NOTHING)
    round_day = models.TextField()

    class Meta:
        managed = False
        db_table = 'Round'


class Tourngolfer(models.Model):
    tg_id = models.IntegerField(primary_key=True)
    tg_tourn = models.ForeignKey('Tournament', models.DO_NOTHING)
    tg_golfer = models.ForeignKey(Golfer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TournGolfer'


class Tournament(models.Model):
    tourn_id = models.IntegerField(primary_key=True)
    tourn_name = models.TextField()
    tourn_course = models.ForeignKey(Golfcourse, models.DO_NOTHING)
    tourn_start_date = models.DateField()
    tourn_num_rounds = models.IntegerField()
    tourn_num_golfers = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Tournament'
