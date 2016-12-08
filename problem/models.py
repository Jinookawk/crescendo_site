from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Problem(models.Model):
	num = models.AutoField(primary_key=True)
	artifact = models.PositiveSmallIntegerField(null=True)
	title = models.CharField(max_length=50, blank=True)
	author = models.ForeignKey('auth.User')
	created_date = models.DateField(blank=True)
	level = models.PositiveSmallIntegerField(null=True)
	right_answer = models.CharField(max_length=100, null=True)
	submits = models.IntegerField(blank=True, null=True)
	corrects = models.IntegerField(blank=True, null=True)
	tags = models.CharField(max_length=200, null=True, blank=True)
	importance = models.PositiveSmallIntegerField(null=True)
	difficulty = models.PositiveSmallIntegerField(null=True)
	score = models.IntegerField(null=True)
	downfile = models.FileField(null=True, blank=True)
	content = models.TextField(null=True, blank=True)
	solve_user = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		return self.title

class Answerlog(models.Model):
	num = models.AutoField(primary_key=True)
	submitter = models.ForeignKey('auth.User')
	problem_num = models.IntegerField(null=True)
	problem_title = models.CharField(max_length=50, null=True)
	submit_answer = models.CharField(max_length=100, null=True)
	submit_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.submit_answer

class Scenario(models.Model):
	snum = models.IntegerField(null=True)
	answer_num = models.IntegerField(null=True)
	answer1 = models.CharField(max_length=100, null=True, blank=True)
	answer2 = models.CharField(max_length=100, null=True, blank=True)
	answer3 = models.CharField(max_length=100, null=True, blank=True)
	answer4 = models.CharField(max_length=100, null=True, blank=True)
	answer5 = models.CharField(max_length=100, null=True, blank=True)
	answer6 = models.CharField(max_length=100, null=True, blank=True)
        answer7 = models.CharField(max_length=100, null=True, blank=True)
        answer8 = models.CharField(max_length=100, null=True, blank=True)
        answer9 = models.CharField(max_length=100, null=True, blank=True)
        answer10 = models.CharField(max_length=100, null=True, blank=True)
        answer11 = models.CharField(max_length=100, null=True, blank=True)
        answer12 = models.CharField(max_length=100, null=True, blank=True)
        answer13 = models.CharField(max_length=100, null=True, blank=True)
        answer14 = models.CharField(max_length=100, null=True, blank=True)
        answer15 = models.CharField(max_length=100, null=True, blank=True)
