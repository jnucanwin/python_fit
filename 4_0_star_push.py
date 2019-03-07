"""
-------------------------------------------------
   File Name：
   Description :将转换后的图像，根据位移平移至小行（恒星？？？？）星对齐
   Author :     李灿伟
   date：        2018_11_16前
-------------------------------------------------
   Change Activity:
        2018_11_16前：创建文件，完成目标
        2018.11.16：增加次部分说明
        2018.12.04:修改对齐方式，通过修改参数，可以对齐至不同图像
        2019.2.23：感觉这个是恒星对齐，上面写的description可能错了
-------------------------------------------------
"""
from my_function import *
from fits_function import *
import os
txt_path = "E:\\MyPro\\python_fit2\\fit_image\\time_difference.txt"
i = 0
with open(txt_path) as f:
    lines = f.readlines()
    for line in lines:
        line = int(line.split()[0])
        lines[i] = line
        i = i+1

path = "E:\\MyPro\\python_fit2\\fit_image\\apart"
filename = os.listdir(path)
data_sum = ([])
for fit_name in filename[0:51]:
    if "fit" in fit_name or "fits" in fit_name:
        fit_path = path + "\\" + fit_name
        data = get_fits_data(fit_path)
        """这里要改参数哦！！"""

        data_sum.append(np.array(data))

fusion_fit("E:\\MyPro\\python_fit2\\fit_image\\result\\start\\" + "mean_fusion.fit", data_sum, 1)


j = 0
# print("aaaaaaaaaa")
