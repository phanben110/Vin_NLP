import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> PROPERN | DET NOM | PRON
VP -> ADVP V NP PP | V VP | V NP | ADVP V NP | V NP NP| V PP
ADVP -> ADV
PP -> P NP
DET -> Q | CD |
ADJP -> ADJ | ADVP ADJ| ADJ ADVP
NOM -> N | N N ADJP | UN N 
	
PROPERN -> 'nam' | 'lan' | 'Nam' | 'Lan'
PRON -> 'nó' | 'Nó'
V -> 'đọc' | 'thích' | 'có' | 'mua' | 'tặng'|'ở'
P -> 'ở'
N -> 'sách' | 'thư_viện' |'cuốn'
UN -> 'cuốn'
Q -> 'nhiều'
ADV -> 'rất' | 'mới' | 'đang' | 'hay' |'mua'
ADJ -> 'hay' | 'mới'| 'nhiều'
CD -> 'một' | 'hai'
""")
# phân tích cú pháp với theo top-down
nltk.app.rdparser() # top-down
#phân tích cú pháp theo bottom-up
nltk.app.srparser() # bottom-up
# đọc file chứa câu ngữ liệu. Đặt file cùng thư mục và đặt tên là text.txt
file1 = open('text.txt', 'r', encoding="utf8")
Lines = file1.readlines()
# xử lý từng câu
for line in Lines:
    sentence = line.split()
    print(sentence) 
    def parse(sent):
        a = []
        parser = nltk.ChartParser(grammar) #ChartParser
        for tree in parser.parse(sent):
           a.append(tree)
        return(a[0])
    print(parse(sentence))
    parse(sentence).draw()