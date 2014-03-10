from django.db import models
  

class PlayerStatus(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Player(models.Model):
    first_name  = models.CharField(max_length=200)
    patronymic  = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    birthday    = models.DateTimeField('date published')
    height = models.IntegerField();
    weight = models.IntegerField();
    game_number = models.CharField(max_length=200)
    role          = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)

    status = models.ForeignKey(PlayerStatus)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question
