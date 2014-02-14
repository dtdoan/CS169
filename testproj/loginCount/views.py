from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from loginCount.models import UserModel
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render
import json


def login(request):
    if request.method == 'POST':
	user_request = json.loads(request.body)
        new_user = user_request['username']
        user_password = user_request['password']

        err_code = UserModel.login(new_user, user_password)
        dictionary['errCode'] = err_code

        if err_code == UserModel.SUCCESS:
            returning_user = UserInfo.objects.get(username=new_user)
            dictionary['count'] = returning_user.count
            
    return HttpResponse(json.dumps(dictionary), content_type='application/json')

    
def add(request):
    if request.method == 'POST':
        user_req = json.loads(request.body)
        new_user = user_req['username']
        user_password = user_req['password']

        err_code = UserModel.login(new_user, user_password)
        dictionary['errCode'] = err_code

        if err_code == UserModel.SUCCESS:
            returning_user = UserInfo.objects.get(username=new_user)
            dictionary['count'] = returning_user.count
            
    return HttpResponse(json.dumps(dictionary), content_type='application/json')


def default(request):
    return HttpResponse('default')


