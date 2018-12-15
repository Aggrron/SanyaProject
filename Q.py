import codecs
list = codecs.open("List.txt", "r", 'utf-8')
ans = codecs.open("Answers.txt", 'r', 'utf-8')


class Question:
    def __init__(self, text, n, a, b, c, d):
        self.text = text
        self.n = n
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.corr = 'а'


def printQuestion(obj):
    print(obj.n)
    print(obj.text)
    print(obj.a)
    print(obj.b)
    print(obj.c)
    print(obj.d)
    print('Correct: ' + str(obj.corr))


def clearSpaces(line):
    i = 0
    for letter in line:
        if letter.isalpha():
            break
        i += 1
    result = line[i:]
    return result


def findNum(line):
    dot_index = line.find('.')
    num = line[:dot_index]
    return int(num)

def findText(line):
    dot_index = line.find('.')
    text = line[dot_index+1:]
    text = clearSpaces(text)
    text = text[0: len(text)-1]
    return text



def findCorr(line, que):
    l = line.split()
    #print(l)
    for i in range(len(l)//2):
        num = int(l[i*2])
        corr = l[(i*2)+1]
        #print(num)
        if corr == 'а':
            que[num-1].corr = 1
        if corr == 'б':
            que[num - 1].corr = 2
        if corr == 'в':
            que[num - 1].corr = 3
        if corr == 'г':
            que[num - 1].corr = 4


question_list = []
i = 0
#Get questions
for line in list:
    if line[0].isdigit():
        num = findNum(line)
        text = findText(line)
    if line[0] == 'а':
        a = findText(line)
    if line[0] == 'б':
        b = findText(line)
    if line[0] == 'в':
        c = findText(line)
    if line[0] == 'г':
        d = findText(line)
        question_list.append(Question(text, num, a, b, c, d))

#Get answers
ans.readline()
for line in ans:
    findCorr(line, question_list)












