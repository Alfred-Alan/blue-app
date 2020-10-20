import base64
import time

from blueking.component.shortcuts import get_client_by_user
import logging

client = get_client_by_user('liujiqing')
logger = logging.getLogger(__name__)

bk_app_code = 'blue-app'
bk_app_secret = '837d12fb-a738-4c04-9f61-c724fb2dddd8'
bk_token = '9q4LSDNHUkeNJmo53Lr-uCsJlGtHlgaSwGSP2QqgCuE'

class script_obj:
    # 执行脚本
    def excute_script(self,hostip, biz_id, scriptcontent):

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
            'bk_callback_url':"http://dev.paas.guodong.com:8086/script_callback/",
        }
        excute_data = client.job.fast_execute_script(kwargs)
        if excute_data.get('result', False):
            return excute_data['data']['job_instance_id']
        else:
            logger.error(u'执行任务失败：%s' % excute_data.get('message'))
            return False

    # 查询执行状态
    def get_job_status(self,biz_id, job_instance_id):
        kwargs = {
            'bk_app_code': bk_app_code,
            'bk_app_secret': bk_app_secret,
            'bk_token': bk_token,
            'bk_biz_id': biz_id,
            'job_instance_id': job_instance_id
        }
        tag = True  # 开关
        num = 0  # 计数
        while True:
            excute_status = client.job.get_job_instance_status(kwargs)
            if excute_status.get('result', False):
                stauts = excute_status['data']['job_instance']['status']
                if int(stauts) == 2:  # 执行未成功
                    time.sleep(1)
                else:
                    tag = True
                    break
            else:
                logger.error(u'request filied')
                num += 1
                if num > 5:
                    tag = False
                    break
                time.sleep(1)

        if tag:
            step_instances = {}
            for step_item in excute_status['data']['blocks'][0]['step_instances']:
                step_instances['step_instance_id'] = step_item['step_instance_id']
                step_instances['status'] = step_item['status']
            return {'status': excute_status['data']['job_instance']['status'],
                    'step_instances': step_instances}
        else:
            logger.error(u'查询执行状态失败：%s' % excute_status.get('message'))
            return False

    # 查询执行结果
    def get_job_result(self,biz_id, job_instance_id):
        kwargs = {
            'bk_app_code': bk_app_code,
            'bk_app_secret': bk_app_secret,
            'bk_token': bk_token,
            'bk_biz_id': biz_id,
            'job_instance_id': job_instance_id,
        }
        result = client.job.get_job_instance_log(kwargs)
        # print(result)
        if result.get('result', False):
            return result['data'][0]['step_results'][0]['ip_logs'][0]['log_content']
        else:
            logger.error(u'执行任务失败：%s' % result.get('message'))
            return False

scriptfun = script_obj()

