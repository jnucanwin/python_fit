"""
-------------------------------------------------
   File Name：
   Description :能用到的有关结构体
   Author :     李灿伟
   date：        2018_11_16前
-------------------------------------------------
   Change Activity:
        2018_11_16前：创建文件，完成目标
        2018.11.16：增加次部分说明
-------------------------------------------------
"""


class ComStar:
    def _init_(self, x1=0, y1=0, x2=0, y2=0, magnitude=0, SDx=0, SDy=0, pnext=None):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.magnitude = magnitude
        self.SDx = SDx
        self.SDy = SDy
        self.next = pnext


class StarNode:
    def __init__(self, star_name, x, y, alpha, beta, magnitude, pmra, pmrb, pnext = None):
        self.star_name = star_name
        self.x = x
        self.y = y
        self.alpha = alpha
        self.beta = beta
        self.magnitude = magnitude
        self.pmra = pmra
        self.pmrb = pmrb
        self.next = pnext


class Star:
    def __init__(self, line):
        self.star_name = line[0]
        self.x = line[1]
        self.y = line[2]
        self.alpha = line[3]
        self.beta = line[4]
        self.magnitude = line[5]
        self.pmra = line[6]
        self.pmrb = line[7]


class FitsRef:
    def __init__(self, line, pnext=None):
        self.file_name = line[0]
        self.star_num = line[1]
        self.star = pnext




