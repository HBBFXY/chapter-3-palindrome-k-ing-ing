user_input = input("请输入一个5位数字：")
if not user_input.isdigit():
     print("错误提示：输入不是纯数字")
elif len(user_input) != 5:
     print("错误提示：输入不是5位数字")
else:

     if user_input == user_input[::-1]:
         print("是回文数")
     else:
         print("不是回文数")
