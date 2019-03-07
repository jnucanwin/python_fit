"""
-------------------------------------------------
   File Name：
   Description :将文件夹下的图像进行裁剪，才去黑边
   Author :     李灿伟
   date：        2018_11_16前
-------------------------------------------------
   Change Activity:
        2018_11_16前：创建文件，完成目标
        2018.11.16：增加次部分说明，发现程序中存在冗余代码，未修改。
-------------------------------------------------
"""
from my_function import *
from fits_function import *
import os


path = "E:\\MyPro\\python_fit2\\fit_image\\result\\asteroid"
filename = os.listdir(path)
for name in filename:
    if "fit" in name:
        fit_path = path + "\\" + name
        data = get_fits_data(fit_path)
        data = np.array(data)
        data = data[10:380, 10:380]
        f = fits.writeto(fit_path, data, overwrite=True)



