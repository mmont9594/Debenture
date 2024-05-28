import pandas as pd
import glob

def carregar_tratar_info_registros_consolidados(Ativo:str):
    """ 
    Carregar informações dos Registros Consolidados por Ativos
    Tratar as informações, e salvar num data.frame
     
    :param Ativo: Escolher qual ativo será trabalhado ~ DEB, CRI, CRA, LIG, COE, LF, CFF, NC, LFSN, LFSC 
    :type Ativo: str
    
    """
    registros_files = glob.glob("Files/Registro*") # Busca dos arquivos que contém a palavra inicial Registro
    df_registros_list = []
    
    for reg_file in registros_files:
        aux_reg = pd.read_csv(reg_file, sep=';', skiprows=4, decimal=',')
        aux_reg = aux_reg.rename(columns={
            'Volume Financeiro (R$)': 'Vol.Fin',
            'Código IF': 'Codigo.IF',
            'Código ISIN': 'Codigo.ISIN',
            'Data Liquidação': 'Dt.Liquidacao',
            'Quantidade Negociada': 'Qtd.Negociada',
            'Preço Mínimo': 'Preco.Min',
            'Preço Médio': 'Preco.Med',
            'Preço Máximo': 'Preco.Max',
            'Último Preço': 'Ultimo.Preco',
            'Preço de Referência': 'Preco.Ref',
            'Número de Negócios':'Num.Negocios',
            'Oscilação':'Oscilacao'
        })
    
        aux_reg['file_date'] = pd.to_datetime(
            reg_file.replace('Files\\Registros Consolidados-', '').split('.')[0],
            format='%d-%m-%Y'
        )
        aux_reg = aux_reg[aux_reg['Instrumento Financeiro'] == Ativo]
        
        aux_reg['Qtd.Negociada'] = pd.to_numeric(aux_reg['Qtd.Negociada'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
        aux_reg['Dt.Liquidacao'] = pd.to_datetime(aux_reg['Dt.Liquidacao'], format='%d/%m/%Y')
        aux_reg['Preco.Min'] = pd.to_numeric(aux_reg['Preco.Min'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
        aux_reg['Preco.Med'] = pd.to_numeric(aux_reg['Preco.Med'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
        aux_reg['Preco.Max'] = pd.to_numeric(aux_reg['Preco.Max'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
        aux_reg['Preco.Ref'] = pd.to_numeric(aux_reg['Preco.Ref'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
        aux_reg['Ultimo.Preco'] = pd.to_numeric(aux_reg['Ultimo.Preco'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
        aux_reg['Vol.Fin'] = pd.to_numeric(aux_reg['Vol.Fin'].str.replace('.', '').str.replace(',', '.'), errors='coerce')
        aux_reg['Num.Negocios'] = pd.to_numeric(aux_reg['Num.Negocios'], errors='coerce')
        aux_reg['Oscilacao'] = pd.to_numeric(aux_reg['Oscilacao'], errors='coerce')
        
        df_registros_list.append(aux_reg)

    df_registros = pd.concat(df_registros_list, ignore_index=True)
    
    return df_registros