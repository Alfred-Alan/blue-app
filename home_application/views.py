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

from django.shortcuts import render
from blueking.component.shortcuts import get_client_by_user
import logging

client = get_client_by_user('liujiqing')
logger = logging.getLogger(__name__)

bk_app_code = 'blue-app'
bk_app_secret = '837d12fb-a738-4c04-9f61-c724fb2dddd8'
bk_token = 'IC9pXaehI-E8hjSrciceMdRaXOAOUjQo-F9D8Vx5HUI'


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    kwargs = {
        'bk_app_code':bk_app_code,
        'bk_app_secret':bk_app_secret,
        'bk_token':bk_token,
    }
    data = client.bk_paas.get_app_info(kwargs)
    app_info=data['data']
    print(app_info)
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

def app_view(request):
    return render(request,'')