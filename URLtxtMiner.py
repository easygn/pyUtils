##############################
# Webpage text URL mining and exporter
# remade by Easygn , April 22, 2F
# prototype code gen by Claude3 Ai sonnet
#####


FIND_KWD = '?q=JohnDoe'
TARGET_FILE = 'a.html'
EXPORT_FILE = 'out.txt'


file = open(TARGET_FILE, 'r', encoding='utf-8')

txt = file.read()


wrFile = open(EXPORT_FILE, 'w', encoding='utf-8')
for line in txt.split('\n'):
    if FIND_KWD in line:
        wrFile.write(line[line.find('http'):line.find(FIND_KWD)+len(FIND_KWD)] + '\n')
print('Done')