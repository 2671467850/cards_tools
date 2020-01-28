cards_list = []
# 菜单目录
def menu():
    print("*" * 30)
    print("-联系人管理系统!-")
    print("1.显示联系人")
    print("2.新建联系人")
    print("3.查找联系人")
    print()
    print("0.退出系统")
    print("*" * 30)

# 显示功能
def show():
    print("-" * 30)
    print("显示联系人")

    if len(cards_list) == 0:
        print("无联系人,请添加联系人!")
        return

    for name in ["姓名", "电话", "QQ"]:
        print(name, end="\t\t")
    print()
    print("=" * 30)

    for cards_dict in cards_list:
        print("%s\t\t%s\t\t%s\t\t" % (cards_dict["name"],
                                      cards_dict["phone"],
                                      cards_dict["QQ"]))

# 添加功能
def new():
    print("-" * 30)
    print("新建联系人")
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入QQ:")

    cards_dict = {"name": name,
                  "phone": phone,
                  "QQ": qq}

    cards_list.append(cards_dict)
    # print(cards_list)
    print("联系人添加成功!")

# 查询功能
def find():
    print("-" * 30)
    print("查找联系人")

    find_name = input("请输入姓名:")

    for cards_dict in cards_list:
        if find_name == cards_dict["name"]:
            print("姓名\t\t电话\t\tQQ\t\t")
            print("=" * 30)
            print("%s\t\t%s\t\t%s\t\t" % (cards_dict["name"],
                                      cards_dict["phone"],
                                      cards_dict["QQ"]))
            print("=" * 30)

            change(cards_dict);

            break
    else:
        print("未找到%s联系人!" % find_name)


# 修改功能
def change(find_dict):

    A = input("请输入要进行的操作:"
              "[1] 修改内容 [2] 删除内容 [0] 返回上一步 ")

    if A == "1":
        # 修改
        find_dict["name"] = change_input(find_dict["name"],"姓名: ")
        find_dict["phone"] = change_input(find_dict["phone"],"电话: ")
        find_dict["QQ"] = change_input(find_dict["QQ"],"QQ: ")
        print("修改完成!")

    if A == "2":
        # 删除
        cards_list.remove(find_dict)
        print("联系人已删除!")


# 输入修改,回车不变
def change_input(dict_str,input_str):

    temp_str = input(input_str)

    if len(temp_str) > 0:
        return  temp_str
    else:
        return dict_str
