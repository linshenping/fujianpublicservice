# -*- coding: utf-8 -*-
import requests
import urllib3
import json
import unittest
import os
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

class XiamenPublicServiceTest(unittest.TestCase):

    def setUp(self):
        print '##########厦门公共服务接口测试############'
        self.url = "https://open.fjylbz.gov.cn/api/gafe/rest?zyregion=350200"
        self.url_area = 'https://ylbz.ixm.gov.cn/xmyb/api/gafe/rest'


    def test_personal_information(self):
        print '##########个人基本信息用例执行############'
        date = {
            "funid": "N07.08.03.03",
            "data": {
                "idcard": "350603199510110019",
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        # datas = json.loads(r.text.encode('utf-8')).get('data')
        # print('datas{0}:'.format(datas))
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_personal_information_idcard_null(self):
        print '##########个人基本信息 - 身份证数据为空 用例执行############'
        date = {
            "funid": "N07.08.03.03",
            "data": {
                "idcard": "",
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        cause = json.loads(r.text).get('cause')
        print 'cause:{0}'.format(cause)
        self.assertEqual(flags, u'100509')
        self.assertEqual(r.status_code, 200)

    def test_personal_information_idcard_error(self):
        print '##########个人基本信息 - 身份证数据不存在 用例执行############'
        date = {
            "funid": "N07.08.03.03",
            "data": {
                "idcard": "12334455",
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        cause = json.loads(r.text).get('cause')
        print 'cause:{0}'.format(cause)
        self.assertEqual(flags, u'100517')
        self.assertEqual(r.status_code, 200)

    def test_insurance_information(self):
        print '##########参保信息用例执行############'
        date = {
            "funid": "N07.08.03.01",
            "data": {
                "idcard": "350603199510110019",
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_insurance_information_idcard_null(self):
        print '##########参保信息，身份证号为空用例执行############'
        date = {
            "funid": "N07.08.03.01",
            "data": {
                "idcard": " ",
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        cause = json.loads(r.text).get('cause')
        print 'cause: {0}'.format(cause)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'100509')
        self.assertIn(cause, '身份证不能为空')
        self.assertEqual(r.status_code, 200)

    def test_insurance_information_idcard_error(self):
        print '##########参保信息，身份证号是错误的用例执行############'
        date = {
            "funid": "N07.08.03.01",
            "data": {
                "idcard": "12346788",
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        cause = json.loads(r.text).get('cause')
        print 'cause: {0}'.format(cause)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'100531')
        self.assertIn(cause, '您没有在厦门参加医保保险或没有停保')
        self.assertEqual(r.status_code, 200)


    def test_get_insurance_information(self):
        print '##########获取参保号用例执行############'
        date = {
            "funid": "N07.08.03.02",
            "data": {
                "idcard": "350603199510110019"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        data = json.loads(r.text.encode('utf-8')).get('data')
        print 'data: {0}'.format(data)
        id0000 = data['id0000']
        print '保险号: {}'.format(id0000)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertIsNotNone(id0000)
        self.assertEqual(r.status_code, 200)

    def test_get_insurance_information_idcard_null(self):
        print '##########获取参保号,身份证号为空用例执行############'
        date = {
            "funid": "N07.08.03.02",
            "data": {
                "idcard": ""
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        data = json.loads(r.text.encode('utf-8')).get('data')
        print(r.status_code, r.reason)
        cause = json.loads(r.text).get('cause')
        print 'cause: {0}'.format(cause)
        self.assertEqual(flags, u'100509')
        self.assertIn(cause, '身份证不能为空')
        self.assertEqual(r.status_code, 200)

    def test_get_insurance_information_idcard_error(self):
        print '##########获取参保号，身份证号错误用例执行############'
        date = {
            "funid": "N07.08.03.02",
            "data": {
                "idcard": "1234567"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        data = json.loads(r.text.encode('utf-8')).get('data')
        print(r.status_code, r.reason)
        cause = json.loads(r.text).get('cause')
        print 'cause: {0}'.format(cause)
        self.assertEqual(flags, u'100531')
        self.assertIn(cause, '您没有在厦门参加医保保险或没有停保')
        self.assertEqual(r.status_code, 200)

    def test_payment_information(self):
        print '##########缴费查询用例执行############'
        date = {
            "funid": "N07.08.04.01",
            "data": {
                "start_time": "201801",
                "end_time": "201909",
                "page": "1",
                "rows": "50",
                "idcard": "350603199510110019"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        data = json.loads(r.text).get('data')
        print 'data:{0}'.format(data)
        total = data['total']
        rows = data['rows']
        print 'rows长度: {0}'.format(len(rows))
        print 'total:{0}'.format(total)
        self.assertEqual(flags, u'1')
        self.assertEqual(total, len(rows))
        self.assertEqual(r.status_code, 200)

    def test_consume_information(self):
        print '##########消费查询用例执行############'
        date = {
            "funid": "N07.08.05.01",
            "data": {
                "consultation_type": "",
                "start_time": "201701",
                "end_time": "201909",
                "page": "1",
                "rows": "50",
                "idcard": "350823199311161020"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_list_fees(self):
        print '##########费用清单用例执行############'
        date = {
            "funid": "N07.08.05.02",
            "data": {
                "consultation_type": "0",
                "serial_no": "000297495855    "
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_billing_details(self):
        print '##########结算明细用例执行############'
        date = {
            "funid": "N07.08.05.03",
            "data": {
                "consultation_type": "0",
                "serial_no": "000297495855    "
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_rank_number_query(self):
        print '##########公共查询 - 等级编号查询 用例执行############'
        date = {
            "funid": "N07.08.09.08",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_fixed_point_organization_information(self):
        print '##########定点机构查询 - 等级查询 用例执行############'
        date = {
            "funid": "N07.08.09.01",
            "data": {
                "wdjbbh": "02"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########定点机构查询 - 等级查询 - 详细查询 用例执行############'
        date_01 = {
                "funid": "N07.08.09.01",
                "data": {
                    "wdjbbh": "02",
                    "fwwdmc": "厦门弘爱医院"
                        }
                  }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

        print '##########定点机构查询 - 等级查询 - 模糊查询 用例执行############'
        date_02 = {
                "funid": "N07.08.09.01",
                "data": {
                    "wdjbbh": "02",
                    "fwwdmc": "弘爱"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_02 = requests.post(url=self.url, json=date_02, headers=headers)
        print r_02.text
        flags_02 = json.loads(r_02.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_02.status_code, r_02.reason)
        self.assertEqual(flags_02, u'1')
        self.assertEqual(r_02.status_code, 200)

    def test_fixed_point_drugstore(self):
        print '##########定点药店查询 用例执行############'
        date = {
            "funid": "N07.08.09.02",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########定点药店查询 - 精确查询 用例执行############'
        date_01 = {
            "funid": "N07.08.09.02",
            "data": {
                "fwwdmc": "福建国大药房连锁有限公司厦门湖里店"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

        print '##########定点药店查询 - 模糊查询 用例执行############'
        date_02 = {
                "funid": "N07.08.09.02",
                "data": {
                    "fwwdmc": "国大"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_02 = requests.post(url=self.url, json=date_02, headers=headers)
        print r_02.text
        flags_02 = json.loads(r_02.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_02.status_code, r_02.reason)
        self.assertEqual(flags_02, u'1')
        self.assertEqual(r_02.status_code, 200)

    def test_provincial_network_information(self):
        print '##########全省联网机构查询用例执行############'
        date = {
            "funid": "N07.08.09.03",
            "data": {
                "wdjbbh": "01"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_drug_and_medical_information(self):
        print '##########药品和诊疗项目查询用例执行############'
        date = {
            "funid": "N07.08.09.06",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_medical_examination_agency_information(self):
        print '##########体检定点机构查询用例执行############'
        date = {
            "funid": "N07.08.09.04",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########体检定点机构查询 - 精确查询 用例执行############'
        date_01 = {
                "funid": "N07.08.09.04",
                "data": {
                    "tjddbz": "02",
                    "fwwdmc": "厦门市同安区新民卫生院"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url_area, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

    def test_drug_system_and_zero_point_medical_information(self):
        print '##########执行基本药物制度及零差价定点医疗机构用例执行############'
        date = {
            "funid": "N07.08.09.05",
            "data": {
                "page": "1",
                "rows": "50"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)


class QuanzhouPublicServiceTest(unittest.TestCase):

    def setUp(self):
        print '##########泉州公共服务接口测试############'
        self.url = "https://open.fjylbz.gov.cn/api/gafe/rest?zyregion=350500"
        self.url_area = "http://qzyb.quanzhou.gov.cn/api/gafe/rest"
        self.url_ip = "http://172.23.1.96/api/gafe/rest"
    def test_personal_information(self):
        print '##########个人基本信息用例执行############'
        date = {
            "funid": "N07.08.03.03",
            "data": {
                "ybid": "2898110"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        # datas = json.loads(r.text.encode('utf-8')).get('data')
        # print('datas{0}:'.format(datas))
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)


    def test_insurance_information(self):
        print '##########参保信息用例执行############'
        date = {
            "funid": "N07.08.03.01",
            "data": {
                "ybid": "2898110"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_get_insurance_information(self):
        print '##########获取参保号用例执行############'
        date = {
            "funid": "N07.08.03.02",
            "data": {
                "id_card": "350500197101304564",
                "name": "杨红梅",
                "cardno": "CB7239433"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_ip, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)


    def test_payment_information(self):
        print '##########缴费查询用例执行############'
        date = {
            "funid": "N07.08.04.01",
            "data": {
                "start_time": "201801",
                "end_time": "201909",
                "page": "1",
                "rows": "50",
                "ybid": "2898110"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_consume_information(self):
        print '##########消费查询用例执行############'
        date = {
            "funid": "N07.08.05.01",
            "data": {
                "consultation_type": "",
                "start_time": "201701",
                "end_time": "201909",
                "page": "1",
                "rows": "50",
                "ybid": "2898110"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_list_fees(self):
        print '##########费用清单用例执行############'
        date = {
            "funid": "N07.08.05.02",
            "data": {
                "consultation_type": "2",
                "serial_no": "258383751"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_billing_details(self):
        print '##########结算明细用例执行############'
        date = {
            "funid": "N07.08.05.03",
            "data": {
                "consultation_type": "2",
                "serial_no": "258383751"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_rank_number_query(self):
        print '##########公共查询 - 等级编号查询 用例执行############'
        date = {
            "funid": "N07.08.09.08",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_fixed_point_organization_information(self):
        print '##########定点机构查询 - 等级查询 用例执行############'
        date = {
            "funid": "N07.08.09.01",
            "data": {
                "wdjbbh": "02"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########定点机构查询 - 等级查询 - 详细查询 用例执行############'
        date_01 = {
                "funid": "N07.08.09.01",
                "data": {
                    "wdjbbh": "02",
                    "fwwdmc": "泉州洛江万鸿医院"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

        print '##########定点机构查询 - 等级查询 - 模糊查询 用例执行############'
        date_02 = {
                "funid": "N07.08.09.01",
                "data": {
                    "wdjbbh": "02",
                    "fwwdmc": "洛江"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_02 = requests.post(url=self.url, json=date_02, headers=headers)
        print r_02.text
        flags_02 = json.loads(r_02.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_02.status_code, r_02.reason)
        self.assertEqual(flags_02, u'1')
        self.assertEqual(r_02.status_code, 200)

    def test_fixed_point_drugstore(self):
        print '##########定点药店查询 用例执行############'
        date = {
            "funid": "N07.08.09.02",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########定点药店查询 - 精确查询 用例执行############'
        date_01 = {
                "funid": "N07.08.09.02",
                "data": {
                    "fwwdmc": "福建省燕煌医药连锁有限公司阳山分店"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

        print '##########定点药店查询 - 模糊查询 用例执行############'
        date_02 = {
                "funid": "N07.08.09.02",
                "data": {
                    "fwwdmc": "燕煌医药"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_02 = requests.post(url=self.url, json=date_02, headers=headers)
        print r_02.text
        flags_02 = json.loads(r_02.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_02.status_code, r_02.reason)
        self.assertEqual(flags_02, u'1')
        self.assertEqual(r_02.status_code, 200)

    def test_drug_and_medical_information(self):
        print '##########药品和诊疗项目查询用例执行############'
        date = {
            "funid": "N07.08.09.06",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

class FuzhouPublicServiceTest(unittest.TestCase):

    def setUp(self):
        print '##########福州公共服务接口测试############'
        self.url = "https://open.fjylbz.gov.cn/api/gafe/rest?zyregion=350100"
        self.url_area = "http://wx3.fzybzx.com.cn/fzyb/api/gafe/rest"

    def test_personal_information(self):
        print '##########个人基本信息用例执行############'
        date = {
            "funid": "N07.08.03.03",
            "data": {
                "ybid": "15163103"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        # datas = json.loads(r.text.encode('utf-8')).get('data')
        # print('datas{0}:'.format(datas))
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)


    def test_insurance_information(self):
        print '##########参保信息用例执行############'
        date = {
            "funid": "N07.08.03.01",
            "data": {
                "ybid": "15163103"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_get_insurance_information(self):
        print '##########获取参保号用例执行############'
        date = {
            "funid": "N07.08.03.02",
            "data": {
                "id_card": "350102196105110827",
                "name": "吴素平",
                "cardno": "A99943596"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)


    def test_payment_information(self):
        print '##########缴费查询用例执行############'
        date = {
            "funid": "N07.08.04.01",
            "data": {
                "start_time": "201801",
                "end_time": "201909",
                "page": "1",
                "rows": "50",
                "ybid": "15163103"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_consume_information(self):
        print '##########消费查询用例执行############'
        date = {
            "funid": "N07.08.05.01",
            "data": {
                "consultation_type": "",
                "start_time": "201701",
                "end_time": "201909",
                "page": "1",
                "rows": "50",
                "ybid": "15163103"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_list_fees(self):
        print '##########费用清单用例执行############'
        date = {
            "funid": "N07.08.05.02",
            "data": {
                "consultation_type": "0",
                "serial_no": "10080944891"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_billing_details(self):
        print '##########结算明细用例执行############'
        date = {
            "funid": "N07.08.05.03",
            "data": {
                "consultation_type": "0",
                "serial_no": "10080944891"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_rank_number_query(self):
        print '##########公共查询 - 等级编号查询 用例执行############'
        date = {
            "funid": "N07.08.09.08",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_fixed_point_organization_information(self):
        print '##########定点机构查询 - 等级查询 用例执行############'
        date = {
            "funid": "N07.08.09.01",
            "data": {
                "wdjbbh": "01"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########定点机构查询 - 等级查询 - 详细查询 用例执行############'
        date_01 = {
                "funid": "N07.08.09.01",
                "data": {
                    "wdjbbh": "01",
                    "fwwdmc": "福清红卫门诊部"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

        print '##########定点机构查询 - 等级查询 - 模糊查询 用例执行############'
        date_02 = {
                "funid": "N07.08.09.01",
                "data": {
                    "wdjbbh": "01",
                    "fwwdmc": "福清红"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_02 = requests.post(url=self.url, json=date_02, headers=headers)
        print r_02.text
        flags_02 = json.loads(r_02.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_02.status_code, r_02.reason)
        self.assertEqual(flags_02, u'1')
        self.assertEqual(r_02.status_code, 200)

    def test_fixed_point_drugstore(self):
        print '##########定点药店查询 用例执行############'
        date = {
            "funid": "N07.08.09.02",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########定点药店查询 - 精确查询 用例执行############'
        date_01 = {
                "funid": "N07.08.09.02",
                "data": {
                    "fwwdmc": "福建康佰家大药房连锁一一一店"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

        print '##########定点药店查询 - 模糊查询 用例执行############'
        date_02 = {
                "funid": "N07.08.09.02",
                "data": {
                    "fwwdmc": "康佰家"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_02 = requests.post(url=self.url, json=date_02, headers=headers)
        print r_02.text
        flags_02 = json.loads(r_02.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_02.status_code, r_02.reason)
        self.assertEqual(flags_02, u'1')
        self.assertEqual(r_02.status_code, 200)

    def test_drug_and_medical_information(self):
        print '##########药品和诊疗项目查询用例执行############'
        date = {
            "funid": "N07.08.09.06",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)


class NingdePublicServiceTest(unittest.TestCase):

    def setUp(self):
        print '##########宁德公共服务接口测试############'
        self.url = "https://open.fjylbz.gov.cn/api/gafe/rest?zyregion=350900"
        self.url_area = "http://wx.ybj.ningde.gov.cn:7777/api/gafe/rest"

    def test_personal_information(self):
        print '##########个人基本信息用例执行############'
        date = {
            "funid": "N07.08.03.03",
            "data": {
                "ybid": "35222119651012003X "
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        # datas = json.loads(r.text.encode('utf-8')).get('data')
        # print('datas{0}:'.format(datas))
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)


    def test_insurance_information(self):
        print '##########参保信息用例执行############'
        date = {
            "funid": "N07.08.03.01",
            "data": {
                "ybid": "35222119651012003X "
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_get_insurance_information(self):
        print '##########获取参保号用例执行############'
        date = {
            "funid": "N07.08.03.02",
            "data": {
                "id_card": "35222119651012003X",
                "name": "毛瑾琳",
                "cardno": "J01916107"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)


    def test_payment_information(self):
        print '##########缴费查询用例执行############'
        date = {
            "funid": "N07.08.04.01",
            "data": {
                "start_time": "201801",
                "end_time": "201909",
                "page": "1",
                "rows": "50",
                "ybid": "35222119651012003X "
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_consume_information(self):
        print '##########消费查询用例执行############'
        date = {
            "funid": "N07.08.05.01",
            "data": {
                "consultation_type": "",
                "start_time": "201701",
                "end_time": "201909",
                "page": "1",
                "rows": "50",
                "ybid": "35222119651012003X "
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_list_fees(self):
        print '##########费用清单用例执行############'
        date = {
            "funid": "N07.08.05.02",
            "data": {
                "consultation_type": "2",
                "serial_no": "68413547        "
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_billing_details(self):
        print '##########结算明细用例执行############'
        date = {
            "funid": "N07.08.05.03",
            "data": {
                "consultation_type": "2",
                "serial_no": "68413547        "
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_rank_number_query(self):
        print '##########公共查询 - 等级编号查询 用例执行############'
        date = {
            "funid": "N07.08.09.08",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

    def test_fixed_point_organization_information(self):
        print '##########定点机构查询 - 等级查询 用例执行############'
        date = {
            "funid": "N07.08.09.01",
            "data": {
                "wdjbbh": "05"
                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########定点机构查询 - 等级查询 - 详细查询 用例执行############'
        date_01 = {
                "funid": "N07.08.09.01",
                "data": {
                    "wdjbbh": "05",
                    "fwwdmc": "宁德市中医院"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

        print '##########定点机构查询 - 等级查询 - 模糊查询 用例执行############'
        date_02 = {
                "funid": "N07.08.09.01",
                "data": {
                    "wdjbbh": "01",
                    "fwwdmc": "中医院"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_02 = requests.post(url=self.url, json=date_02, headers=headers)
        print r_02.text
        flags_02 = json.loads(r_02.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_02.status_code, r_02.reason)
        self.assertEqual(flags_02, u'1')
        self.assertEqual(r_02.status_code, 200)

    def test_fixed_point_drugstore(self):
        print '##########定点药店查询 用例执行############'
        date = {
            "funid": "N07.08.09.02",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

        print '##########定点药店查询 - 精确查询 用例执行############'
        date_01 = {
                "funid": "N07.08.09.02",
                "data": {
                    "fwwdmc": "福建康佰家大药房连锁有限公司宁德市八一五店"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_01 = requests.post(url=self.url, json=date_01, headers=headers)
        print r_01.text
        flags_01 = json.loads(r_01.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_01.status_code, r_01.reason)
        self.assertEqual(flags_01, u'1')
        self.assertEqual(r_01.status_code, 200)

        print '##########定点药店查询 - 模糊查询 用例执行############'
        date_02 = {
                "funid": "N07.08.09.02",
                "data": {
                    "fwwdmc": "康佰家"
                        }
                    }
        headers = {"Content-Type": "application/json"}
        r_02 = requests.post(url=self.url, json=date_02, headers=headers)
        print r_02.text
        flags_02 = json.loads(r_02.text).get('flag')
        print 'flags_01:{0}'.format(flags)
        print(r_02.status_code, r_02.reason)
        self.assertEqual(flags_02, u'1')
        self.assertEqual(r_02.status_code, 200)

    def test_drug_and_medical_information(self):
        print '##########药品和诊疗项目查询用例执行############'
        date = {
            "funid": "N07.08.09.06",
            "data": {

                    }
                }
        headers = {"Content-Type": "application/json"}
        r = requests.post(url=self.url_area, json=date, headers=headers)
        print r.text
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        print(r.status_code, r.reason)
        self.assertEqual(flags, u'1')
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()


