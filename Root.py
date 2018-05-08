# -*-coding:utf-8-*-
#请写出一个二分法找方程根的通用函数，加到大家的软件包里去。能够处理单调递增和递减的情况。
#注：本程序仅适用于某区间内函数  单调递增  或  单调递减  或  二次函数  或  半个周期的 三角函数
#name: Huang Weihao
#date: 2018/5/8

import math
import numpy as np


def func(x):                       #半个周期内的三角函数 或二次函数
    return math.cos(x)-1

# def func(x):                       #单调递增函数
#     return math.exp(x)-3.4

# def func(x):                         #单调递减函数
#     return -x**2+3

def sym_(a,b,s):                     #二分法求方程的根
    k=0
    while(True):
        if func(a)*func(b)==0:       #当f(a)*f(b)=0
            if func(a)==0:
                return a
            else:
                return b
        else:
            m=(a+b)/2
            if abs(a-b)<s:
                return m
            else:
                if func(m)*func(b)<0:
                    a=m
                elif func(m)==0:
                    return m
                else:
                    b=m
        k+=1

while(True):
    print("Please enter the range of argument ant accurancy: ")
    a=float(input("a="))
    b=float(input("b="))
    s=float(input("ℇ="))
    if func(a)*func(b)>0:              #判断两端点处函数值符号是否相同，是则执行语句，否则直接用二分法求根
        if (func(a)-func(a+s))*(func(b)-func(b+s))<0:       #判断两端点处的斜率是否互异（求解二次函数或半周期三角函数的根）
            while(True):
                m = (a + b) / 2
                if func(a)*func(m) > 0:
                    if (func(m - s) - func(m)) * (func(m) - func(m + s)) < 0:       #如果成立，说明m点在在该精度下为函数极值点
                        if abs(func(m)) < s:                            #如果中间点的函数值的绝对值小于精度值ℇ，则该点为在该精度下函数的根
                            print("x0 =",m)
                            break
                        else:
                            break
                    elif (func(m - s) - func(m)) * (func(m) - func(m + s)) == 0:    #如果成立，说明m点在在该精度下为函数极值点，并取中间值为函数的根
                        if func(m) == func(m - s):
                            print("x0 =",m - s / 2)
                            break
                        else:
                            print("x0 =",m + s / 2)
                            break
                    else:
                        if (func(a) - func(a + s)) * (func(m) - func(m + s)) < 0:  #将m点的值赋给某一个端点，该端点的斜率与m点的斜率互异
                            b = m
                        else:
                            a = m
                        continue
                elif func(m)==0:
                    print("x0 =",m)
                    break
                else:                                 #用二分法分别求解二次函数或半周期三角函数的两个根（当其存在两个根时）
                    print("x1 =",sym_(a,m,s))
                    print("x2 =",sym_(m,b,s))
                    break
    else:
        print("x0 =",sym_(a,b,s))
        break
    break

