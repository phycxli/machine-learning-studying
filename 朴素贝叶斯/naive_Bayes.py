#根据天气情况决策是否打球 如果给出新一天的气象指标数据: sunny , cool , high , TRUE， 判断一下会不会去打球
#创建训练集
outlook=['sunny','sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy','sunny','overcast','overcast','rainy']
temperature=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
humdity=['high','high','high','high','normal','normal','normal','high','normal','normal','normal','high','normal','high']
windy=['FALSE','TRUE','FALSE','FALSE','FALSE','TRUE','TRUE','FALSE','FALSE','FALSE','TRUE','TRUE','FALSE','TRUE']
play=['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']

o=input('天气：')
t=input('温度：')
h=input('湿度：')
w=input('有无风：')

def wordnum(word,items):
    count=0
    for item in items:
        if item==word:
            count+=1
    return count

def word_condition(word,condition,items):
    count=0
    for i in range(len(items)):
        if items[i]==word and play[i]==condition:
            count+=1
    return count
pyn=wordnum('no',play)/len(play)
pyy=wordnum('yes',play)/len(play)
pon=word_condition(o,'no',outlook)/wordnum('no',play)
poy=word_condition(o,'yes',outlook)/wordnum('yes',play)
ptn=word_condition(t,'no',temperature)/wordnum('no',play)
pty=word_condition(t,'yes',temperature)/wordnum('yes',play)
phn=word_condition(h,'no',humdity)/wordnum('no',play)
phy=word_condition(h,'yes',humdity)/wordnum('yes',play)
pwn=word_condition(w,'no',windy)/wordnum('no',play)
pwy=word_condition(w,'yes',windy)/wordnum('yes',play)
out1=pyn*pon*ptn*phn*pwn
out2=pyy*poy*pty*phy*pwy
if out1>out2:
    out='no'
else:
    out='yes'
print(out)