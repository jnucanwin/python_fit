"""
-------------------------------------------------
   File Name：
   Description :图像转换值恒星对齐
   Author :     李灿伟
   date：        2018_11_16前
-------------------------------------------------
   Change Activity:
        2018_11_16前：创建文件，完成目标
        2018.11.16：增加次部分说明
        2018.11.20:取消手动每次修改基准名称，改为自动读取第一幅图名称
                    todo:应该修改到能输入文件编号来选择基准
-------------------------------------------------
"""
from my_function import *
from fits_function import *
import os

path = "E:\\MyPro\\python_fit2\\fit_image"
filename = os.listdir(path)
result = "2R.fit"
f = open('E:\\MyPro\\python_fit2\\fit_image\\image_name.txt')
star_name = (f.read().split())[0]
f.close()

for fit_name in filename:
    if "fit" in fit_name or "fits" in fit_name:
        if fit_name != star_name:
            fit_path = path + "\\" + fit_name
            data = get_fits_data(fit_path)
            txt_path = path + "\\" + "ppwj.txt"
            const = get_consts6(txt_path, fit_name)

            b = merge_plate(data, const)
            result = list(fit_name)
            result[0] = fit_name[0]+"R"
            result = "".join(result)
            result_path = "E:\\MyPro\python_fit2\\fit_image\\move\\" + result
            f = fits.writeto(result_path, np.array(b), overwrite=True)
            print(result + "完成")
        else:
            fit_path = path + "\\" + fit_name

            result = list(fit_name)
            result[0] = fit_name[0] + "R"
            result = "".join(result)
            data = get_fits_data(fit_path)
            result_path = "E:\\MyPro\python_fit2\\fit_image\\move\\" + result
            f = fits.writeto(result_path, np.array(data), overwrite=True)