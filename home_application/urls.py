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

from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.home),
    url(r'^dev-guide/$', views.dev_guide),
    url(r'^contact/$', views.contact),
    url(r'^app_logs/$', views.app_logs),
    url(r'^search_logs/$', views.search_logs),
    url(r'^script_result/$', views.logs_result),
    url(r'^log_content_result/$', views.log_content_result),
    url(r'^host/$', views.host_view),
    url(r'^saas_app/$', views.saas_app),
    url(r'^show_logs/$', views.show_logs),
    url(r'^app_database/$', views.app_database),
    url(r'^search_database/$', views.search_database),
    url(r'^script_callback/$', views.script_callback_view),
)
