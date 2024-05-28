import pandas as pd
import glob

def carregar_tratar_info_titulos_privados(Titulo:str):
    """ 
    Carregar informações dos titulos privados
    Tratar as informações, e salvar num data.frame

    :param Titulo: Escolher qual ativo será trabalhado ~ Debênture, CRI, CRA 
    :type Titulo: str
        
    """    
    private_bonds_info_files = glob.glob("Files/*.xls") # Busca dos arquivos que terminam com a extensão .xls

    df_private_info_list = []
    for file in private_bonds_info_files:
        df_private_info = pd.read_excel(file)
        df_private_info = df_private_info[df_private_info['Tipo'] == Titulo]
        df_private_info = df_private_info.drop(columns=['Nome da operação', 'Expressão do papel', 'Devedor', 'Cedente', 'Lei 12.431', 'Artigo'])
        
        df_private_info = df_private_info.rename(columns={
            'Código': 'Codigo',
            'Remuneração': 'Remuneracao',
            'Emissão': 'Emissao',
            'Série': 'Serie',
            'Expressão do papel': 'ExpressaoPapel',
            'Data da emissão': 'DtEmissao',
            'Data de vencimento': 'DtVencimento',
            'Data início da rentabilidade': 'DtRentabilidadeInicial',
            'Prazo da emissão': 'PrazoEmissao',
            'Prazo remanescente':'PrazoRestante',
            'Resgate antecipado':'ResgateAntecipado'
        })
        
        df_private_info['Taxa'] = df_private_info['Remuneracao'].str.extract(r'(\d+(?:,\d+)?)%')
        df_private_info['Taxa'] = df_private_info['Taxa'].str.replace(',', '.').astype(float)
        df_private_info['Indice'] = df_private_info['Remuneracao'].str.extract(r'([A-Z]+)')
        df_private_info['PrazoRestante'] = pd.to_numeric(df_private_info['PrazoRestante'].str.replace(' dias corridos', '').str.replace('.', ''), errors='coerce')
        df_private_info['DtEmissao'] = pd.to_datetime(df_private_info['DtEmissao'], format='%d/%m/%Y')
        df_private_info['DtVencimento'] = pd.to_datetime(df_private_info['DtVencimento'], format='%d/%m/%Y', errors='coerce')
        df_private_info['DtRentabilidadeInicial'] = pd.to_datetime(df_private_info['DtRentabilidadeInicial'], format='%d/%m/%Y', errors='coerce')
        df_private_info['PrazoEmissao'] = pd.to_numeric(df_private_info['PrazoEmissao'], errors='coerce')
    
        df_private_info_list.append(df_private_info)

    df_private_info = pd.concat(df_private_info_list, ignore_index=True)

    return df_private_info