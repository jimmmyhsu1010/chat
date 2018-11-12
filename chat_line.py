
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#清單切割寫法:
#n[開始值：結束值](開始有包含，結束不包含)
#n[:3]可以拿到前三個（開始值是0可以不用寫）
#n[2:4]可以一個清單裝著n[2]跟n[3]
#n[-2:]拿到最後兩個,（結尾值不寫表示到底)

def convert(lines):
    person = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)

        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)

    print('Allen說了', allen_word_count, '個字')
    print('Allen使用了', allen_sticker_count, '個貼圖')
    print('Allen傳了', allen_image_count, '張圖片')
    print('Viki說了', viki_word_count, '個字')
    print('Viki使用了', viki_sticker_count, '個貼圖')
    print('Viki傳了', viki_image_count, '張圖片')
       
    

def write_file(filename, lines):
    with open(filename, 'w',) as f:
        for line in lines:
            f.write(line + '\n')
 

def main():
    lines = read_file('-LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)
main()