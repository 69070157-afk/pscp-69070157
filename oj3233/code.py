'''PRP'''
Winning_lottery = input().split()
me_lottery = input().split()
reward = [0]
Winning_lottery = {
    (Winning_lottery[0],Winning_lottery[1]):1000000,
    Winning_lottery[1]:100000,
    (Winning_lottery[0],Winning_lottery[1][-2:]):1000,
    (Winning_lottery[0],Winning_lottery[1][-3:]):2000,
    Winning_lottery[1][-2:]:100,
    Winning_lottery[1][-3:]:200,
    Winning_lottery[0]:20
}
reward.append(Winning_lottery.get((me_lottery[0],me_lottery[1]),0))
reward.append(Winning_lottery.get(me_lottery[1][-2:],0))
reward.append(Winning_lottery.get(me_lottery[1][-3:],0))
reward.append(Winning_lottery.get(me_lottery[0],0))
reward.append(Winning_lottery.get(me_lottery[1],0))
reward.append(Winning_lottery.get((me_lottery[0],me_lottery[1][-2:]),0))
reward.append(Winning_lottery.get((me_lottery[0],me_lottery[1][-3:]),0))
print(max(reward))
