# Import lib
import pandas as pd

def carregar_info_cia_abertas(exportar=True):
    """ 
    Carregar informações de Companhias Abertas
    
    :param exportar: Exportar arquivo 
    :type exportar: bool
    
    """
    ## Companhias abertas
    
    cia_abertas = pd.read_csv('Files/cad_cia_aberta.csv', sep=';', encoding='latin1')
    
    if exportar:
        cia_abertas.to_excel('cia_abertas.xlsx', sheet_name="Cia", index=False)
    
    return(cia_abertas)