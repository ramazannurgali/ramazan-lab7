import re
with open('row.txt','r', encoding='utf-8') as text:
    data = text.read()
#1
P = r'а*б*'
M = re.findall(P, data)
M = [match for match in M if match.strip()]
for i in M:
    print(i,end = ' ') 

#2
P = r'а*б{2,3}'
M = re.findall(P, data)
M = [match for match in M if match.strip()]
for i in M:
    print(i,end=' ') 

#3
P = r'[а-я]+_[а-я]+'
M = re.findall(P, data)
M = [match for match in M if match.strip()]
for i in M:
    print(i, end=' ') 
    
#4
P = r'[А-Я]{1}[а-я]+'
M = re.findall(P, data, re.MULTILINE | re.DOTALL)
M = [match for match in M if match.strip()]
for i in M:
    print(i,end=', ') 

#5 
P = r'^а.*б$'
M = re.findall(P, data, re.MULTILINE | re.DOTALL)
M = [match for match in M if match.strip()]
for i in M:
    print(i, end=' ')   

#6
ND = re.sub(r' ', ';', data)
print(ND)  


#7
P = r'_(\w)'
U = re.sub(P, lambda x: x.group(0).upper(), data)

RESULT = re.sub(r'_','',U)
print(RESULT)


    
#8
SD = re.split(r'[А-Я]', data)
print(SD) 

#9
RR = re.sub(r'([а-я])([А-Я])',r'\1 \2', data)
print(RR) 
    
#10
def GAME(data):
    W = re.findall(r'[А-Я][а-я]*', data)
    return '_'.join(word.lower() for word in W)

result = GAME(data)
print(result) 
