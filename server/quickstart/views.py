from django.contrib.auth import authenticate
from django.http import FileResponse
from django.http import Http404,HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from PyPDF2 import PdfFileWriter

from django.views.decorators.csrf import csrf_exempt

from quickstart.models import ExampleModel
from quickstart.serializers import ExampleModelSerializer,appModelSerializer,testModelSerializer

from rest_framework.parsers import JSONParser

from quickstart.models import ExampleModel,appModel, formsModel,testModel
from quickstart.forms import  UploadForm

import json
import requests
import pdfrw
import os
import shortuuid
from datetime import date



ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        if type(data_dict[key]) == bool:
                            if data_dict[key] == True:
                                annotation.update(pdfrw.PdfDict(
                                    AS=pdfrw.PdfName('Yes')))
                        else:
                            annotation.update(
                                pdfrw.PdfDict(V='{}'.format(data_dict[key]),Ff=1)
                            )
                            annotation.update(pdfrw.PdfDict(AP=''))
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)
#give path
def path_find(str,uid):
    if(str=="birth certificate"):
    	p="./media/applied/birthcertificate/"+"ap"+uid+".pdf"
    	return p
    elif(str=="death certificate"):
    	p="./media/applied/deathcertificate/"+"ap"+uid+".pdf"
    	return p
#to dict
def to_dic(d,n,index):
    l=len(d)
    d2=[]
    d1=[]
    d3=[]
    d4=[]
    dict={}
    dict1={}
    for i in range(0,l):
    	if(n[i]=="birth certificate"):
            d1.append(d[i])  
            d3.append(index[i])
            res_dct = {d3[i]: d1[i] for i in range(0, len(d1))}
            dict={"birthcertificate":res_dct}
    	elif(n[i]=="death certificate"):
            d2.append(d[i])
            d4.append(index[i])
            res_dct1 = {d4[i]: d2[i] for i in range(0, len(d2))}
            dict1={"deathcertificate":res_dct1}		
    res = not dict
    res1= not dict1
    if(str(res)=='True')and(str(res1)=='True'):
    	dict3={"b":"null","d":"null"}
    elif(str(res)!='True')and(str(res1)=='True'):
        	dict3={"b":dict,"d":"null"}
    elif(str(res)=='True')and(str(res1)!='True'):
        	dict3={"b":"null","d":dict1}
    else:
    	dict3={"b":dict,"d":dict1}
    return dict3
         
@csrf_exempt
def file_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')       
    

@csrf_exempt
def testApi(request, id=0):
	if request.method=='GET':
		data=ExampleModel.objects.all()
		t_serializer=ExampleModelSerializer(data, many=True)
		return JsonResponse(t_serializer.data, safe=False)
	elif request.method=='POST': 
		data=JSONParser().parse(request)
		email = str(data['email'])
		check=ExampleModel.objects.filter(email=email).exists()
		if check is True:
    			return JsonResponse("FAIL",safe=False)
		else:	
			r = requests.post('http://127.0.0.1:8009/mine_block', data = json.dumps(data))
			y = json.loads(r.text)
			index= str(y['index'])
			data1={"email": email ,"index": index }
			node={"nodes":["http://127.0.0.1:8009","http://127.0.0.1:8008"]}
			t = requests.post('http://127.0.0.1:8009/replace_chain')
			m = requests.post('http://127.0.0.1:8008/replace_chain')
			f = requests.post('http://127.0.0.1:8009/connect_node', data = json.dumps(node) )
			t_serializer=ExampleModelSerializer(data=data1)
			if t_serializer.is_valid():
				t_serializer.save()	
				return JsonResponse("success",safe=False)
			return JsonResponse("fail", safe=False)
	elif request.method=='DELETE':
		data=ExampleModel.objects.get(userid=id)
		data.delete()
		return JsonResponse("Deleted..",safe=False)

@csrf_exempt
def login(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		email = str(data['email'])
		check=ExampleModel.objects.filter(email=email).exists()
		if check is True:
			data2=ExampleModel.objects.filter(email=email)
			res=(list(data2.values("index")))
			res1=res[0]
			f = requests.get('http://127.0.0.1:8009/get_details', data = json.dumps(res1))
			y = json.loads(f.text)
			pswd=y['details'][0]['DATA']['pswd']
			return JsonResponse(pswd, safe=False)
		return JsonResponse("Fail",safe=False)

@csrf_exempt
def loggedin(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		email = str(data['email'])
		check=ExampleModel.objects.filter(email=email).exists()
		if check is True:
			data2=ExampleModel.objects.filter(email=email)
			res=(list(data2.values("index")))
			res1=res[0]
			f = requests.get('http://127.0.0.1:8009/get_details', data = json.dumps(res1))
			y = json.loads(f.text)
			fname=y['details'][0]['DATA']['firstname']
			return JsonResponse(fname, safe=False)
		return JsonResponse("Fail",safe=False)

@csrf_exempt
def get_pdf(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		title=str(data['appname'])	
		check=formsModel.objects.filter(title=title).exists()
		if check is True:
			app=formsModel.objects.filter(title=title)
			res=(list(app.values("pdf")))
			print(res)
			res1=res[0]		
		template_input="media/"+res1['pdf']
		userid = str(data['userid'])
		check=ExampleModel.objects.filter(email=userid).exists()
		uid=shortuuid.uuid()
		if check is True:
			data2=ExampleModel.objects.filter(email=userid)
			res=(list(data2.values("index")))
			res1=res[0]
			dict={"index":res1['index'],"appname":title,"uid":uid,"time":""}
			f = requests.post('http://127.0.0.1:8009/add_app', data = json.dumps(dict))
		tempfile = open("temp.txt","w+")
		tempfile.write(uid)
		tempfile.close()
		path=path_find(title,uid)
		f = open(path, "x")
		template_output=path
		data_dict={
			'aname':str(data['aname']),
			'address':str(data['address']),
			'bname':str(data['bname']),
			'dob':str(data['dob']),
			'bmname':str(data['bmname']),
			'bfname':str(data['bfname']),
			'adddress2':str(data['adddress2']),
			'pob':str(data['pob']),
			'regno':str(data['regno']),
			'name':str(data['name1']),
			'phno':str(data['phno']),
			'place':str(data['place']),
			'date':str(data['date']),}
		fill_pdf(template_input,template_output, data_dict)
		data1={"uid": uid ,"pdf": path,"email":userid}
		t_serializer=appModelSerializer(data=data1)
		if t_serializer.is_valid():
			t_serializer.save()	
		f_serializer=testModelSerializer(data=data1)
		if f_serializer.is_valid():
			f_serializer.save()	
		dict_uid={'uid':uid,'s':"Success"}
		return JsonResponse(dict_uid,safe=False)
	if request.method=='GET':
		f = open("temp.txt", "r")
		uid=f.read()
		f.close()
		check=appModel.objects.filter(uid=uid).exists()
		if check is True:
			app=appModel.objects.filter(uid=uid)
			res=(list(app.values("pdf")))
			res1=res[0]	
			template_output=res1['pdf']
		return FileResponse(open(template_output, 'rb'), content_type='application/pdf')

@csrf_exempt
def get_appl(request):
	if request.method=='POST':
		data=JSONParser().parse(request)
		email = str(data['email'])
		check=ExampleModel.objects.filter(email=email).exists()
		if check is True:
			data2=ExampleModel.objects.filter(email=email)
			res=(list(data2.values("index")))
			res1=res[0]
			f = requests.get('http://127.0.0.1:8009/get_app', data = json.dumps(res1))
			y = json.loads(f.text)
			appl=y['details']
			d=[]
			n=[]
			index=[]
			for i in range(1,len(appl)):
				d.append(appl[i]['uid'])
				n.append(appl[i]['appname'])
				index.append(appl[i]['index'])
			dict=to_dic(d,n,index)
			return JsonResponse(dict, safe=False)
		return JsonResponse("Fail",safe=False)

