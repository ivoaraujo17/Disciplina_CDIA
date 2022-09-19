import pandas as pd


def view_csv(path):
    table = pd.read_csv(path)
    for row in table.index:
        print(f'{table.loc[row, "Nome"]} : {table.loc[row, "Idade"]}')


view_csv(r"C:\Users\ivoar\OneDrive\Documentos\CDIA\Introducao_Ciencia_de_Dados\Teste.txt")
