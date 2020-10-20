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

# from django.test import TestCase

# Create your tests here.
# import os
# path='./'
# for filename in os.listdir(path):
#     filesize=os.path.getsize(path+filename)
#     print(filename,filesize,'byte')
#     if os.path.isfile(path+filename):
#         with open(path+filename,'r+',encoding='utf-8')as f:
#             print(f.read(filesize))

# a='a{}2'
# print(a.format('2'))
# b='/tmp/bkjob/stepInstanceId_192.py: line 1: ��N��M��^��N����\uf3b8�������^��ͽ�\n\x03�\n��M��N��ނ��������^��N��^��̈́뾹�����라�N�\uf3bc�\x1e��ނ랄�^�락�=�M��M��N��ބ\uf37c뮽�.��N��: File name too long\n'
# print(b.encode('utf-8'))
# c=b'/tmp/bkjob/stepInstanceId_192.py: line 1: \xef\xbf\xbd\xef\xbf\xbdN\xef\xbf\xbd\xef\xbf\xbdM\xef\xbf\xbd\xef\xbf\xbd^\xef\xbf\xbd\xef\xbf\xbdN\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\x8e\xb8\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd^\xef\xbf\xbd\xef\xbf\xbd\xcd\xbd\xef\xbf\xbd\n\x03\xef\xbf\xbd\n\xef\xbf\xbd\xef\xbf\xbdM\xef\xbf\xbd\xef\xbf\xbdN\xef\xbf\xbd\xef\xbf\xbd\xde\x82\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd^\xef\xbf\xbd\xef\xbf\xbdN\xef\xbf\xbd\xef\xbf\xbd^\xef\xbf\xbd\xef\xbf\xbd\xcd\x84\xeb\xbe\xb9\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xeb\x9d\xbc\xef\xbf\xbdN\xef\xbf\xbd\xef\x8e\xbc\xef\xbf\xbd\x1e\xef\xbf\xbd\xef\xbf\xbd\xde\x82\xeb\x9e\x84\xef\xbf\xbd^\xef\xbf\xbd\xeb\x9d\xbd\xef\xbf\xbd=\xef\xbf\xbdM\xef\xbf\xbd\xef\xbf\xbdM\xef\xbf\xbd\xef\xbf\xbdN\xef\xbf\xbd\xef\xbf\xbd\xde\x84\xef\x8d\xbc\xeb\xae\xbd\xef\xbf\xbd.\xef\xbf\xbd\xef\xbf\xbdN\xef\xbf\xbd\xef\xbf\xbd: File name too long\n'
# print(c.decode())

# import os
#
# path = '/data/bkee/paas_agent/apps/logs/'
# app_name = '{}'
# log_name='{}'
# if log_name not in os.listdir(path+app_name+'/'):
#     print('找不到该文件')
#     exit()
#
# filesize = os.path.getsize(path + app_name + '/' + log_name)
# with open(path + app_name + '/' + log_name,'r')as f:
#     print(f.readlines())
from blueking.component.shortcuts import get_client_by_user
import logging

client = get_client_by_user('liujiqing')
logger = logging.getLogger(__name__)

bk_app_code = 'blue-app'
bk_app_secret = '837d12fb-a738-4c04-9f61-c724fb2dddd8'
bk_token = '9q4LSDNHUkeNJmo53Lr-uCsJlGtHlgaSwGSP2QqgCuE'


def excute_script(hostip, biz_id, scriptcontent):
    objtest = base64.b64encode(scriptcontent.encode('utf-8'))
    kwargs = {
        'bk_token': bk_token,
        'bk_biz_id': biz_id,
        'script_content': str(objtest, 'utf-8'),
        'account': 'root',
        'script_type': 4,
        'ip_list': [{
            "bk_cloud_id": 0,
            "ip": hostip
        }],
        'bk_callback_url': "http://dev.paas.guodong.com:8086/script_callback/",
    }
    excute_data = client.job.fast_execute_script(kwargs)
    if excute_data.get('result', False):
        return excute_data['data']['job_instance_id']
    else:
        logger.error(u'执行任务失败：%s' % excute_data.get('message'))
        return False



excute_script(hostobj.hostip,hostobj.biz_id,'print(1)')

