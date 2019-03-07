"""
-------------------------------------------------
   File Name：
   Description :将图像分割成合适大小，以加速后续处理速度
   Author :     李灿伟
   date：        2018_11_24
-------------------------------------------------
   Change Activity:
        2018_11_24：创建文件，完成目标

-------------------------------------------------
"""

from fits_function import *
from astropy.io import fits
import numpy as np
import os

length = 200
start_point_x = 1322
start_point_y = 337
f = open('E:\\MyPro\\python_fit2\\fit_image\\apart\\变化.txt',"w")
f.write("结果图x + \t"+str(start_point_x-length)+"\t是原图的x"+"\n" +
        "结果图y + \t"+str(start_point_y-length+2056)+"\t是原图的y")
f.close()

def apart_fit(fit_path=""):
    data = np.array(get_fits_data(fit_path))
    """结果x---->原图x:+start_point_x-length
       结果y--->原图y：+start_point_y-length
    """
    fit_p = fit_path.split('\\')
    data2 = data[start_point_y-length:start_point_y+length, start_point_x-length:start_point_x+length]
    fit_path2 = "E:\\MyPro\\python_fit2\\fit_image\\apart\\"+fit_p[-1]
    fits.writeto(fit_path2, np.array(data2),overwrite=True)


path = "E:\\MyPro\\python_fit2\\fit_image\\move"
filename = os.listdir(path)

for fit_name in filename:
    fit_path = path + "\\" + fit_name
    if "fit" in fit_name or "fits" in fit_name:
        print(fit_path)
        apart_fit(fit_path)

