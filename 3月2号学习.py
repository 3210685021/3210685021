# 斐波纳契奇数求和
a , b = 0 , 1
while b < 10 :
    print(b)
    a , b = b , a + b

# 两个元素的总和确定了下一个数
a , b = 0 , 1
while b < 1024 :
    print(b , end=',')
    a , b = b , a + b

# if控制的简单运用
age = int(input("请输入你家狗狗的年龄: ")) 
print("") 
if age < 0:  
    print("请输入正确的年龄。") 
elif age == 1:  
    print("相当于 14 岁的人。") 
elif age == 2:  
    print("相当于 22 岁的人。") 
elif age > 2:  
    human = 22 + (age -2)*5  
print("对应人类年龄: ", 
human) 
### human运行显示未定义不知道什么意思
### 退出提示，本地环境下可以使用这样的退出提示使代码更易用 
input('点击 enter 键退出')