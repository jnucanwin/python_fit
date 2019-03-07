# """
# -------------------------------------------------
#    File Name：
#    Description :根据时间差和速度求得位移差
#    Author :     李灿伟
#    date：        2018_12_25
# -------------------------------------------------
#    Change Activity:
#         2018_11_25：创建文件，使用最小二乘拟合进行转换
#
# -------------------------------------------------
# """
#
#
# from my_function import *
#
# txt_path = "E:\\MyPro\\python_fit2\\fit_image\\time_difference.txt"
# i = 0
# with open(txt_path) as f:
#     lines = f.readlines()
#     for line in lines:
#         line = int(line.split()[0])
#         lines[i] = line
#         i = i+1
#
#
# txt_path = "E:\\MyPro\\python_fit2\\fit_image\\星象匹配.txt"
# x1 = []
# y1 = []
# x2 = []
# y2 = []
# match_star_num = 0
# with open(txt_path) as f:
#     lines = f.readlines()  # 读取全部内容
#     for s in lines:
#         if s != " " and s != "\n":
#             s = s.split()
#
#             x1.append(float(s[3]))
#             y1.append(float(s[4]))
#             x2.append(float(s[1]))
#             y2.append(float(s[2]))
#             match_star_num += 1
# const = get_plate_consts6(x1, y1, x2, y2, match_star_num)
# f2 = open('E:\\MyPro\\python_fit2\\fit_image\\位置测试.txt',"w")
# f3 = open('E:\\MyPro\\python_fit2\\fit_image\\六常数模型.txt',"w")
# i = 0
# f3.write(str(const[0])+" * ra + "+str(const[1])+" * de + "+str(const[2])+"\n"+str(const[3])
#          +" * ra + "+str(const[4])+" * de + "+str(const[5]))
# while i < match_star_num:
#
#     f2.write(str((x2[i]-(const[0]*x1[i]+const[1]*y1[i]+const[2]))*0.21)+"\t"+str((y2[i]-(const[3]*x1[i]+const[4]*y1[i]+const[5]))*0.21)+"\n")
#     i = i+1
# f3.close()
# f2.close()
#
# x = []
# y = []
# txt_path="E:\\MyPro\\python_fit2\\fit_image\\目标天球坐标.txt"
# with open(txt_path) as f:
#     lines = f.readlines()  # 读取全部内容
#     for s in lines:
#         if s != " " and s != "\n" and len(s)>25:
#             s = s.split()
#             ra = ((float(s[8])/60+float(s[7]))/60+float(s[6]))*15
#             if float(s[9]) < 0:
#                 de = ((float(s[11])/60+float(s[10]))/60+(-1*float(s[9])))*(-1)
#             else:
#                 de = ((float(s[11]) / 60 + float(s[10])) / 60 + (float(s[9])))
#             x.append(const[0]*ra+const[1]*de+const[2])
#             y.append(const[3]*ra+const[4]*de+const[5])
#
#
# f1 = open('E:\\MyPro\\python_fit2\\fit_image\\move.txt',"w")
#
# path = "E:\\MyPro\\python_fit2\\fit_image\\move"
# filename = os.listdir(path)
# i = 0
# for fit_name in filename :
#         if "fit" in fit_name or "fits" in fit_name:
#             f1.write(fit_name + "\n"+str(x[i])+"\t"+str(y[i])+"\n")
#             i = i+1
# f1.close()
#
#
#
#
