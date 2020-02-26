from rest_framework import serializers
from .models import KingQueenData,IMEIs,King,Queen,Miss,Mister,Cos,MisterMissData,PopMiss,PopMister,APP

class AppSerial(serializers.ModelSerializer):
    class Meta:
        model = APP
        fields=['app']

class KingQueenSerial(serializers.ModelSerializer):
    class Meta:
        model = KingQueenData
        fields=['names','number','image','major',]

class MisterMissSerial(serializers.ModelSerializer):
    class Meta:
        model = MisterMissData
        fields=['names','number','image','major',]

class ImeiSerial(serializers.ModelSerializer):
    class Meta:
        model=IMEIs
        fields=['imei','King','Queen','Mister','Miss','popMister','popMiss','cos']

#added
class KingSerial(serializers.ModelSerializer):
    class Meta:
        model = King
        fields=['king',]

class QueenSerial(serializers.ModelSerializer):
    class Meta:
        model = Queen
        fields=['queen',]

class MisterSerial(serializers.ModelSerializer):
    class Meta:
        model = Mister
        fields=['mister',]

class MissSerial(serializers.ModelSerializer):
    class Meta:
        model = Miss
        fields=['miss',]

class CosSerial(serializers.ModelSerializer):
    class Meta:
        model = Cos
        fields=['cos',]

class PMisterSerial(serializers.ModelSerializer):
    class Meta:
        model = PopMister
        fields=['pmis',]

class PMissSerial(serializers.ModelSerializer):
    class Meta:
        model = PopMiss
        fields=['pmiss',]
