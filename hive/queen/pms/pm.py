#!/usr/bin/python
# -*- coding: UTF-8 -*-
from base.APIConstants import Constants
from base.APIMessage import PushMessage
from APISender import APISender
from GTManager import *
from queen.models import Token

import os

def register(post):
	hw_token = post['hw']
	obj, created = Token.objects.get_or_create(token=hw_token,default={'platform':'hw'})
	return json.dumps({'result':'ok','created':created})

def push(post):
    title = post['title']
    content = post['content']
    extra = post['extra']
    notify = post.get('notification','').strip()
    payload = post.get('payload','').strip()
    platforms = []
    test = []
    save_flag = post.get('save','')
    if post.get('mi','').strip():
        platforms.append('mi')
    if post.get('huawei','').strip():
        platforms.append('huawei')
    if post.get('getui','').strip():
        platforms.append('getui')
    if post.get('umeng','').strip():
        platforms.append('umeng')
    if post.get('jpush','').strip():
        platforms.append('jpush')
    if post.get('tt','').strip():
        platforms.append('tt')
    if post.get('baidu','').strip():
        platforms.append('baidu')
    if post.get('ali','').strip():
        platforms.append('ali')
    if notify :
        #send
        if platforms.count('mi'):
            test.append(push_mi(title+'_mi',content,extra))
        if platforms.count('huawei'):
            test.append(push_hw(title+'_huawei',content,extra))
        if platforms.count('getui'):
            test.append(push_gt(title+'_gt',content,extra))
        if platforms.count('umeng'):
            test.append(push_umeng(title+'_umeng',content,extra))
        if platforms.count('jpush'):
            test.append(push_jpush(title+'_jpush',content,extra))
        if platforms.count('tt'):
            test.append(push_tt(title+'_tt',content,extra))
        if platforms.count('baidu'):
            test.append(push_baidu(title+'_baidu',content,extra))
        if platforms.count('ali'):
            test.append(push_ali(title+'_ali',content,extra))
    if payload :
        #send
        if platforms.count('mi'):
            test.append(payload_mi(title+'_mi',content,extra))
        if platforms.count('huawei'):
            test.append(payload_hw(title+'_huawei',content,extra))
        if platforms.count('getui'):
            test.append(payload_gt(title+'_gt',content,extra))
        if platforms.count('umeng'):
            test.append(payload_umeng(title+'_umeng',content,extra))
    return test

def payload_mi(title, content, extra):
    return do_mi(title,content,extra,1)

def push_mi(title, content, extra):
    return do_mi(title,content,extra,0)

def do_mi(title, content, extra,payload):
    Constants.use_official()
    sender = APISender('jRmdPFa8mBprOYIQ6Hzbrw==')
    # android message
    message = PushMessage() \
    .restricted_package_name('com.daivp.pushcollector') \
    .title(title).description(content) \
    .pass_through(payload).payload(extra)
    recv = sender.broadcast_all(message.message_dict())
    result={'title':'小米 '+('Notification' if payload==1 else 'Payload')}
    result['status']= (0 if recv['result']=='ok' else 1)
    result['message'] = str(recv)
    return result

def push_gt(title, content, extra):
    return do_gt(title, content, extra,False)

def payload_gt(title, content, extra):
    return do_gt(title, content, extra,True)

def do_gt(title, content, extra,payload):
    result={'title':'个推 '+('Payload' if payload else 'Notification')}
    result['status']= 1
    result['message'] = ''
    token = read_config('getui')
    recv = json.loads(send_gt(title, content, extra,token,payload))
    if recv['result']=='not_auth':
        auth_recv = json.loads(auth_gt())
        if auth_recv['result']=='ok':
            token = auth_recv['auth_token']
            write_config('getui',token)
            recv = json.loads(send_gt(title, content, extra,token,payload))
            result['status']= (0 if recv['result']=='ok' else 1)
            result['message'] = str(recv)
        else :
            result['status']= 0
            result['message'] = str(auth_recv)
    else :
        result['status']= (0 if recv['result']=='ok' else 1)
        result['message'] = str(recv)   
    return result

def push_hw(title, content, extra): 
    return do_hw(title, content, extra,False)

def payload_hw(title, content, extra): 
    return do_hw(title, content, extra,True)

def do_hw(title, content, extra,payload):    
    result={'title':'华为 '+('Payload' if payload else 'Notification')}
    result['status']= 1
    result['message'] = ''
    token = read_config('huawei')
    users = []
    users_qs = Token.objects.filter(platform='hw')
    for uq in users_qs:
    	users.append(uq.token)
    recv = json.loads(send_hw(title, content, extra,token,payload,users))
    if recv.has_key('error') and (recv['error']=='invalid session'):
        #{"error":"invalid session"}
        recv = json.loads(auth_hw())
        #{"access_token":"CFkG7s5SwjV9x13OiTWa4LHpix9ySPZoIAbMJMondgt1us2Pnncmu1SlC05bOKMTP7Z14qrMWfHs2u6VAm1pow==","expires_in":604800}
        if recv.has_key('access_token'):
            token = recv['access_token']
            write_config('huawei',token)
            recv = json.loads(send_hw(title, content, extra,token,payload,users))
    #{"message":"success","requestID":"14930373561127240","resultcode":0}
    result['status']= (0 if (recv.has_key('resultcode') and recv['resultcode']==0) else 1)
    result['message'] = str(recv)
    return result
def push_umeng(title, content, extra):
    return do_umeng(title, content, extra,False)

def payload_umeng(title, content, extra):
    return do_umeng(title, content, extra,True)

def do_umeng(title, content, extra,payload):
    #{"ret":"SUCCESS","data":{"task_id":"us46209149302982428600"}}
    result={'title':'友盟 '+('Payload' if payload else 'Notification')}
    recv = json.loads(send_umeng(title, content, extra,payload))
    result['status']= (0 if (recv.has_key('ret') and recv['ret']=='SUCCESS') else 1)
    result['message'] = str(recv)   
    return result

def push_jpush(title, content, extra):
    return {'title':'极光PSUH','status':1,'message':'not support'}

def push_tt(title, content, extra):
    return {'title':'腾讯信鸽','status':1,'message':'not support'}

def push_baidu(title, content, extra):
    return {'title':'百度云','status':1,'message':'not support'}

def push_ali(title, content, extra):
    return {'title':'阿里云','status':1,'message':'not support'}