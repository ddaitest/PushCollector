#!/usr/local/bin/python  
#coding=utf-8

import time
from hashlib import sha256,md5
import requests
import json
import urllib
import ConfigParser

CONFIG_PATH = './queen/pms/token.ini'
#umeng - office
UMENG_APP_KEY = '54938e2efd98c5a805001212'
UMENG_MASTER_SECRET = '7fjia8dx9dso1l6janpl5lcjxj8r4qao'
#umeng - DAI
#UMENG_APP_KEY = '58ede1c6c62dca1bff0006b1'
#UMENG_MASTER_SECRET = 'nrto7fxwroofycjg20rngnipex0iqxmv'
#GT
GT_APPKEY = 'W8VFMontYp6NqclaB3UQJA'
GT_APP_ID = 'Pch3EpJM1AAm8PQUoVefSA'

#huawei - dai
HW_APP_ID = '10513650'
HW_CLIENT_SECRET = 'ukhno1k3nml2jhzc4m2k8g4r837xyrtu'
#huawei - dai
#HW_APP_ID = '10883659'
#HW_CLIENT_SECRET = '9f30eac14b1199ec57cab6e18e230a89'

#xinge
XINGE_ACCESS_ID = '2100256523'
XINGE_SECRET_KEY = '82e6c7ab131f83cef3f2970e2f95432d'

def auth_gt():
    url = "https://restapi.getui.com/v1/"+GT_APP_ID+"/auth_sign";
    postbody = {'appkey':GT_APPKEY}
    millis = int(round(time.time() * 1000 ))
    postbody['sign'] = sha256(GT_APPKEY+str(millis)+'DUwo6ah1Et64tEb8z3286').hexdigest()
    postbody['timestamp'] = millis
    r = requests.post(url, json=postbody)
    return r.text

def send_gt(title, content, extra, token, payload):
    postbody = {'requestid':str(long(round(time.time() * 1000 )))}
    message = {'appkey':GT_APPKEY,'is_offline':False,'msgtype':('transmission' if payload else 'notification')}
    postbody['message']=message
    if payload:
        notification = {'transmission_type':False,'transmission_content':str(extra)}
        postbody['transmission']=notification
    else :
        notification = {'transmission_type':False,'transmission_content':str(extra),'style':{'type':0,'text':content,'title':title}}        
        postbody['notification']=notification
    url = 'https://restapi.getui.com/v1/'+GT_APP_ID+'/push_app'
    header = {'authtoken':token}
    r = requests.post(url, json=postbody,headers=header)
    return r.text

def auth_hw():
    url = 'https://login.vmall.com/oauth2/token'
    postbody = {'grant_type':'client_credentials','client_id':HW_APP_ID,'client_secret':HW_CLIENT_SECRET}
    r = requests.post(url,postbody)
    return r.text

def send_hw(title, content, extra,token,payload,users):
    url = 'https://api.vmall.com/rest.php'
    action  = 'openpush.message.batch_send' if payload else 'openpush.message.psBatchSend'
    postbody = {'access_token':token, 'nsp_fmt':'JSON','nsp_ts':time.time(),'nsp_svc':action}
    postbody['cacheMode']='1'
    postbody['msgType']='1'
    postbody['userType']='1'
    android = {'notification_title':title,'notification_content':content,'doings':2,'intent':'intent://com.qding.push/parser#Intent;scheme=QDPUSH;S.notify_hw='+extra+';end'}
    # android = {'notification_title':title,'notification_content':content,'doings':1,'extras':[{'eee':extra}]}
    # "{\"notification_title\":\"the good news!\",\"notification_content\":\"Price reduction!\",\"doings\":3,\"url\":\"vmall.com\"}";
    if payload:
        postbody['message']=extra
    else:
        postbody['android']=json.dumps(android)
    postbody['deviceTokenList']=json.dumps(users)
    r = requests.post(url,postbody)
    return r.text

def send_umeng(title, content, extra,payload):
    url = 'http://msg.umeng.com/api/send'
    body = {'display_type':'notification','body':{'ticker':'提示文字','title':title,'text':content,'after_open':'go_custom','custom':extra}}
    if payload:
        body = {'display_type':'message','body':{'custom':extra}}
    postbody = {'appkey': UMENG_APP_KEY,'timestamp': int(time.time() * 1000),'type':'broadcast','payload':body}
    sign = md5('%s%s%s%s' % ('POST',url,json.dumps(postbody),UMENG_MASTER_SECRET)).hexdigest()
    r = requests.post(url+'?sign='+sign, json=postbody)
    return r.text

def read_config(key):
    cfg = ConfigParser.ConfigParser()
    cfg.read(CONFIG_PATH)
    cfg.sections()
    return cfg.get('token',key)

def write_config(key,value):
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(CONFIG_PATH)
        cf.set('token', key, value)
        cf.set('update',key,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
        cf.write(open(CONFIG_PATH,'w'))
    except:
        print 'exception'

def send_xg(title, content, extra,payload):
    url = 'http://openapi.xg.qq.com/v2/push/all_device'
    #notification: {"content":"this is content","title":"this is title", "vibrate":1}
    #payload: {"content":"this is content","title":"this is title"}
    params = {}
    params['access_id'] = XINGE_ACCESS_ID
    params['timestamp'] = time.time()
    if payload:
        params['message_type'] = 2
        params['message'] = json.dumps({"content":extra,"title":title})
    else :
        params['message_type'] = 1
        params['message'] = json.dumps({"content":content,"title":title,"vibrate":1,'builder_id':0})
    ks = sorted(params.keys())
    paramStr = ''.join([('%s=%s' % (k, params[k])) for k in ks])
    sign = md5('%s%s%s%s' % ('POST','openapi.xg.qq.com/v2/push/all_device',paramStr,XINGE_SECRET_KEY)).hexdigest()
    params['sign'] = sign
    r = requests.post(url,params)
    return r.text

def check_xg(pushid):
    url = 'http://openapi.xg.qq.com/v2/push/get_msg_status'
    #notification: {"content":"this is content","title":"this is title", "vibrate":1}
    #payload: {"content":"this is content","title":"this is title"}
    params = {}
    params['access_id'] = XINGE_ACCESS_ID
    params['timestamp'] = time.time()
    params['push_id'] = json.dumps([{"push_id":pushid}])    
    ks = sorted(params.keys())
    paramStr = ''.join([('%s=%s' % (k, params[k])) for k in ks])
    sign = md5('%s%s%s%s' % ('POST','openapi.xg.qq.com/v2/push/get_msg_status',paramStr,XINGE_SECRET_KEY)).hexdigest()
    params['sign'] = sign
    r = requests.post(url,params)
    return r.text

def main():
    #getui
    #token = 'CFkG7s5SwjV9x13OiTWa4LHpix9ySPZoIAbMJMondgt1us2Pnncmu1SlC05bOKMTP7Z14qrMWfHs2u6VAm1pow=='
    #huawei 
    #token = 'CFkJfdQXUJz/qdd8yVU/9V7bpRq63w+Q77podHRX3SvZHyZQpH2ifq6yG/ALXTn6l/ESvEYypso9/71Lr7gU0g=='
    print auth_hw()
    #print send_gt('a','b','c',token)
    #print send_hw('a','b','c',token,True)
    #print send_umeng('aaa','bbbb','ccc')
    #print send_xg('aaa','bb','cc',True)
    #print check_xg('2546955582')


if __name__ == '__main__':
    main()