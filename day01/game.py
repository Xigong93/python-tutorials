# encoding=utf-8
# 成语接龙游戏
import random
import time

__author_ = "pokercc<pokercc@sina.com>"
import os


def create_chengyudaquan():
    """
    创建成语字库
    :return:
    """
    chengyu_list = []
    with open("成语大全（31648个成语解释）.Txt", encoding='utf-8')as fp:
        for line in fp.readlines():
            if line.strip() and "拼音" in line:
                _chengyu = line[:line.index("拼音")]
                chengyu_list.append(_chengyu.strip())

    print(chengyu_list)
    print(f"成语数量:{len(chengyu_list)}")
    with open("成语大全.txt", encoding='utf-8', mode='w')as fp:
        # fp.write(os.linesep.join(chengyu_list))
        fp.writelines(chengyu_list)


def start_game():
    chengyu_list = None
    with open("成语大全.txt", encoding='utf-8')as fp:
        chengyu_list = [line.strip() for line in fp.readlines()]
    print(f"欢迎来到成语接龙挑战赛!")
    print(f"我是主持人王小丫，我知道{len(chengyu_list)}条成语")
    # word = input()
    print("我先开始，给我两秒钟...")
    time.sleep(1)
    # 随机取一个成语
    random_index = random.randint(0, len(chengyu_list) - 1)
    machine_word = chengyu_list[random_index]

    count = 0
    while True:
        print(f"王小丫:{machine_word}")
        while True:
            person_word = input("王小丫:请接龙:(答不出来，输入`c`结束游戏)\n").strip()
            if person_word.lower() == 'c':
                if count >= 3:
                    print(f"王小丫:你真棒!你已经答对{count}轮,这次挑战失败没关系，欢迎再来挑战!")
                else:
                    print("很遗憾您放弃了比赛,欢迎再来挑战!")
                exit(0)
            elif person_word not in chengyu_list:
                # 你说的成语，在成语库里没有
                print(f'王小丫:抱歉，你说的成语"{person_word}",我没听说过!')
            elif person_word[0] != machine_word[-1]:
                # 你说的成语，接龙接不上
                print(f'王小丫:你说的"{person_word}"和我说的"{machine_word}",收尾接不上，请你再说一个别的成语!')
            else:
                count += 1
                # 查找匹配的成语列表
                match_words = [w for w in chengyu_list if w.startswith(person_word[-1])]
                if match_words:
                    # 有匹配的
                    machine_word = match_words[0]
                    break
                else:
                    # 没有匹配的
                    print(f"王小丫:我答不出来,恭喜你赢了，一共接上{count}轮")


start_game()
# create_chengyudaquan()
