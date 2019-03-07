"""
-------------------------------------------------
   File Name：
   Description :有关的数学函数，与fit无关，只与数学有关
   Author :     李灿伟
   date：        2018_11_16前
-------------------------------------------------
   Change Activity:
        2018_11_16前：创建文件，完成目标
        2018.11.16：增加此部分说明
-------------------------------------------------
"""
import numpy as np
from scipy.linalg import solve
from my_struct import *
import time
import os
from ctypes import *
# adder = CDLL('./test_c.dll')


def gauss_solve_linear_equation(A, b):
    """
    求解多元线性方程
    :param A:系数矩阵，一个二维列表。
    :param b:右端向量，一个一维列表
    :return x:解列表（numpy.ndarray）
    """
    a = np.array(A)
    right_matrix = np.array(b)
    x = solve(a, right_matrix)
    return x


def init_come_array(com_stars, x1=[], y1=[], x2=[], y2=[], n=0):
    """
    求解共同星，赋给x,y列表（list）
    :param com_stars:一个ComStar()类的链表的头结点(非空)
    :param x1:第一个文件的x坐标，一维列表（空）
    :param y1:第一个文件的y坐标，一维列表（空）
    :param x2:目标文件的x坐标，一维列表（空）
    :param y2:目标文件的y坐标，列表（空）
    :param n:公共星数，整形（具体）
    """
    p = com_stars.next
    for i in range(0, n):
        x1.append(p.x1)
        x2.append(p.x2)
        y1.append(p.y1)
        y2.append(p.y2)
        p = p.next


def get_plate_consts6(x1=[], y1=[], x2=[], y2=[], n=0, ):
    """
    得到2-->1变换的六常数
    :param x1:第一个文件的x坐标，一维列表（非空）
    :param y1:第一个文件的y坐标，一维列表（非空）
    :param x2:目标文件的x坐标，一维列表（非空）
    :param y2:目标文件的y坐标，列表（非空）
    :param n:共同星数目（具体）
    :return consts:六常数，一维列表(list)
    """
    n = len(x1)
    for i in range(n):
        x1[i] = float(x1[i])
        y1[i] = float(y1[i])
        x2[i] = float(x2[i])
        y2[i] = float(y2[i])
    A = [([0] * 3) for i in range(3)]
    a = [0 for i in range(3)]
    b = [0 for i in range(3)]
    consts = [0 for i in range(6)]
    for i in range(0, n):
        A[0][0] += x1[i] * x1[i]
        A[0][1] += x1[i] * y1[i]
        A[1][0] = A[0][1]
        A[0][2] += x1[i]
        A[2][0] = A[0][2]
        A[1][1] += y1[i] * y1[i]
        A[1][2] += y1[i]
        A[2][1] = A[1][2]
        A[2][2] += 1
        a[0] += x1[i] * x2[i]
        a[1] += y1[i] * x2[i]
        a[2] += x2[i]
        b[0] += x1[i] * y2[i]
        b[1] += y1[i] * y2[i]
        b[2] += y2[i]

    B = [([0] * 3) for i in range(3)]
    for i in range(3):
        for j in range(3):
            B[i][j] = A[i][j]
    #   TODO:高斯求解,这里还需要进行异常处理
    a = gauss_solve_linear_equation(A, a)
    b = gauss_solve_linear_equation(B, b)
    for i in range(3):
        consts[i] = a[i]
        consts[i + 3] = b[i]

    return consts


def get_consts6(txt_path="E:\\MyPro\\Test\\Test\\ppwj.txt", fits_name="2.fit"):
    """
    得到目标转换的六常数(第一幅图的坐标经--->到第二幅图的坐标)
    :param txt_path:txt文件的路径和文件名
    :param fits_name:目标文件名
    :return:六常数，一维列表(list)
    """
    with open(txt_path) as f:
        s = f.readline()
        # file_name = "1.fits"
        fits_ref1 = FitsRef(s.split())

        message = []
        fits_ref1.star = message
        for i in range(int(fits_ref1.star_num)):
            line = f.readline().split()
            star = Star(line)
            message.append(star)
        filename1 = fits_name

        # TODO:缺少异常处理。
        while True:
            s = f.readline()
            while s[0] == " " or s[0] == "\n":
                s = f.readline()
            fits_ref2 = FitsRef(s.split())
            message = []
            fits_ref2.star = message
            if fits_ref2.file_name == filename1:
                for i in range(int(fits_ref2.star_num)):
                    line = f.readline().split()
                    star = Star(line)
                    message.append(star)
                break
            else:
                for i in range(int(fits_ref2.star_num)):
                    line = f.readline().split()
    com_star = ComStar()
    p = com_star
    for i in range(int(fits_ref2.star_num)):
        """
        这里的x,y好像和文件读取的xy是相反的
        """
        p.next = ComStar()
        p = p.next
        p.next = None
        p.x2 = fits_ref2.star[i].x
        p.y2 = fits_ref2.star[i].y
        p.x1 = fits_ref1.star[int(fits_ref2.star[i].star_name) - 1].x
        p.y1 = fits_ref1.star[int(fits_ref2.star[i].star_name) - 1].y
        p.magnitude = fits_ref1.star[int(fits_ref2.star[i].star_name) - 1].magnitude
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    init_come_array(com_star, x1, y1, x2, y2, int(fits_ref2.star_num))
    return get_plate_consts6(x1, y1, x2, y2, int(fits_ref2.star_num))


# """"这里基本失败了，全部注释掉，以防以后弄得着""
# def get_consts6_2(txt_path="E:\\MyPro\\Test\\Test\\ppwj.txt", fits_name1="", fits_name=""):
#     """
#
#     -------------------------------------------------------------------
#     Change Activity:
#                    2018_11_15:根据 get_consts6 编写
#     :param txt_path:txt文件的路径和文件名
#     :param fits_name1:原图文件名
#     :param fits_name:目标文件名
#     :return:六常数，一维列表(list)
#     """
#     with open(txt_path) as f:
#         while True:
#             s = f.readline()
#             while s[0] == " " or s[0] == "\n":
#                 s = f.readline()
#             fits_ref1 = FitsRef(s.split())
#             message = []
#             fits_ref1.star = message
#             if fits_ref1.file_name == fits_name1:
#                 for i in range(int(fits_ref1.star_num)):
#                     line = f.readline().split()
#                     star = Star(line)
#                     message.append(star)
#                 break
#             else:
#                 for i in range(int(fits_ref1.star_num)):
#                     line = f.readline().split()
#         # TODO:缺少异常处理。
#     f.close()
#     with open(txt_path) as f:
#         while True:
#             s = f.readline()
#             while s[0] == " " or s[0] == "\n":
#                 s = f.readline()
#             fits_ref2 = FitsRef(s.split())
#             message = []
#             fits_ref2.star = message
#             if fits_ref2.file_name == fits_name:
#                 for i in range(int(fits_ref2.star_num)):
#                     line = f.readline().split()
#                     star = Star(line)
#                     message.append(star)
#                 break
#             else:
#                 for i in range(int(fits_ref2.star_num)):
#                     line = f.readline().split()
#     f.close()
#     com_star = ComStar()
#     p = com_star
#     for i in range(int(fits_ref2.star_num)):
#         """
#         这里不对啊  ，，，咋办啊 ，，，，写不对
#         """
#         p.next = ComStar()
#         p = p.next
#         p.next = None
#         p.x2 = fits_ref2.star[i].x
#         p.y2 = fits_ref2.star[i].y
#         p.x1 = fits_ref1.star[int(fits_ref2.star[i].star_name) - 1].x
#         p.y1 = fits_ref1.star[int(fits_ref2.star[i].star_name) - 1].y
#         p.magnitude = fits_ref1.star[int(fits_ref2.star[i].star_name) - 1].magnitude
#     x1 = []
#     x2 = []
#     y1 = []
#     y2 = []
#     init_come_array(com_star, x1, y1, x2, y2, int(fits_ref2.star_num))
#     return get_plate_consts6(x1, y1, x2, y2, int(fits_ref2.star_num))


def merge_plate(fit_data, consts):
    """
    根据传入的六常数，对图像数据进行变换
    :param fit_data:图像的二维列表(要转换的图的信息)
    :param consts: 六常数（list）
    :return:
    """
    b = [([0] * len(fit_data[0])) for i in range(len(fit_data))]
    # fit_data = fit_data.tolist()
    yy = len(fit_data)
    xx = len(fit_data[0])

    time1 = time.time()
    print(time1)
    i = 0
    while i < xx:
        j = 0
        while j < yy:
            x = consts[0] * i + consts[1] * j + consts[2]
            y = consts[3] * i + consts[4] * j + consts[5]
            if x >= 0 and y >= 0:
                lx = int(x)
                ly = int(y)
                if lx >= 0 and ly >= 0 and lx+1 < xx and ly + 1 < yy:
                    xd = x - lx
                    yd = y - ly
                    fe = 0
                    ff = 0
                    a1 = 1 - xd
                    a2 = lx + 1
                    a3 = ly + 1
                    fe = a1 * fit_data[ly][lx] + xd * fit_data[ly][a2]
                    ff = a1 * fit_data[a3][lx] + xd * fit_data[a3][a2]
                    b[j][i] = (1 - yd) * fe + yd * ff
            j = j + 1
        i = i + 1

    time2 = time.time()
    print(time2)
    print(str(time2-time1))
    return b

# """"这里基本失败了，全部注释掉，以防以后弄得着""
# def merge_plate2(fit_data, consts,dx,dy):
#     """
#     根据传入的六常数，对图像数据进行变换
#     :param fit_data:图像的二维列表(要转换的图的信息)
#     :param consts: 六常数（list）
#     :param dx: x方向的位移（int）
#     :param dx: y方向的位移（int）
#     :return:
#     """
#     b = [([0] * len(fit_data[0])) for i in range(len(fit_data))]
#     # fit_data = fit_data.tolist()
#     yy = len(fit_data)
#     xx = len(fit_data[0])
#
#     time1 = time.time()
#     print(time1)
#     i = 0
#     while i < xx:
#         j = 0
#         while j < yy:
#             x = consts[0] * (i+dx) + consts[1] * (j+dy) + consts[2]
#             y = consts[3] * (i+dx) + consts[4] * (i+dx) + consts[5]
#             if x >= 0 and y >= 0:
#                 lx = int(x)
#                 ly = int(y)
#                 if lx >= 0 and ly >= 0 and lx+1 < xx and ly + 1 < yy:
#                     xd = x - lx
#                     yd = y - ly
#                     fe = 0
#                     ff = 0
#                     a1 = 1 - xd
#                     a2 = lx + 1
#                     a3 = ly + 1
#                     fe = a1 * fit_data[ly][lx] + xd * fit_data[ly][a2]
#                     ff = a1 * fit_data[a3][lx] + xd * fit_data[a3][a2]
#                     b[j][i] = (1 - yd) * fe + yd * ff
#             j = j + 1
#         i = i + 1
#
#     time2 = time.time()
#     print(time2)
#     print(str(time2-time1))
#     return b


def get_asteroid_coordinate(fits_name="1R.fit", txt_path="E:\\MyPro\\python_fit2\\fit_image\\move.txt"):
    with open(txt_path) as f:
        while True:
            s = f.readline()
            if s != " " and s != "\n":
                s = s.split()
                if s[0] == fits_name:
                    s = f.readline()
                    while s == " " or s == "\n":
                        s = f.readline()
                    coordinate = s.split()
                    break
        return coordinate


def move_fit(fit_data, coor1, coor2):
    """
    :param fit_data: 需要平移图像的数据
    :param coor1: 原图坐标点
    :param coor2: 对应的需要平移图的坐标点
    :return: 平移后的图像数据部分
    """
    print(str(coor2[0])+"  "+str(coor2[1])+"\n")
    dx = float(coor2[0]) - float(coor1[0])
    dy = float(coor2[1]) - float(coor1[1])
    b = [([0] * len(fit_data[0])) for i in range(len(fit_data))]
    if dx == 0 and dy == 0:
        return fit_data
    yy = len(fit_data)
    xx = len(fit_data[0])
    i = 0
    while i < xx:
        j = 0
        while j < yy:

            x = i+dx
            y = j+dy
            if x >= 0 and y >= 0 and x < xx and y < yy:
                lx = int(x)
                ly = int(y)
                if lx >= 0 and ly >= 0 and lx+1 < xx and ly + 1 < yy:
                    xd = x - lx
                    yd = y - ly
                    a1 = 1 - xd
                    a2 = lx + 1
                    a3 = ly + 1
                    fe = a1 * fit_data[ly][lx] + xd * fit_data[ly][a2]
                    ff = a1 * fit_data[a3][lx] + xd * fit_data[a3][a2]

                    b[j][i] = (1 - yd) * fe + yd * ff
            j = j + 1
        i = i + 1

    return b


