# """重构函数，将代码分为一系列具体工作的函数，分为三部分，1获取存储用户名2新用户提示输入3问候用户执行主函数"""
import json
def get_username():
    filename='使用json存储数据2.json'
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_newuser():
    username=input("what's your name? ")
    filename='使用json存储数据2.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user():
    username=get_username()
    if username:
        print("welcome back "+username+"!")
    else:
        username=greet_newuser()
        print("we will remember you when you come back "+username)
def rename_user():
    filename="使用json存储数据2.json"
    username=input("please enter new name ")
    with open(filename,'w')as f_obj:
        json.dump(username,f_obj)
    print('new name has been writen')
greet_user()
rename_user()

