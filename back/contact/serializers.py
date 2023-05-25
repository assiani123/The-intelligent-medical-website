from rest_framework import serializers
from contact.models import  E,User, messg, notm, notp, rdv,messgm


class rdvs(serializers.ModelSerializer):
     class Meta:
        model = rdv
        fields = ['id','nomm','nomp','date','Time','prix','spec','etat']
from django.contrib.auth.hashers import make_password
class U(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name','nomp' ,'email', 'password','prix','spec','role','phone']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
class ms(serializers.ModelSerializer):
    class Meta:
        model = messg
        fields = ['id', 'nome', 'nomc', 'mesg']
class msm(serializers.ModelSerializer):
    class Meta:
        model = messgm
        fields = ['id', 'nome', 'nomc', 'mesg']
class notps(serializers.ModelSerializer):
    class Meta:
        model = notp
        fields = ['id', 'nomp', 'notp']
class notms(serializers.ModelSerializer):
    class Meta:
        model = notm
        fields = ['id', 'nomm', 'notm']

