
# coding: utf-8

# In[ ]:


#1:算出字串中出現的指定字母之間的距離
list1 = input()
target = input()
list1 = list1.upper()#string is immutabe, so upper() will return a new string
target = target.upper()
list(list1)#即使加了這一行但list1的type卻仍然是str, 而且還依舊可以用index去找

list2 = []
for i in range(len(list1)):#'int' object is not iterable:int不可迭代，需要range()
    if list1[i] == target:
        list2.append(i)
for i in range(1,len(list2)):
    a = list2[i]-list2[i-1]
    print(a,end=' ')
#算出曾經出現過的字母的位置
#算出每一次的間隔


# In[22]:


#多行輸入，五個-號結尾。判斷是否為迴文，大小寫視為不同文字，最後輸出YES or NO
w = input()

answer = []
while w != '-----':
    w = list(w)
    a = (len(w)-1)//2
    for i in range(a+1):
        if w[i] == w[len(w)-1-i]:
            if i == a:
                answer.append('YES')
        else:
            answer.append('NO')
            break
    w = input()
    
for n in range(len(answer)):
    print(answer[n])
        


# In[32]:


#太鼓達人: 算得分和最高COMBO數。增加的分數 = COMBO*100, 累加；COMBO數一旦有錯則全部歸零(但得分不歸零)
c = input()
a = input()
list(c)
list(a)
Combo = 0
Score = 0
FinalCombo = 0
for i in range(len(c)):
    if c[i]=='-':
        FinalCombo = max(FinalCombo,Combo)
        continue
    elif c[i]==a[i]:
        Combo += 1
        FinalCombo = max(FinalCombo,Combo)
        Score = Score + Combo*100
    else:
        FinalCombo = max(FinalCombo,Combo)
        Combo = 0
        
print(Score,FinalCombo,end=' ')


# In[8]:


#字串中學堂:輸入字串和其順序，組成完整句子並加上句點
w = input()
Sentence = {}

while w != '0':
    w = w.split(" ")
    Sentence[w[1]] = w[0]
    w = input()
s = sorted(Sentence.keys())
for i in range(len(s)-1):
    #print(Sentence[i],end=' ')#錯誤
    print(Sentence[s[i]],end=' ')
print(Sentence[s[len(s)-1]]+'.')


# In[5]:


a={1:'sunny',3:'nunu',2:'jkj'}
type(a)
b = sorted(a.keys())
for i in range(len(b)-1):
    print(a[b[i]],end = ' ')


