
lines = []
with open('line_chat_1.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ') #String可以當做清單來切割
    time = s[0][:5]
    name = s[0][5:]
    print(name)
    
