# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import base64
import time

import requests
from django.http import JsonResponse
from django.shortcuts import render
from blueking.component.shortcuts import get_client_by_user
import logging

client = get_client_by_user('liujiqing')
logger = logging.getLogger(__name__)

bk_app_code = 'blue-app'
bk_app_secret = '837d12fb-a738-4c04-9f61-c724fb2dddd8'
bk_token = 'F_uo0Iu2wg_FHaQR_xSPevIgWJdvt7IMofmTlOAuSRU'
from home_application.models import Scripts, Hosts
from home_application.logic import scriptfun

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/index_home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render(request, 'home_application/dev_guide.html')


def contact(request):
    """
    联系页
    """
    return render(request, 'home_application/contact.html')


# app日志界面
def app_logs(request):
    return render(request, 'logs.html')

def app_database(request):
    return render(request, 'app_database.html')

from home_application.models import Apps
from home_application.serializers import AppsSerializers,HostsSerializers

def saas_app(request):
    hid = request.GET.get('hid', 1)
    app_ser=AppsSerializers(Apps.objects.filter(server=hid).all(),many=True)
    return JsonResponse({"app_info":app_ser.data})

def host_view(request):
    hostsobj = Hosts.objects.all()
    hostser=HostsSerializers(hostsobj,many=True)
    return JsonResponse({'code':200,'data':hostser.data})



def search_logs(request):
    hid = request.GET.get('hid', '')
    app_code = request.GET.get('app_code', '')
    script_id = request.GET.get('script_id', '')
    print(hid, app_code)
    hostobj = Hosts.objects.get(pk=hid)

    script = Scripts.objects.get(pk=script_id)
    # 执行查询脚本
    job_id = scriptfun.excute_script(hostobj.hostip, hostobj.biz_id, script.scriptcontent.format(app_code))
    if not job_id:
        return JsonResponse({'code': 502, 'msg': '执行失败'})

    status_dict = scriptfun.get_job_status(hostobj.biz_id, job_id)
    if not status_dict:
        return JsonResponse({'code': 502, 'msg': '查询结果失败'})
    print(status_dict)

    log_content=scriptfun.get_job_result(hostobj.biz_id,job_id)
    data=[]
    for filename,filesize in eval(log_content):
        data.append({"filename":filename,"filesize":filesize})
    print(data)
    return JsonResponse({'code': 200, 'msg': 'success', 'data': data})

def show_logs(request):
    hid = request.GET.get('hid', '')
    app_code = request.GET.get('app_code', '')
    logs_name = request.GET.get('logs_name', '')
    print(hid,app_code,logs_name)

    hostobj = Hosts.objects.get(pk=hid)

    script = Scripts.objects.get(pk=2)
    # 执行查询脚本
    job_id = scriptfun.excute_script(hostobj.hostip, hostobj.biz_id, script.scriptcontent.format(app_code,logs_name))
    if not job_id:
        return JsonResponse({'code': 502, 'msg': '执行失败'})

    status_dict = scriptfun.get_job_status(hostobj.biz_id, job_id)
    if not status_dict:
        return JsonResponse({'code': 502, 'msg': '查询结果失败'})
    print(status_dict)

    log_content=scriptfun.get_job_result(hostobj.biz_id,job_id)
    print(log_content)
    return JsonResponse({'code': 200, 'msg': 'success','content_list':eval(log_content)})

def search_database(request):
    return JsonResponse({'code': 200, 'msg': 'success',})