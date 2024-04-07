# 截取路径和文件名
path = "D:\\data\\Usa\\states.shp"
path_split = path.split("\\")
file_path = "\\".join(path_split[:-1])
file_name = path_split[-1]
print(path_split)
print(file_path)
print(file_name)

# 另一种方法rfind
n = path.rfind("\\")
file_path = path[:n]
file_name = path[n+1:]
print(file_path)
print(file_name)

# 直接用os
import os
file_path = os.path.dirname(path)
file_name = os.path.basename(path)
print(file_path)
print(file_name)