# -*- coding: utf-8 -*-
import threading

# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('关联的%s (in %s)')
