
# coding: utf-8

# In[3]:


#Homework1.1
#input處理，將輸入的值對應到三個變數中(cookies, choco, cakes)
cookies = int(input())
choco = int(input())
cake = int(input())
#對尚未兌換贈品的數量進行計算: 10 coolies->1choco, 5choco->1cake利用商數
if(cookies>=10):
    choco = choco + cookies//10
if(choco >= 5):
    cake = cake + choco//5
#format, 將三者欄位和值對齊
print("{:^s}\t{:^s}\t{:^s}".format("Cookies","Chocos","Cakes"))
print("{:<}\t{:<}\t{:<}".format(cookies,choco,cake))


# In[2]:


#Homework 1.2 金融卡號碼，不滿16位數者在前面補0
number = int(input())
print("{:0>16d}".format(number))


# In[ ]:


#Homework 1.3 分組分辨組員或組長: N個人按照座號一組，號碼最大者為該組組長，其餘則為組員
denominator = int(input())
nominator = int(input())
team = nominator//denominator
remainder = nominator%denominator

if remainder > 0:
    team = team+1
    print("member of team %d "%team)
else:
    print("leader of team %d "%team)


# In[2]:


#plus:compare two places' temperature
A = input()
B = input()
l1=A.split(',')
l2=B.split(',')
l1[1]=float(l1[1])
l2[1]=float(l2[1])
l2[1]= 5/9*(l2[1]-32)
if l1[1] < l2[1]:
    print(l2[0])
else:
    print(l1[0])

