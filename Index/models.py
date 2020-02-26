from django.db import models

class KingQueenData(models.Model):
    names=models.CharField(max_length=225)
    major=models.CharField(max_length=225,default='BE')
    number=models.IntegerField()
    image=models.ImageField(upload_to='KingQueenData')
    def __str__(self):
        return self.names

class MisterMissData(models.Model):
    names = models.CharField(max_length=225)
    major = models.CharField(max_length=225, default='BE')
    number = models.IntegerField()
    image = models.ImageField(upload_to='MisterMissData')

    def __str__(self):
        return self.names

class King(models.Model):
    king=models.IntegerField()
    def __str__(self):
        return 'king %s added' %self.king

class Queen(models.Model):
    queen=models.IntegerField()
    def __str__(self):
        return 'queen %s added' %self.queen

class Mister(models.Model):
    mister=models.IntegerField()
    def __str__(self):
        return 'king %s added' %self.mister

class Miss(models.Model):
    miss = models.IntegerField()

    def __str__(self):
        return 'king %s added' % self.miss

class Cos(models.Model):
    cos = models.IntegerField()

    def __str__(self):
        return 'king %s added' % self.cos

class PopMister(models.Model):
    pmis=models.IntegerField()
    def __str__(self):
        return self.pmis
class PopMiss(models.Model):
    pmiss=models.IntegerField()
    def __str__(self):
        return self.pmiss

class APP(models.Model):
    app=models.FileField(upload_to='App')


class IMEIs(models.Model):
    imei=models.CharField(max_length=225)
    King=models.BooleanField(default=False)
    Queen=models.BooleanField(default=False)
    Mister = models.BooleanField(default=False)
    Miss = models.BooleanField(default=False)
    popMister=models.BooleanField(default=False)
    popMiss=models.BooleanField(default=False)

    cos= models.BooleanField(default=False)
    def __str__(self):
        return self.imei



