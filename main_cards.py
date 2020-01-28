import cards_defs
# 程序循环执行
while True:

    # 显示菜单
    cards_defs.menu()

    # 键入选择
    temp = input("请输入要执行的操作:")
    print("你选择的操作为:[%s]" % temp)

    # 判断要进行的操作程序
    if temp in ["1","2","3"]:
        # 查看联系人
        if temp == "1":
            cards_defs.show()

        # 新建联系人
        elif temp == "2":
            cards_defs.new()

        # 查找联系人
        else:
            cards_defs.find()

    # 当输入为0时,退出循环,程序结束
    elif temp == "0":
        print("程序结束,感谢使用!")
        break

    # 输入错误
    else:
        print("输入错误,请检查后重新输入!")
