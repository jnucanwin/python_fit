"""
-------------------------------------------------
   File Name：
   Description :对fit文件进行存取融合等操作
   Author :     李灿伟
   date：        2018_11_16前
-------------------------------------------------
   Change Activity:
        2018_11_16前：创建文件，完成目标
        2018.11.16：增加此部分说明
        2018.11.21:修改get_fits_data()函数说明，使之更加准确
        2019.02.28:
-------------------------------------------------
"""
from astropy.io import fits
import numpy as np


def open_fits(file_name=""):
    """
    得到fits文件的HDU列表
    :param file_name: fits文件名
    :return: 文件的HDU列表(astropy.io.fits.hdu.hdulist.HDUList)
    """
    if "fit" in file_name[30:]:
        hdu_list = fits.open(file_name)
        return hdu_list


def get_fits_data(path=""):
    """
    得到路径队形的图像的数据（hdu[0].data需要是一个二维ny形矩阵）
    :param path: 文件路径
    :return: 数据部分（二维列表）
    """

    hdu = open_fits(path)
    ac = hdu[0].data.tolist()

    return ac


def get_fits_obs_time(path=""):
    hdu = open_fits(path)
    obs_time = hdu[0].header["DATE"]
    return obs_time


def fusion_fit(path="", data=[[[]]], mode=0):
    """

    :param data:图像数据数组（三维列表）
    :param mode:融合方式（0=中值 1=均值）
    :return:将结果以fit图片形式输出
    """
    x = len(data)
    y = len(data[0])
    z = len(data[0][0])

    if mode == 0:
        print("开始中值融合")
        mid_fit = [([0] * z) for i in range(y)]
        for i in range(y):
            for j in range(z):
                data_list = []
                for num in range(x):
                    data_list.append(data[num][i][j])
                mid_fit[i][j] = np.median(data_list)
        print("中值融合完成")

        fits.writeto(path, np.array(mid_fit),overwrite=True)
        return 0

    if mode == 1:
        print("开始均值融合")
        median_fit = [([0] * z) for i in range(y)]
        for i in range(y):
            for j in range(z):
                data_list = []
                for num in range(x):
                    data_list.append(data[num][i][j])
                median_fit[i][j] = (np.mean(data_list))
        print("均值融合完成")

        fits.writeto(path, np.array(median_fit), overwrite=True)
        # return fits.writeto("s_median_fusion.fit", np.array(median_fit))
    if mode == 2:
        print("开始总值融合")
        median_fit = [([0] * z) for i in range(y)]
        for i in range(y):
            for j in range(z):
                data_list = []
                for num in range(x):
                    data_list.append(data[num][i][j])
                median_fit[i][j] = np.sum(data_list)
        print("总值融合完成")

        fits.writeto(path, np.array(median_fit), overwrite=True)
        # return fits.writeto("s_median_fusion.fit", np.array(median_fit))


def get_time_difference(basis=0,path="E:\\MyPro\\python_fit2\\fit_image\\time_difference.txt",):
    time = []
    s = []
    with open(path) as f:
        s = f.readlines()
    for t in s:
        t.split()
        # time.append(int(t)-basis)
        time.append(int(t))
    b = time[basis]
    if basis < len(time):
        for t in range(len(time)):
            time[t] = time[t] - b
    return time
