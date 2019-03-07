"""
-------------------------------------------------
   File Name：
   Description :得到文件夹下fit图像的名称和拍摄时间及时间间隔
   Author :     李灿伟
   date：        2018_11_16前
-------------------------------------------------
   Change Activity:
        2018_11_16前：创建文件，完成目标
        2018.11.16：增加次不分说明
-------------------------------------------------
"""
from fits_function import *
import os

f = open('E:\\MyPro\\python_fit2\\fit_image\\obs_time.txt',"w")
f1 = open('E:\\MyPro\\python_fit2\\fit_image\\image_name.txt',"w")
path = "E:\\MyPro\\python_fit2\\fit_image"
filename = os.listdir(path)
for fit_name in filename:
    if "fit" in fit_name or "fits" in fit_name:
        fit_path = path + "\\" + fit_name
        obs_time = get_fits_obs_time(fit_path)
        obs_time = obs_time.replace(":", " ").replace("-", " ").replace("T", " ")

        # obs_time= obs_time.split().
        f.write(obs_time+"\n")
        f1.write(fit_name + "\n\n\n")
f.close()
f1.close()

f = open('E:\\MyPro\\python_fit2\\fit_image\\time_difference.txt',"w")
f1 = open('E:\\MyPro\\python_fit2\\fit_image\\obs_time.txt')
s = f1.readlines()

data0 = s[0]
data0 = data0.split()
time0 = (int(data0[3])*60+int(data0[4]))*60+int(data0[5])
for data in s:
    data = data.split()
    time = (int(data[3])*60+int(data[4]))*60+int(data[5])
    obs_interval = time - time0
    f.write(str(obs_interval)+"\n")

f.close()
f1.close()




