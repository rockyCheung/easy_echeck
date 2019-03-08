# -*- coding:utf-8 -*-
c_bin = "AAAAAA"
c_product_type = "BBB"
c_serilise  = "DDDDDDD"
c_v = "E"
# E位的运算规则：E位以前的数据，自右向左，偶位的数字乘2，将乘2后的积与未参与运算的数字进行相加，相加后的和与10求模，再用10减余数得到校验位