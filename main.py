num = input("请输入一个5位数字：")
if not (num.isdigit() and len(num) == 5):
    print("输入错误: 请输入5位数字")
else:
    if num == num[::-1]:
        print(f"{num} -> 是回文数")
    else:
        print(f"{num} -> 不是回文数")
