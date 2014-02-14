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
            returning_user = UserModel.objects.get(username=new_user)
            dictionary['count'] = returning_user.count
            
    return HttpResponse(json.dumps(dictionary), content_type='application/json')

    '''    
    try:
        returning_user = UserModel.objects.get(username=new_user)
    except UserModel.DoesNotExist:
        raise Http404
        return UserModel.ERR_BAD_CREDENTIALS

    if returning_user.password != user_password:
        return UserModel.ERR_BAD_CREDENTIALS

    returning_user.count += 1
    return returning_user.count
        '''
    
def add(request):
    if request.method == 'POST':
        user_req = json.loads(request.body)
        new_user = user_req['username']
        user_password = user_req['password']

        err_code = UserModel.login(new_user, user_password)
        dictionary['errCode'] = err_code

        if err_code == UserModel.SUCCESS:
            returning_user = UserModel.objects.get(username=new_user)
            dictionary['count'] = returning_user.count
            
    return HttpResponse(json.dumps(dictionary), content_type='application/json')

    '''
    try:
        print('Test if user exists in db')
        return add_user == UserModel.objects.get(username=new_user)
    except e: #UserModel.DoesNotExist:
        print('User does not exist')
        return UserModel.ERR_BAD_CREDENTIALS

    def valid_username(username):
        print('isValidUsername Test')
        return username != "" and len(username) <= UserModel.MAX_USERNAME_LENGTH

    def valid_password(password):
        print('isValidPassword Test')
        return len(password) <= UserModel.MAX_PASSWORD_LENGTH
    
    if not valid_username(add_user.username):
        print('returns bad username')
        return UserModel.ERR_BAD_USERNAME
    if not valid_password(add_user.password):
        print('returns bad password')
        return UserModel.ERR_BAD_PASSWORD
    user_added = UserModel(username=new_user, password=user_password, count=1)
    user_added.save()
    return user_added.count
        '''


def default(request):
    return HttpResponse('login/default.html')


