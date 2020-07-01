# 游戏'''
# 1 选择人物
# 2 购买武器 金币
# 3.打仗 赢金币
# 4 选择删除武器
# 5 查看武器
# 6 退出游戏
# '''
import random
print('欢迎来到王者荣耀')

role = input('请选择游戏人物:(1.鲁班 2.后羿 3.李白 4.孙尚香 5.貂蝉 6.诸葛亮):')

coins = 1000
weapons = [['屠龙刀', 500], ['樱花枪', 400], ['98k', 1000],
           ['加特格林', 800], ['光剑', 150], ['鹅毛扇', 600]]

weapon_list = []  # 保存武器的容器
print('欢迎 !{0}来到"王者荣耀",当前金币是{1}.'.format(role, coins))

while True:
    choice = input('\n请选择:\n1.购买武器\n2.打仗\n3.丢弃武器\n4.查看武器\n5.推出游戏 \n')
    if choice == '1':
        # 购买武器功能
        print('欢迎进入武器仓库:')
        weapons = [['屠龙刀', 500], ['樱花枪', 400], ['98k', 1000],
                   ['加特格林', 800], ['光剑', 150], ['鹅毛扇', 600]]
        for weapon in weapons:  # 遍历列表
            print(weapon[0], weapon[1], sep='   ')
        # 输入要买的武器
        weaponname = input('请输入要购买的武器名称:')
        # 判断 1.原来有没有买过 2.输入的武器是否在武器库里
        if weaponname not in weapon_list:
            # 输入的武器是否在武器库里
            for weapon in weapons:
                if weaponname == weapon[0]:
                    # 存在 购买武器
                    if coins >= weapon[1]:
                        coins -= weapon[1]
                        weapon_list.append(weapon[0])  # 添加到自己的武器库
                        print('{}购买武器:{}成功!'.format(role, weaponname))
                        break
                    else:
                        print('金币不足,滚去刷图!')
                        break

            else:
                print('输入武器名称错误!')
        else:
            print('已经拥有此武器')

    elif choice == '2':
        # 打仗  假设背包里有多个武器
        print('进入战场.....')

        # 判断有没有武器
        if len(weapon_list) > 0:
            # 选择武器
            for weapon in weapon_list:
                print(weapon)

            while True:
                weaponname = input('请选择:')
                #
                if weaponname in weapon_list:
                    # 进入战斗(默认与张飞对战):
                    ran1 = random.randint(1, 20)  # 张飞
                    ran2 = random.randint(1, 20)  # role

                    # 战力进行比较
                    if ran1 > ran2:  # 张飞随机数大于
                        print('此举对战:张飞胜利!!!')

                    elif ran1 < ran2:
                        print('此举对战{}胜利'.format(role))
                        coins += 200  # 获胜获得
                        print('金币数量是{}'.format(coins))
                    else:
                        print('平局,可以再次对战')

                    break
                else:
                    print('武器不存在,请重新选择')
        else:
            print('还没有购买武器,赶快使用金币去购买武器去')

    elif choice == '3':
        # 删除武器
        print('武器太多,很沉,扔几个.....')
        print('{}拥有的武器如下:'.format(role))
        if len(weapon_list) > 0:
            for weapon in weapon_list:
                print(weapon)

            while True:
                weaponname = input('请选择要删除的武器名称:')
                if weaponname in weapon_list:
                    # 删除武器
                    weapon_list.remove(weaponname)
                    # 扔掉武器默认归还金币
                    for weapon in weapons:  # [['98k',1000],[]....]
                        if weaponname == weapon[0]:
                            coins += weapon[1]
                            break  # 控制for循环

                    break  # 控制while循环
                else:
                    print('武器名称有误')
        else:
            print('你都没有武器,还沉啥呀,赶快购买去吧')

    elif choice == '4':
        # 遍历武器
        print('{}拥有的武器如下:'.format(role))
        for weapon in weapon_list:
            print(weapon)
        print('总金币有', coins)
    elif choice == '5':
        answer = input('确定要离开游戏吗(yse no)')
        if answer != 'no':
            print('game over!')
            break
    else:
        print('输入错误,请重新选择')
