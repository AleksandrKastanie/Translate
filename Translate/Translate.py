from module1 import* 
ENG=[]
RUS=[]
RUS=read_file("rus.txt", RUS)
print(RUS)
print() 

ENG=read_file("eng.txt", ENG)
print(ENG)
print()

while True: 
    menu=input("Speak - S, \nAll Words -A, \nTranslate -T, \nNew words -N, \nMistackes -M, \nExamen -E, \nThe End -E")