import functions as f
import pandas as pd
import csv
MSG1="Quants videos vols introduir: "

def main():
    reg=int(input(MSG1))

    with open ('files/dades.csv', 'w' , encoding='utf-8', newline='') as csvfile:
        fieldnames=['Identificador', 'Grup/cantant', 'Nom', 'Data pub.', 'Visualitzacions']
        writeCSV=csv.DictWriter(csvfile, fieldnames= fieldnames)
        writeCSV.writeheader()
        for i in range(reg):
            dictio = f.dades()
            writeCSV.writerow(dictio)

    f.mostrar('files/dades.csv')

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
