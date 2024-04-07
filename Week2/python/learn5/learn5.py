# 数组切片
a_list = ["physics", "chemistry", 2017, 2.5, [0.5,3]]
a = a_list
print(a)
print(a[1:3])
print(a[1:-1])
print(a[1:])
print(a[:3])
print(a[:])
print(a[0::2]) # 间隔为2
print(a[::-1]) # 直接倒序

# 列表添加元素
a_add = ["a_add"]
a = a + a_add
print(a)
a.append(a_add)
print(a) # 这里注意区分 + 和 append是不一样的
a.extend([3,2]) 
print(a) # extend跟append不一样，有点像+
a.insert(2,3.14) # index,value
print(a)

# 列表检索元素
a.append(2017)
print(a)
# 首次出现
index = a.index(2017) # index(value,start,end)
print(index)
index = a.index(2017,3) # index(value,start,end)
print(index) # 从索引3开始查找
# index = a.index(2017,4,10) # index(value,start,end)
# print(index) # 从索引4到索引10查找

# 列表元素计数
count = a.count(3)
print(count)
count = a.count(2017)
print(count)

# 列表是否存在元素
print(a)
print(2017 in a)
print(0.5 in a) # 注意区分
print([0.5,3] in a) # 注意区分
print([3,0.5] not in a) # 注意区分 顺序?

# 列表删除元素
print(a)
del a[1] # 依据索引
print(a)
a.remove(2.5) # 依据value remove(value)
print(a)
print(a.pop(1)) # 依据index pop(index) 还会返回值
print(a)
# 删除列表
print(id(a))
print(id(a_list))
# del a
# print(a_list)

# 列表比较
b = [1,1,1,1,1]
b_l = [1,2,1,1,1]
b_s = [0,1,1,1,1]
c = [1,1,1,1,1]
# d = [1,"a",1,1,1]
# e = [1,"a","python",1,1]
f = ["1","b","python"]
g = ["2","3","4"]
# python 2.x
# cmp(a_list,b)
# python 3.x
# 字符串已经和数字比不了了
# print(b>b_l,b>b_s,b==c,b>d,b>e)
# print(max(d))
# 最大值最小值比较
print(max(b_l))
print(min(f))
# 同一类型还能比
print(f>g)
print(b>b_l)
print(b>b_s)
print(b==c)
# 求和
print(b_l)
sum = sum(b_l)
print("求和:",sum)

# 列表排序
list_ = [90, 70, 45, 67 ,109]
list_sort = sorted(list_) # 升序
print(list_sort)
list_sort = sorted(list_, reverse=True) # 降序
print(list_sort)

list_sort.sort()
print(list_sort)
list_sort = list_.sort() # 区分
print(list_sort)

# 二维列表指定排序
array = [("Li", 88), ("Zhang",78), ("Wang", 60), ("Zhao", 90)]
array_sort = sorted(array, key=lambda a:a[1])
print(array_sort)


# 列表翻转
list_reverse = list_
print(list_reverse)
list_reverse.reverse()
print(list_reverse)

# 元组创建
a = (1)
print(a)
a = (1,)
print(a)
a = (1,2,3)
print(a)

# 切片读取和列表一样
# 检索和计数也一样

# 元组不能随便删除和更改
# a[1] = 3 # 不能改元素
# del a[1] # 不能删元素
del a # 可以整个删除

# 元组与列表的转换
a = [1,2,3,4,5]
print(type(a),a)
a = tuple(a)
print(type(a),a)
a = list(a)
print(type(a),a)

# 元组赋值
v = ["!",1]
x,y = v
print(x,y)

# 字符串
# 加反斜杠代表不变
string = "Programe \"Python\""
print(string)

# 分片
string = 'Python Program'
print(string[0:7:2]) # start stop stride
print(string[-1:-20])
print(string[-20:-1])
print(string[-1:-20:-1])

# 前取n个 后取n个
n = 5
print(string[:n])
print(string[-n:])
# 中间从第k个取n个
k = 2
print(string[k-1:n+k-1])

# 用加号连接
a = "Python"
b = " No.1"
print(a+b)
print(a*2) # 重复

# 字符串比较
print("abc">"abd")
print("bbc">"abd")
print("bbc"<"abdd")
print(""<"0")
print()

# 是否在
print("aab" in "a")
print("a" in "aab")
print("aa" in "aab")
print("aab" in "aab")
print("ac" in "aab")

# 查找find函数
string = "Guangdong is Guangdong"
print(string.find("Guangdong"))
print(string.find("Guangdong", 2))
print(string.find("Guangdong", 25, 30)) # 没找到返回-1

# 字符串替换
string = string.replace("Guangdong","Beijing")
print(string)

# 字符串分割
string = "beijing,shanghai,guangzhou,shenzhen"
string = string.split(",")
print(string)

# 利用字符串分割来做字符串相减
string = "abcde'-'de"
print(string)
# string = string - "de" # 报错
string = string.replace("'","")
string_minus = string.split('-')
string = string_minus[0].replace(string_minus[1],"")
print(string)

# 字典创建
dictionary = {"Alice":95, "Beth":45, "Cat":105}
print(dictionary)
dictionary = dict(zip(["one", "two", "three"], [1, 2, 3]))
print(dictionary)
dictionary = dict([("one", 1), ("two", 2), ("three", 3)])
print(dictionary)
dictionary = dict((("one", 1), ("two", 2), ("three", 3)))
print(dictionary)
dictionary = dict({("one", 1), ("two", 2), ("three", 3)})
print(dictionary)

dictionary = {}.fromkeys((1,2,3), "student")
print(dictionary)

# 字典得值
print(dictionary[1])

# 字典修改
dictionary[2]="twice"
print(dictionary)

# 字典添加
dictionary["three"] = 3
print(dictionary)

# 字典合并
dictionary_add = {"Alice":95, "Beth":45, "Cat":105}
dictionary.update(dictionary_add)
print(dictionary)

# 字典删除元素
del_dictionary = dictionary.pop(1)
print(del_dictionary)
print(dictionary)
del dictionary[2]
print(dictionary)
print(dictionary.popitem())
print(dictionary)

# 字典删除
dictionary_add.clear()
print(dictionary_add)
# del dictionary_add

# 字典遍历
key = dictionary.keys()
print(key)
value = dictionary.values()
print(value)
item = dictionary.items()
print(item)

# 集合
