from django.contrib.auth import authenticate
from django.http import FileResponse
from django.http import Http404,HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail


from django.views.decorators.csrf import csrf_exempt

from quickstart.serializers import employeeModelSerializer,appModelSerializer,temp1ModelSerializer

from rest_framework.parsers import JSONParser

from quickstart.models import employeeModel,appModel,temp1Model

import json
import requests

@csrf_exempt
def employeesignup(request, id=0):
	if request.method=='GET':
		data=employeeModel.objects.all()
		t_serializer=employeeModelSerializer(data, many=True)
		return JsonResponse(t_serializer.data, safe=False)
	elif request.method=='POST': 
		data=JSONParser().parse(request)
		f_serializer=employeeModelSerializer(data=data)
		if f_serializer.is_valid():
		    f_serializer.save()
		    return JsonResponse("success",safe=False)
		return JsonResponse("Fail",safe=False)
	elif request.method=='DELETE':
		data=employeeModel.objects.get(userid=id)
		data.delete()
		return JsonResponse("Deleted..",safe=False)
@csrf_exempt
def employeelogin(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		eid = str(data['eid'])
		check=employeeModel.objects.filter(eid=eid).exists()
		if check is True:
		    d=employeeModel.objects.filter(eid=eid)
		    res=list(d.values('pswd'))
		    res2=list(d.values('fname'))
		    res1=res[0]
		    res3=res2[0]
		    dict={"pswd":res1,"fname":res3}
		    return JsonResponse(dict,safe=False)
		return JsonResponse("Fail",safe=False)
@csrf_exempt
def view_app(request):
	if request.method=='POST':
		data1=JSONParser().parse(request)
		uid=str(data1['uid'])
		check=appModel.objects.filter(uid=uid).exists()
		if check is True:
			app=appModel.objects.filter(uid=uid)
			app1=list(app.values("uid"))
			app2=list(app.values("pdf"))
			data={"uid":app1[0]['uid'],"pdf":app2[0]['pdf']}
			t_serializer=temp1ModelSerializer(data=data)
			if t_serializer.is_valid():
			    t_serializer.save()	
			    return JsonResponse ("success",safe=False)
	if request.method=='GET':
		data=appModel.objects.all()
		t_serializer=appModelSerializer(data, many=True)
		d=json.loads(json.dumps(t_serializer.data))
		d1=d[0]['uid']
		check=appModel.objects.filter(uid=d1).exists()
		if check is True:
			app=temp1Model.objects.filter(uid=d1)
			res=(list(app.values("pdf")))
			res1=res[0]	
			template_output=res1['pdf']
			data1=temp1Model.objects.get(uid=d1)
			data1.delete()
		return FileResponse(open(template_output, 'rb'), content_type='application/pdf')
@csrf_exempt
def send_email(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		uid = str(data['uid'])
		check=appModel.objects.filter(uid=uid).exists()
		if check is True:
			email=appModel.objects.filter(uid=uid)
			app1=list(email.values("email"))
			app2=app1[0]['email']
			subject = 'Egovernance Application Status'
			message = f'Hi {app2}, Your application completed stage 1.'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [app2]
			send_mail( subject, message, email_from, recipient_list )
		return JsonResponse ("success",safe=False)
@csrf_exempt
def send_email1(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		uid = str(data['uid'])
		check=appModel.objects.filter(uid=uid).exists()
		if check is True:
			email=appModel.objects.filter(uid=uid)
			app1=list(email.values("email"))
			app2=app1[0]['email']
			subject = 'Egovernance Application Status'
			message = f'Hi {app2}, Your application was accepted.'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [app2]
			send_mail( subject, message, email_from, recipient_list )
		return JsonResponse ("success",safe=False)
@csrf_exempt
def send_email2(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		uid = str(data['uid'])
		check=appModel.objects.filter(uid=uid).exists()
		if check is True:
			email=appModel.objects.filter(uid=uid)
			app1=list(email.values("email"))
			app2=app1[0]['email']
			subject = 'Egovernance Application Status'
			message = f'Hi {app2}, Your application was rejected.'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [app2]
			send_mail( subject, message, email_from, recipient_list )
		return JsonResponse ("success",safe=False)