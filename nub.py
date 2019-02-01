# -*- coding: utf-8 -*-
#声明身高变量
height = 1.75
#声明体重变量
weight = 80.5
#bmi指数变量
bmi = weight/height**2
#打印bmi结果
print(bmi)
#bmi的各种变量情况
if bmi < 18.5: 
   print('低于18.5：过轻')
#低于18.5的情况
if 18.5<bmi<25:
   print('18.5<bmi<25:正常')
#bmi正常范围
if 25<bmi<28:
   print('25<bmi<28:过重')
#bmi显示过重
if 28<bmi<32:
   print('28<bmi<32:肥胖')
#bmi显示肥胖
if bmi > 32:
   print('bmi>32:严重肥胖')
#bmi严重肥胖
