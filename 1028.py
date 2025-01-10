# -*- coding: utf-8 -*-
import time

from addEmployee import *
from read_data import *
import threading

def run_tests(user_list, index):

    for m in user_list:
        data1['login']['data']['userNumber'] = m
        data1['EntrantInfo']['data']['counselorNumber'] = m
        data1['ProcessOfGoAdmission']['data']['userNumber'] = m
        data2['login']['data']['userNumber'] = m
        data2['EntrantInfo']['data']['counselorNumber'] = m
        data2['ProcessOfGoAdmission']['data']['userNumber'] = m

        start_time = time.time()  # 记录开始时间
        # 这里写需要测试运行时间的代码
        for i in range(index):
            name = test_employee_entry().ready_('154')[0]
            # test_employee_entry().ready_('uat')
            entrantId = test_employee_entry().test_send_information()


            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Authorization': token,
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'http://172.16.91.154',
                'Referer': 'http://172.16.91.154/entryManagement/paddingEntry',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            }

            json_data = {
                'entrantId': entrantId,
                'employeeName': name,
                'lossDate': lossDate,
                'lossType': '4',
                'lossReason': '151121252212526',
            }

            response = requests.post(
                'http://172.16.91.154/new/oa_personnel/recruitmentLoss/updateEntrantToLoss',
                headers=headers,
                json=json_data,
                verify=False,
            )

        end_time = time.time()  # 记录结束时间
        run_time = end_time - start_time  # 计算运行时间（单位为秒）
        print("脚本运行时间：", round(run_time, 2), '秒')

def threaded_run(lists, list1, list2, list3):
    threads = []

    for l in lists:
        if l == list1:
            thread = threading.Thread(target=run_tests, args=(list1, 1))
            threads.append(thread)
            thread.start()

        if l == list2:
            thread = threading.Thread(target=run_tests, args=(list2, 2))
            threads.append(thread)
            thread.start()

        if l == list3:
            thread = threading.Thread(target=run_tests, args=(list3, 3))
            threads.append(thread)
            thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    lossDate='2024-11-10'
    uuu1=deal_data(columns_to_read1,d,e,f)
    list1 = uuu1[0]
    list2 = uuu1[1]
    list3 = uuu1[2]
    # print(list1)
    # print(list2)
    # print(list3)
    lists=[list1,list2,list3]
    print(lists)
    test_employee_entry().ready_('154')
    token=login()
    # 调用多线程执行函数
    threaded_run(lists, list1, list2, list3)








