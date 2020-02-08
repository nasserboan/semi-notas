import pandas as pd
import warnings

warnings.filterwarnings('ignore')

if __name__ == "__main__":
    print('Buscando o arquivo!')

    ## selecionando as colunas que quero
    columns = ['cod_aluno','escola','cod_escola','curso','cod_serie','serie','cod_turno','turno',
    'cod_disciplina','disciplina','bimestre','nota_bimestral']

        ## lendo o arquivo csv utilizando C como linguagem
    df = pd.read_csv('data/raw/dados abertos - desempenho escolar_20180515_160111.csv',
                sep=';',
                encoding='latin-1',
                usecols=columns,
                engine='c')

    ## filtrando somente o que eu quero
    df = df[(df['serie'].isin(['6º Ano','7º Ano','8º Ano','9º Ano'])) & 
            (df['bimestre'] == 'resultado final') & 
            (df['disciplina'].isin(['Matemática']))]

    ## salvando o arquivo
    df.to_csv('data/filtered.csv',index=False)

    print(f'Processo terminado! O arquivo final tem {df.shape[0]} linhas e {df.shape[1]} colunas.')