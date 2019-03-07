"""
-------------------------------------------------
   File Name：
   Description :将切割后的图像，根据速度平移至小行星对齐并堆叠
   Author :     李灿伟
   date：        2018_11_16前
-------------------------------------------------
   Change Activity:
        2018_11_16前：创建文件，完成目标
        2018.11.16：增加次部分说明
        2018.12.04:修改对齐方式，通过修改参数，可以对齐至不同图像
        2019.2.28:将计算时间差函数（get_time_difference）移至fits_function文件
        2019.2.28:修改程序，根据时间计算位移像素
        2019.02.01：
-------------------------------------------------
"""
from my_function import *
from fits_function import *
import os
time = get_time_difference(0)#和起始图像的时间差，单位秒
i = 0

path = "E:\\MyPro\\python_fit2\\fit_image\\apart"
txt_path = "E:\\MyPro\\python_fit2\\fit_image\\result\\asteroid\\位移像素.txt"
f = open(txt_path,"w")
filename = os.listdir(path)
s = 0
start = 0
end = 51
j = start

for v in range(-5,15):
    data_sum = ([])
    img = 0
    f.write(str(v)+"\n")
    for fit_name in filename[start:end]:
        if "fit" in fit_name or "fits" in fit_name:
            fit_path = path + "\\" + fit_name
            data = get_fits_data(fit_path)
            """这里要改参数哦！！"""
            b = move_fit(data, [0, 0], [(time[img])/6000*v, 0])
            f.write(fit_name+"\t"+str((time[img])/6000*v)+"\n")
            data_sum.append(np.array(b))
            img += 1
    print(str(v)+"\n\n\n")
    fusion_fit("E:\\MyPro\\python_fit2\\fit_image\\result\\asteroid\\" +str(start)+"_"+str(end) +"_"+ str( round(time[end-1]/6000*v,3))+"_mean_fusion.fit", data_sum, 1)
f.close()



