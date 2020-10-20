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

from django.db import models

# Create your models here.

class Scripts(models.Model):
    scriptname=models.CharField(max_length=50,verbose_name='脚本名称')
    scriptcontent=models.TextField(verbose_name='脚本内容')
    status_choice = [(1,'shell脚本'),(2,'bat脚本'),(3,'perl脚本'),(4,'python脚本'),(5,'Powershell脚本')]
    script_type = models.IntegerField(choices=status_choice,default=1,verbose_name='脚本类型')

    def __str__(self):
        return self.scriptname

    class Meta:
        db_table = "Scripts"
        verbose_name = "脚本表"
        verbose_name_plural = verbose_name

class Hosts(models.Model):
    hostname=models.CharField(max_length=50,verbose_name='主机名称')
    hostip=models.CharField(max_length=50,verbose_name='主机IP')
    biz_id=models.CharField(max_length=50,default=2,verbose_name='业务id')


    def __str__(self):
        return self.hostname

    class Meta:
        db_table = "Hosts"
        verbose_name = "主机表"
        verbose_name_plural = verbose_name

class Apps(models.Model):
    bk_app_code=models.CharField(max_length=200,verbose_name='app_code')
    bk_app_name=models.CharField(max_length=200,verbose_name='app_name')
    introduction=models.CharField(max_length=200,verbose_name='应用介绍')
    creator=models.CharField(max_length=200,verbose_name='创建者')
    developer=models.CharField(max_length=200,verbose_name='开发人员')
    server = models.IntegerField(verbose_name='隶属服务器')

    def __str__(self):
        return self.bk_app_code

    class Meta:
        db_table = "Apps"
        verbose_name = "应用表"
        verbose_name_plural = verbose_name


class Doinfo(models.Model):
    businessname=models.CharField(max_length=50,verbose_name='业务',null=True,blank=True)
    username = models.CharField(max_length=20,verbose_name='用户',null=True,blank=True)
    script = models.ForeignKey(Scripts,models.CASCADE,verbose_name='脚本名称')
    createtime = models.DateTimeField(verbose_name='创建时间')
    starttime = models.DateTimeField(verbose_name='开始执行时间')
    endtime = models.DateTimeField(verbose_name='执行结束时间',null=True,blank=True)
    ipcount = models.IntegerField(verbose_name='执行数量')
    details = models.CharField(max_length=200,verbose_name='详细',null=True,blank=True)
    jobid= models.IntegerField(verbose_name='jobid')
    status_choice = [(1,'未执行'),(2,'正在执行'),(3,'执行成功'),(4,'执行失败')]
    status = models.IntegerField(choices=status_choice,verbose_name='执行状态',default=2)
    log = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.businessname+ self.script.scriptname
    class Meta:
        ordering=['-id']

    def to_dirct(self,biz_map =None):
        if biz_map is None:
            biz_map={}
        return {
            'id':self.id,
            'username':self.username,
            'starttime':self.starttime.strftime('%Y-%m-%d %H:%M:%S'),
            'businessname':biz_map.get(self.businessname,self.businessname),
            'script':self.script.scriptname,
            'scriptcontent':self.script.scriptcontent,
            'ipcount':self.ipcount,
            'jobid':self.jobid,
            'status':self.status,
        }