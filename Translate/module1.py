def read_file(f:str,l:list):
    """
    Info failist f listisse l
    """
    fail=open(f,"r", encoding="utf-8-sig")# r -просмотр
    for rida in fail:
        l.append(rida.strip()) #'\n'
    fail.close()
    return l

def fail_saver(f:str,l:list):
    """
    loetelu salvaestame failisse 
    """
    fail=open(f,'w') ## w - перезапись
    for el in l:
        fail.write(el+'\n')
    fail.close

def rida_salvestamine(f:str, rida:str):
    """
    Üks sõna või lause(rida) salvestame failisse
    """
    fail=open(f,'a')## Дозапись
    fail.write(rida+'\n')
    fail.close()
def uus_sõna(f:str,rida:str)-> list:
    """
    Lisame uus sõna failisse ja listisse 
    """
    mas=[]
    with open(f,'a',encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
    l=read_file(f)
    return l 