from urllib.request import Request
from django.contrib.auth import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, pre_init, post_init
from django.core.signals import request_started, request_finished, got_request_exception

@receiver(user_logged_in, sender=User)
def Login_success(sender, request, user, **kwargs):
    print('User Login SUccessfull: ----Intro user')
    print('Request Sender: ', sender)
    print('This User: ',user)
    print('User First Name: ', user.first_name)
    print('request: ', request)
    print(f'KWARGS: {kwargs}')
    
    
# user_logged_in.connect(Login_success, sender=User)

@receiver(user_logged_out, sender=User)
def Login_out(sender, request, user, **kwargs):
    print('User Login Out SUccessfull: ----Outro user')
    print('Request Sender: ', sender)
    print('This User: ',user)
    print('User First Name: ', user.first_name)
    print('request: ', request)
    print(f'KWARGS: {kwargs}')

@receiver(user_login_failed)

def Login_fail(sender,credentials , request, **kwargs):
    print('Opps! User Login Faild')
    print('Sender: ', sender)
    print(credentials)
    print(request)
    

@receiver(pre_save, sender=User)
def pre_biginning(sender, instance, **kwargs):
    
    print('Pre save Signals: -----------')
    print('Sender: ', sender)
    print("Instance: ", instance)
    print(f'KWARGS: {kwargs}')
    
    
@receiver(post_save, sender=User)
def Post_save(sender, instance, created, **kwargs):
    if created:
        print('POST save Signals: -----------')
        print('Sender: ', sender)
        print("Instance: ", instance)
        print('Created: ',created)
        print(f'KWARGS: {kwargs}')
    else:
        print('-----------User Updated----------')
        

@receiver(pre_delete, sender=User)
def pre_delete(sender, instance, **kwargs):
    
    print('Pre Delete Signals: -----------')
    print('Sender: ', sender)
    print("Instance: ", instance)
    print(f'KWARGS: {kwargs}')
    

@receiver(post_delete, sender=User)
def post_delete(sender, instance, **kwargs):
    
    print('POST Delete Signals: -----------')
    print('Sender: ', sender)
    print("Instance: ", instance)
    print(f'KWARGS: {kwargs}')
    
# @receiver(pre_init, sender=User)
# def pre_init(sender, *args, **kwargs):
    
#     print('Pre Init Signals: -----------')
#     print('Sender: ', sender)
#     print(f'Args: {args}')
#     print(f'KWARGS: {kwargs}')
    
    
# @receiver(post_init, sender=User)
# def post_init(sender, *args, **kwargs):
    
#     print('Post Init Signals: -----------')
#     print('Sender: ', sender)
#     print(f'Args: {args}')
#     print(f'KWARGS: {kwargs}')

@receiver(request_started)
def request_start(sender, environ, **kwargs):
    print('-----------------------------Request Started---------------------------')
    print('Sender: ', sender)
    print("Environ: ",environ)
    print(f'Kwargs: {kwargs}')
    
@receiver(request_finished)
def request_start(sender,**kwargs):
    print('-----------------------------Request Finished---------------------------')
    print('Sender: ', sender)
    print(f'Kwargs: {kwargs}')

@receiver(got_request_exception)
def request_ex(sender, request, **kwargs):
    print('-----------------------------Got Zero Divition Exeption--------------------')
    print('Request: ', request)
    print('Sender: ', sender)
    print(f'Kwargs: {kwargs}')