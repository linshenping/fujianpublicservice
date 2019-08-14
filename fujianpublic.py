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

'''
class GetIxmApiCrossProvinceTest(unittest.TestCase):

    def setUp(self):

        self.url = "https://ylbz.ixm.gov.cn/xmyb/api/gafe/rest"

    # 获取access_token
    def test_get_access_token(self):
        print '#########获取access_token用例执行############'
        # 入参
        date = {
            "funid": "N03.00.05.11",
            "data": {
                "app_type": "0",
                "appid": "xmggfw"
            },
             "appid": "xmggfw"
        }
        r = requests.post(url=self.url, json=date)
        print r.text
        datas = json.loads(r.text.encode('utf-8')).get('data')
        print('datas{0}:'.format(datas))
        access_token = datas.get('access_token')
        print 'access_token:{0}'.format(access_token)
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        expires_time = datas.get('expires_in')
        print 'expires_time:{0}'.format(expires_time)
        refresh_token = datas.get('refresh_token')
        print 'refresh_token:{0}'.format(refresh_token)
        self.assertEqual(flags, u'1')

    # 获取参保人信息jiekou
    def test_get_insured_information(self):
        print '##########获取参保人信息用例执行############'
        #获取accsess_token
        date_token = {
            "funid": "N03.00.05.11",
            "data": {
            "app_type": "0",
            "appid": "xmggfw"
                    },
            "appid": "xmggfw"
                }
        r = requests.post(url=self.url, json=date_token)
        access_token = r.json()['data']['access_token']
        print 'access_token:{0}'.format(access_token)

        #请求参保人信息
        date = {
            "funid": "N06.00.01.02",
            "data": {
                "access_token": access_token,
                "uid": "350823199311161020"
            },
            "access_token": access_token
        }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')
        
        
        # 机构信息查询
    def test_institutional_information_inquiry(self):
        print '##########机构信息查询用例执行############'
        date = {
            "funid": "N07.03.00.21",
            "data": {
            "aab299": "210600"
            }
            }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 跨省异地备案列表查询(机构)
    def test_inter_provincial_record_mechanism_list(self):
        print '##########跨省异地备案列表查询（机构）用例执行############'
        date = {
            "funid": "N07.03.00.16",
            "data": {
            "social_credit_code": "91350200MA31GUTX75",
            "page": "1",
            "rows": "10"
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')


    # 跨省异地备案申请
    def test_inter_provincial_filing_application(self):
        print '########跨省异地备案申请用例执行############'
        date = {
            "funid": "N07.03.00.17",
            "data": {
            "uid":"350603199510110019",
            "record_type":"2",
            "record_city":"210600",
            "effect_date":"2019-08-05",
            "contact_person":"林小延",
            "contact_phone":"18650347652",
            "contact_addr":"快乐快乐",
            "hospitals":"丹东市公安医院",
            "medicals":"国大药房",
            "org_codes":"2106001000002",
            "apply_channel":"01"
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 2.4.1	跨省异地备案列表查询(个人)
    def test_inter_provincial_record_personal_list(self):
        print '##############跨省异地备案列表查询(个人)用例执行##############'
        date = {
            "funid": "N07.03.00.16",
            "data": {
                "uid": "350603199510110019",
                "page": "1",
                "rows": "10"
            }
        }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        id = r.json()['data']['rows'][0]['id']
        print 'id是: {0}'.format(id)
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')


    # 跨省异地备案撤销
    def test_inter_provincial_filing_cancel(self):
        print '##########跨省异地备案撤销用例执行############'
        # 查询最新的id是多少
        date_id = {
            "funid": "N07.03.00.16",
            "data": {
                "uid": "350603199510110019",
                "page": "1",
                "rows": "10"
            }
        }
        r = requests.post(url=self.url, json=date_id)
        id = r.json()['data']['rows'][0]['id']
        print 'id是: {0}'.format(id)

        #  api请求
        date = {
            "funid": "N07.03.00.18",
            "data": {
            "id": id
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')


    # 跨省异地备案截止（数据目前没办法构造）
    def test_inter_provincial_filing_cutoff(self):
        print '##########跨省异地备案截止用例执行############'
        date = {
            "funid": "N07.03.00.19",
            "data": {
            "id": "194190"
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')


    # 跨省异地备案前置校验
    def test_inter_provincial_filing_check(self):
        print '##########跨省异地备案前置校验用例执行############'
        date = {
            "funid": "N07.03.00.20",
            "data": {
            "uid": "350603199510110019"
			}
		}
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 模糊查找本单位人员姓名jiekou
    def test_fuzzy_search(self):
        print '##########模糊查找本单位人员姓名用例执行############'
        date = {
        "funid": "N07.03.00.23",
        "data": {
            "social_credit_code": "91350200MA31GUTX75",
            "name": "王"
                }
                }

        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

class GetIxmApiFixOrganizationTest(unittest.TestCase):

    def setUp(self):
            self.url = "https://ylbz.ixm.gov.cn/xmyb/api/gafe/rest"

    # 查询定点机构信息
    def test_query_fixed_point_organization_informationh(self):
        print '##########查询定点机构信息用例执行############'
        date = {
        "funid": "N07.07.00.01",
        "data": {
            "social_credit_code": "913502030511743851",
            "batch": ""
                }
            }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 定点机构信息新增
    def test_query_fixed_point_organization_new(self):
        print '##########定点机构信息新增用例执行############'
        date = {
            "funid": "N07.07.00.02",
            "data": {
                "apply_type": "01",
                "org_id": "*",
                "org_name": "TEST-linsp厦门最美信息科技有限公司",
                "network_area": "350203",
                "network_addr": "厦门市思明区海翼大厦厦禾路666",
                "key_project": "0",
                "key_project_file_no": "",
                "key_project_file_name": "",
                "contacts": "linsp-test",
                "contacts_certificate_type": "10",
                "contacts_certificate_no": "1234567890",
                "contacts_phone": "22222222222",
                "org_grade": "9",
                "org_type": "51",
                "ownership": "0",
                "operate_nature": "01",
                "license_key": "222222",
                "license_key_begin_date": "20190318",
                "certificate_no": "334343",
                "certificate_no_begin_date": "20190322",
                "social_credit_code": "913502030511743851",
                "business_license": "*",
                "is_org": "0",
                "one_apply_date": "",
                "one_apply_addr": "",
                "second_apply_date": "",
                "second_apply_adddr": "",
                "legal_person": "1",
                "legal_person_certificate_type": "10",
                "legal_person_certificate_no": "2222",
                "legal_person_phone": "23232323",
                "area": "100",
                "actual_area": "100",
                "building_begin_date": "201901",
                "building_end_date": "201907",
                "range": "厦门禹州大学城",
                "main_range": "口腔",
                "bed_num": "2",
                "is_punish": "0",
                "punish_office": "",
                "punish_date": "",
                "is_accident": "0",
                "doctor_num": "5",
                "senior_num": "1",
                "intermediate_num": "2",
                "technician_num": "1",
                "charge_num": "1",
                "apply_channel": "02",
                "street": "厦禾路666",
                "manage_begin_date": "20190128",
                "longitude": "118.23122",
                "latitude": "24.64738"

                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 定点机构信息修改
    def test_query_fixed_point_organization_update(self):
        print '##########定点机构信息修改用例执行############'
        # 查询获取serial_no和batch参数
        date_serial = {
            "funid": "N07.07.00.01",
            "data": {
                "social_credit_code": "913502030511743851",
                "batch": ""
            }
        }
        r = requests.post(url=self.url, json=date_serial)
        serial_no = r.json()['data'][0]['serial_no']
        print ('serial_no: {0}').format(serial_no)
        batch = r.json()['data'][0]['batch']
        print ('serial_no: {0}').format(batch)
        # api请求
        date = {
            "funid": "N07.07.00.03",
            "data": {
                "serial_no": serial_no,
                "batch": batch,
                "apply_type": "01",
                "org_id": "*",
                "org_name": "TEST-厦门最美信息科技有限公司",
                "network_area": "350203",
                "network_addr": "厦门市思明区海翼大厦厦禾路666",
                "key_project": "0",
                "key_project_file_no": "",
                "key_project_file_name": "",
                "contacts": "linsp-test",
                "contacts_certificate_type": "10",
                "contacts_certificate_no": "1234567890",
                "contacts_phone": "22222222222",
                "org_grade": "9",
                "org_type": "51",
                "ownership": "0",
                "operate_nature": "01",
                "license_key": "222222",
                "license_key_begin_date": "20190318",
                "certificate_no": "334343",
                "certificate_no_begin_date": "20190322",
                "social_credit_code": "913502030511743851",
                "business_license": "*",
                "is_org": "0",
                "one_apply_date": "",
                "one_apply_addr": "",
                "second_apply_date": "",
                "second_apply_adddr": "",
                "legal_person": "1",
                "legal_person_certificate_type": "10",
                "legal_person_certificate_no": "2222",
                "legal_person_phone": "23232323",
                "area": "100",
                "actual_area": "100",
                "building_begin_date": "201901",
                "building_end_date": "201907",
                "range": "厦门禹州大学城",
                "main_range": "口腔",
                "bed_num": "2",
                "is_punish": "0",
                "punish_office": "",
                "punish_date": "",
                "is_accident": "0",
                "doctor_num": "5",
                "senior_num": "1",
                "intermediate_num": "2",
                "technician_num": "1",
                "charge_num": "1",
                "apply_channel": "02",
                "street": "厦禾路666",
                "manage_begin_date": "20190128",
                "longitude": "118.23122",
                "latitude": "24.64738"

                    }
                }

        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 机构定点申请数据撤销
    def test_query_fixed_point_organization_cancle(self):
        print '##########机构定点申请数据撤销用例执行############'
        # 查询获取serial_no参数
        date_serial = {
            "funid": "N07.07.00.01",
            "data": {
                "social_credit_code": "913502030511743851",
                "batch": ""
            }
        }
        r = requests.post(url=self.url, json=date_serial)
        serial_no = r.json()['data'][0]['serial_no']
        print ('serial_no: {0}').format(serial_no)
        # api请求
        date = {
            "funid": "N07.07.00.04",
            "data": {
                "serial_no": serial_no
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 机构定点申请医师信息维护
    def test_query_fixed_point_doctor_information_add(self):
        print '##########机构定点申请医师信息维护(新增)用例执行############'
        # 查询获取serial_no参数
        date_serial = {
            "funid": "N07.07.00.01",
            "data": {
                "social_credit_code": "913502030511743851",
                "batch": ""
            }
        }
        r = requests.post(url=self.url, json=date_serial)
        serial_no = r.json()['data'][0]['serial_no']
        print ('serial_no: {0}').format(serial_no)
        # api请求
        date = {
            "funid": "N07.07.00.05",
            "data": {
                "serial_no": serial_no,
                "type": "1",
                "doctor_list": {
                    "biz_serial_no": "",
                    "people_type": "01",
                    "certificate_grade": "01",
                    "name": "萍萍",
                    "certificate_type": "10",
                    "certificate_no": "123454545",
                    "vocational_qc_no": "7787788",
                    "technical_qc_no": "2222222",
                    "title_certificate_no": "44444444",
                    "title_certificate_authorities": "厦门",
                    "licensed_pharmacist_qc_no": ""
                                }
                    }
                }

        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 机构定点申请医师信息查询
    def test_query_fixed_point_doctor_information(self):
        print '##########机构定点申请医师信息查询用例执行############'
        # 查询获取serial_no参数
        date_serial = {
            "funid": "N07.07.00.01",
            "data": {
                "social_credit_code": "913502030511743851",
                "batch": ""
            }
        }
        r = requests.post(url=self.url, json=date_serial)
        serial_no = r.json()['data'][0]['serial_no']
        print ('serial_no: {0}').format(serial_no)
        # api请求
        date = {
            "funid": "N07.07.00.06",
            "data": {
                "serial_no": serial_no,
                "page": "1",
                "rows": "10"
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')
'''


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


    def test_insurance_information(self):
        print '##########参保信息用例执行############'
        date = {
            "funid": "N07.08.03.01",
            "data": {
                "idcard": "350603199510110019",
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
                "idcard": "350603199510110019"
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
                "idcard": "350603199510110019"
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


