from rest_framework import serializers
from quickstart.models import ExampleModel,appModel,testModel,test1Model,employeeModel
from quickstart.models import accpModel,rejectModel,sec_appModel,sec_accpModel,tempModel,temp1Model,temp2Model

class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('email',
                  'index'
                  )
class employeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = employeeModel
        fields = ('fname','lname','eid','email',
                  'pswd'
                  )
class appModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=appModel
        fields=('uid',
                'pdf',
                'email')
class tempModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=tempModel
        fields=('uid',
                'pdf')
class temp2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=temp2Model
        fields=('uid',
                'pdf')
class temp1ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=temp1Model
        fields=('uid',
                'pdf')
class testModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=testModel
        fields=('uid',
                'pdf')
class test1ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=test1Model
        fields=('uid',
                'pdf')               
class accpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=accpModel
        fields=('uid',
                'pdf')
class rejectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=rejectModel
        fields=('uid',
                'pdf','reas')
class sec_appModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=sec_appModel
        fields=('uid',
                'pdf')
class sec_accpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=sec_accpModel
        fields=('uid',
                'pdf','coll_d')