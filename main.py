#%%
import pandas as pd
from CadCiaAbertas import carregar_info_cia_abertas
from Registros import carregar_tratar_info_registros_consolidados
from PrivateInfo import carregar_tratar_info_titulos_privados

#%%

def carregar_info_ativos_exportar(Gerar_Excel:bool, exportar:False, Ativo:str, Titulo:str, ):
    """
    Tratar os arquivos e informações sobre cia abertas, 
    registros consolidados dos ativos e informações sobre os titulos privados
    
    :param Gerar_Excel: Gerar os arquivos trabalhados para Excel em diferentes sheets 
    :type Gerar_Excel: bool
    :param exportar: Exportar o arquivo cia Abertas para Excel
    :type exportar: bool
    :param Ativo: Seleciona o Ativo que sera filtrado nos arquivos consolidados
    :type Ativo: str
    :param Titulo: Seleciona o Titulo que sera filtrado nos arquivos consolidados
    :type Titulo: str
    
    """
    # Cia Abertas ----
    
    df_cia_abertas = carregar_info_cia_abertas(exportar=False)
    
    # Registros Consolidados Debentures ----

    df_registro_consolidado = carregar_tratar_info_registros_consolidados(Ativo=Ativo)
    
    # Private Info Debentures ----

    df_private_info = carregar_tratar_info_titulos_privados(Titulo=Titulo)
    
    
    # Join Registros Consolidados + Private Info ----
    #df_private_info_consolidado = pd.merge(df_registro_consolidado, df_private_info, left_on='Codigo.IF	', right_on='Codigo')

    # Output Setup ----
    output_assets_df = [df_cia_abertas, df_registro_consolidado,df_private_info]
    
    if Gerar_Excel:
        excel_file = f'Output/{Ativo}_Info_Consolidadas.xlsx'
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            df_cia_abertas.to_excel(writer, sheet_name='Cia_abertas', index=False)
            df_registro_consolidado.to_excel(writer, sheet_name='Registro_Consolidado', index=False)
            df_private_info.to_excel(writer, sheet_name='Private_Info', index=False)

    print("Private Asset info gerada com sucesso")
    
#%%
carregar_info_ativos_exportar(Gerar_Excel=True, exportar=False, Ativo='DEB', Titulo='Debênture')

