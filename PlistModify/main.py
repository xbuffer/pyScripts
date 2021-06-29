import plistlib
import jsonpath

# plist文件路径
PlistPath = "F:\\学习相关文档\\test\\pyScripts\\PlistModify\\"


# 读入数据
# with open(PlistPath + "test.plist", 'rb') as fp:
#     pl = plistlib.load(fp)
#     # 查找指定块
#     plistUpdateurl = jsonpath.jsonpath(pl, '$.PlistInfo.updateUrl')
#     manhuaUrls = jsonpath.jsonpath(pl, '$.Servers[*].mainURL')
#     searchUrl = "https://www.bymanhua.com"
#     index = manhuaUrls.index(searchUrl)
#     # 修改块的指定内容
#     # print(pl['Servers'][index]['serverOnlyID'])
#     pl['PlistInfo']['updateUrl'] = "https://github.com/xbuffer/pyScripts/blob/master/PlistModify/hjmh.plist"
#     # 增加指定内容
#
#     # 保存修改后的内容
# with open(PlistPath + "hjmh.plist", 'wb') as fp:
#     plistlib.dump(pl, fp)

def menu():
    print("操作菜单如下:\n1、增加一条源地址\n2、删除指定源地址\n3、修改指定配置文件\n4、查看配置文件源列表\nq、退出")


def add():
    print("add")


def delete():
    print("del")


def modify():
    print("modify")


def view(fname):
    with open(fname, 'rb') as fp:
        pl = plistlib.load(fp)
        manhuaTitles = jsonpath.jsonpath(pl, '$.Servers[*].title')
        print(manhuaTitles)


if __name__ == '__main__':
    menu()
    choice = input("请输入你的选择\n").lower()
    while (choice != 'q'):
        if (int(choice) == 1):
            add()
        elif (int(choice) == 2):
            delete()
        elif (int(choice) == 3):
            modify()
        elif (int(choice) == 4):
            fname = PlistPath + "hjmh.plist"
            view(fname)

        else:
            print("输入错误！\n")
        menu()
        choice = input("请输入你的选择\n").lower()
