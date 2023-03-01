import sys;x='W3Cschool';sys.stdout.write(x+'\n')
# python可以在同一行中使用多条语句，语句之间用分号（；）分割。
# 缩进相同的一组语句构成一个代码块，我们称之代码组。像if、while、def和class这样的复合语句，首行以关键字开始，以冒号（：）结束，该行之后的一行或多行代码构成代码组
if expression :
    suite
elif expression :
    suite
else :
    suite

# print是默认换行的，如果要实现不换行，需要在变量末尾加上end=" "
x="a"
y="b"
print(x)
print(y)
print('----------')
print(x,end=" ")
print(y,end=" ")
print()

# import somemodule 将整个模块导入
# from somemodule import somefunction 从某个模块导入某个函数
# from somemodule import firstfunc，secondfunc，thirdfunc 从某个模块导入多个函数
# from somemodule import * 从某个模块导入全部函数

