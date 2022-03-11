import pandas as pd
MSG1="Identificador:"
MSG2="Grup/Cantant:"
MSG3="Nom cançó:"
MSG4="Data publicació:"
MSG5="Nombre de visualitzacions: "

def dades():
    dicti=dict()
    dicti["Identificador"] = int(input(MSG1))
    dicti["Grup/cantant"] = input(MSG2)
    dicti["Nom"] = input(MSG3)
    dicti["Data pub."] = input(MSG4)
    dicti["Visualitzacions"] = int(input(MSG5))
    return dicti
'''
def vale_num():
    if ident!=int :
        print ("no")


'''

def mostrar(csv):
    df=pd.read_csv(csv)
    print(df)
