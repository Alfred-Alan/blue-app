from celery import task
from django.http import JsonResponse

from home_application.logic import scriptfun


@task
def async_get_job_status(biz_id, job_instance_id):
    status_dict=scriptfun.get_job_status(biz_id, job_instance_id)
    if not status_dict:
        return JsonResponse({'code': 502, 'msg': '查询结果失败'})
    print(status_dict)
    return status_dict
