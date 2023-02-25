from django.http import FileResponse
from django.http import Http404,HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from quickstart.serializers import appModelSerializer,test1ModelSerializer,testModelSerializer,accpModelSerializer
from quickstart.serializers import rejectModelSerializer,sec_appModelSerializer,sec_accpModelSerializer,tempModelSerializer
from quickstart.serializers import temp1ModelSerializer,temp2ModelSerializer
from rest_framework.parsers import JSONParser

from quickstart.models import ExampleModel,appModel, formsModel,testModel,test1Model,temp2Model
from quickstart.models import accpModel,rejectModel,sec_appModel,sec_accpModel,tempModel,temp1Model
from quickstart.forms import  UploadForm

import json
import requests



@csrf_exempt
def for_appl(request):
	if request.method=='GET':
		data=testModel.objects.all()
		t_serializer=testModelSerializer(data, many=True)
		d=json.loads(json.dumps(t_serializer.data))
		l=len(d)
		for i in range(0,l):
		    d1=d[i]
		    f_serializer=test1ModelSerializer(data=d1)
		    if f_serializer.is_valid():
		        f_serializer.save()
		    data1=testModel.objects.get(uid=d1['uid'])
		    data1.delete()
		return JsonResponse("success", safe=False)
@csrf_exempt
def view_appl(request):
	if request.method=='POST':
		data1=JSONParser().parse(request)
		uid=str(data1['uid'])
		check=appModel.objects.filter(uid=uid).exists()
		if check is True:
			app=appModel.objects.filter(uid=uid)
			app1=list(app.values("uid"))
			app2=list(app.values("pdf"))
			data={"uid":app1[0]['uid'],"pdf":app2[0]['pdf']}
			t_serializer=tempModelSerializer(data=data)
			if t_serializer.is_valid():
			    t_serializer.save()	
			    return JsonResponse ("success",safe=False)
	if request.method=='GET':
		data=tempModel.objects.all()
		t_serializer=testModelSerializer(data, many=True)
		d=json.loads(json.dumps(t_serializer.data))
		d1=d[0]['uid']
		check=appModel.objects.filter(uid=d1).exists()
		if check is True:
			app=appModel.objects.filter(uid=d1)
			res=(list(app.values("pdf")))
			res1=res[0]	
			template_output=res1['pdf']
			data1=tempModel.objects.get(uid=d1)
			data1.delete()
		return FileResponse(open(template_output, 'rb'), content_type='application/pdf')

@csrf_exempt
def  accp_clerk(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		uid=str(data['uid'])
		check=test1Model.objects.filter(uid=uid).exists()
		if check is True:
		    app=test1Model.objects.filter(uid=uid)
		    app1=list(app.values("uid"))
		    app2=list(app.values("pdf"))
		    data={"uid":app1[0]['uid'],"pdf":app2[0]['pdf']}
		    t_serializer=accpModelSerializer(data=data)
		    if t_serializer.is_valid():
			    t_serializer.save()	
		    data1=test1Model.objects.get(uid=uid)
		    data1.delete()
		    return JsonResponse ("success",safe=False)

@csrf_exempt
def  rej_clerk(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		uid=str(data['uid'])
		reas=str(data['reas'])
		check=test1Model.objects.filter(uid=uid).exists()
		if check is True:
		    app=test1Model.objects.filter(uid=uid)
		    app1=list(app.values("uid"))
		    app2=list(app.values("pdf"))
		    data={"uid":app1[0]['uid'],"pdf":app2[0]['pdf'],"reas":reas}
		    t_serializer=rejectModelSerializer(data=data)
		    if t_serializer.is_valid():
			    t_serializer.save()	
		    data1=test1Model.objects.get(uid=uid)
		    data1.delete()
		    return JsonResponse ("success",safe=False)
@csrf_exempt
def sec_for_appl(request):
	if request.method=='POST':
		data=accpModel.objects.all()
		t_serializer=accpModelSerializer(data, many=True)
		d=json.loads(json.dumps(t_serializer.data))
		l=len(d)
		for i in range(0,l):
		    d1=d[i]
		    f_serializer=sec_appModelSerializer(data=d1)
		    if f_serializer.is_valid():
		        f_serializer.save()
		    data1=accpModel.objects.get(uid=d1['uid'])
		    data1.delete()
		return JsonResponse("success", safe=False)
@csrf_exempt
def sec_view_appl(request):
	if request.method=='POST':
		data1=JSONParser().parse(request)
		uid=str(data1['uid'])
		check=sec_appModel.objects.filter(uid=uid).exists()
		if check is True:
			app=appModel.objects.filter(uid=uid)
			app1=list(app.values("uid"))
			app2=list(app.values("pdf"))
			data={"uid":app1[0]['uid'],"pdf":app2[0]['pdf']}
			t_serializer=temp2ModelSerializer(data=data)
			if t_serializer.is_valid():
			    t_serializer.save()	
			    return JsonResponse ("success",safe=False)
	if request.method=='GET':
		data=temp2Model.objects.all()
		t_serializer=sec_appModelSerializer(data, many=True)
		d=json.loads(json.dumps(t_serializer.data))
		print(d)
		d1=d[0]['uid']
		check=appModel.objects.filter(uid=d1).exists()
		if check is True:
			app=appModel.objects.filter(uid=d1)
			res=(list(app.values("pdf")))
			res1=res[0]	
			template_output=res1['pdf']
			data1=temp2Model.objects.get(uid=d1)
			data1.delete()
		return FileResponse(open(template_output, 'rb'), content_type='application/pdf')
@csrf_exempt
def  sec_accp(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		uid=str(data['uid'])
		coll_d=str(data['coll_d'])
		check=sec_appModel.objects.filter(uid=uid).exists()
		if check is True:
		    app=sec_appModel.objects.filter(uid=uid)
		    app1=list(app.values("uid"))
		    app2=list(app.values("pdf"))
		    data={"uid":app1[0]['uid'],"pdf":app2[0]['pdf'],"coll_d":coll_d}
		    t_serializer=sec_accpModelSerializer(data=data)
		    if t_serializer.is_valid():
			    t_serializer.save()	
		    data1=sec_appModel.objects.get(uid=uid)
		    data1.delete()
		    return JsonResponse ("success",safe=False)
@csrf_exempt
def  sec_rej(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		print(data)
		uid=str(data['uid'])
		reas=str(data['reas'])
		print(reas)
		print(uid)
		check=sec_appModel.objects.filter(uid=uid).exists()
		if check is True:
		    app=sec_appModel.objects.filter(uid=uid)
		    app1=list(app.values("uid"))
		    app2=list(app.values("pdf"))
		    data={"uid":app1[0]['uid'],"pdf":app2[0]['pdf'],"reas":reas}
		    t_serializer=rejectModelSerializer(data=data)
		    if t_serializer.is_valid():
			    t_serializer.save()	
		    data1=sec_appModel.objects.get(uid=uid)
		    data1.delete()
		    return JsonResponse ("success",safe=False)
@csrf_exempt
def get_test1(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		uid = str(data['uid'])
		check=test1Model.objects.filter(uid=uid).exists()
		if check is True:
			dict={"status":"Yes0","reas":""}
			return JsonResponse(dict,safe=False)
		check1=accpModel.objects.filter(uid=uid).exists()
		if check1 is True:
			dict={"status":"Yes1","reas":""}
			return JsonResponse(dict,safe=False)
		check5=sec_appModel.objects.filter(uid=uid).exists()
		if check5 is True:
			dict={"status":"Yes5","reas":""}
			return JsonResponse(dict,safe=False)
		check2=rejectModel.objects.filter(uid=uid).exists()
		if check2 is True:
			app=rejectModel.objects.filter(uid=uid)
			app1=list(app.values("reas"))
			dict={"status":"Yes2","reas":app1[0]['reas']}
			return JsonResponse(dict,safe=False)
		check3=test1Model.objects.filter(uid=uid).exists()
		if check3 is True:
			dict={"status":"Yes4","reas":""}
			return JsonResponse(dict,safe=False)
		check4=sec_accpModel.objects.filter(uid=uid).exists()
		if check4 is True:
			app=sec_accpModel.objects.filter(uid=uid)
			app1=list(app.values("coll_d"))
			dict={"status":"Yes3","reas":app1[0]['coll_d']}
			return JsonResponse(dict,safe=False)
		return JsonResponse("No",safe=False)
@csrf_exempt
def get_app_clerk(request):
	if request.method=='POST':
		data=test1Model.objects.all().values('uid')
		d=list(data)
		l=len(d)
		d3=[]
		if(l==0):
			return JsonResponse("Null",safe=False)
		else:
			for i in range(0,l):
				d3.append(d[i]['uid'])
			d1={"data":d3}
		return JsonResponse(d1['data'],safe=False)
@csrf_exempt
def get_secapp(request):
	if request.method=='POST':
		data=sec_appModel.objects.all().values('uid')
		d=list(data)
		l=len(d)
		d3=[]
		if(l==0):
			return JsonResponse("Null",safe=False)
		else:
			for i in range(0,l):
				d3.append(d[i]['uid'])
			d1={"data":d3}
		return JsonResponse(d1['data'],safe=False)
@csrf_exempt
def get_secaccp(request):
	if request.method=='POST':
		data=sec_accpModel.objects.all().values('uid')
		d=list(data)
		l=len(d)
		d3=[]
		if(l==0):
			return JsonResponse("Null",safe=False)
		else:
			for i in range(0,l):
				d3.append(d[i]['uid'])
			d1={"data":d3}
		return JsonResponse(d1['data'],safe=False)
@csrf_exempt
def get_rej(request):
	if request.method=='POST':
		data=rejectModel.objects.all()
		d=list(data.values('uid'))
		d1=list(data.values('reas'))
		l=len(d)
		d3=[]
		d4=[]
		if(l==0):
			return JsonResponse("Null",safe=False)
		else:
			for i in range(0,l):
				d3.append(d[i]['uid'])
				d4.append(d1[i]['reas'])
			d1={"data":d3,"reas":d4}
		return JsonResponse(d1,safe=False)
