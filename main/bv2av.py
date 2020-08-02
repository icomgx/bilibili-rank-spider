#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bv2av.py
@Time    :   2020/06/14 11:50:18
@Author  :   Gu Pengcheng 
@Version :   1.0
@Contact :   lewisgu@outlook.com
@License :   (C)Copyright
@Desc    :   None
'''

# here put the import lib

table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr={}
for i in range(58):
    tr[table[i]]=i
s=[11,10,3,8,4,6]
xor=177451812
add=8728348608

def dec(bv_id):
    r = 0
    for i in range(6):
        r += tr[bv_id[s[i]]]*58**i
    return (r-add)^xor

def enc(av_id):
    av_id = (av_id^xor)+add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[av_id//58**i%58]
    return ''.join(r)

def check_b2a_a2b(bv_id_ori):
    av_id = dec(bv_id_ori)
    bv_id_new = enc(av_id)
    if bv_id_ori != bv_id_new:
        return 0
    else:
        return 1




# 作者：mcfx
# 链接：https://www.zhihu.com/question/381784377/answer/1099438784
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。