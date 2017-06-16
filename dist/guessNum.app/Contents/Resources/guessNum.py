#coding:utf8

from random import randint

end = 1
while end:
    choice = raw_input('开始游戏请按1；退出游戏请按2\n')
    if choice == '1':
        name = raw_input('请输入你的名字：')

        f = open('gameRecord.txt')
        lines = f.readlines()
        f.close()

        scores = {}
        try:
            for l in lines:
                s = l.split()
                scores[s[0]] = s[1:]
        except:
            pass
        score = scores.get(name)
        if score is None:
            score = [0, 0, 0]

        total = int(score[0])  #记录游戏轮数
        min   = int(score[1])  #猜中答案的最少次数
        times = int(score[2])  #玩的总次数

        if total > 0:
            avg = float(times) / total #avg为平均猜中次数
        else:
            avg = 0

        print '你已经玩了%d轮，最少%d次猜出答案，平均%.2f次猜出答案' % (total, min, avg)

        num = randint(1, 100)
        _time = 0 #每轮猜的次数
        for i in range(1, 11):  # 每轮最多猜十次
            print '请猜一个1到100之间的整数：'

            ans = input()
            if ans < num:
                print '太小了'
                _time +=1

                if i == 10:
                    print '失败！'
                    end = 0
                    break
            elif ans > num:
                print '太大了'
                _time += 1
                if i == 10:
                    print '失败！'
                    end = 0
                    break
            else:
                print '猜中了，本轮游戏结束！请重新开始或退出游戏'
                _time = i
                break

        # 若十次都未猜中，不记录成绩直接退出游戏
        if end == 1:
            if total == 0 or _time < min:
                min = _time
            times += _time
            total += 1

            scores[name] = [str(total), str(min), str(times)]
            result = ''
            for n in scores:
                line = n + ' ' + ' '.join(scores[n]) + '\n'
                result += line

            f = open('gameRecord.txt', 'w')
            f.write(result)
            f.close()

    elif choice == '2':
        end = 0
    else:
        print '请输入正确的数字退出或开始游戏！'



