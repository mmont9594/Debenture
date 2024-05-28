## ETL XML ----

# Comentarios adicionais: 
#   1) Query consolida todos os XML no diretorio
#   2) Existe uma diferenca no layout dependendo do tipo de ativo alocado no fundo
#       Sugestao: Exportar um arquivo consolidado tendo consolidacao dos ativos em sheets isoladas, ex: Sheet1: titulos publicos, Sheet2: Titulos Privados, etc...


# Define prep_ambiente function and run
prep_ambiente <- function(instalar_pacotes){

  # Instalar os pacotes abaixo, e carrega-los no seu env ----
  
  # params: instalar_pacotes: bool 
  if(isTRUE(instalar_pacotes)){install.packages(c('dplyr', 'magrittr', 'xml2', 'lubridate', 'writexl'))}
  library(dplyr);  library(magrittr);  library(xml2);  library(lubridate); library(writexl)

  writeLines('Pacotes carregados no seu env: \n dplyr, \n magrittr, \n xml2, \n lubridate ')
    
}

prep_ambiente(instalar_pacotes=FALSE)

# Define xmlFundosETL function and run -----
xmlFundosETL <- function(path, formato='.XML'){
  
  # Lista os ativos que contem .XML num caminho espec�fico ----
  funds_files = list.files(path, pattern = formato)

  # Criar um data.frame zerado ----  
  FundosOutput = data.frame()
  
  # loop para abrir cada XML e obter as informacoes de cada sub-header ----
  for(fund in funds_files){
    
    # Leitura do XML file ----
    xml_data <- read_xml(paste(path, fund, sep=''))
    
    # Extrai tudo que se encontra dentro do Elemento Fundo do XML ----
    content_header <- xml_find_all(xml_data, "//fundo")
    
    # Extrai valores unicos dos sub-headers para o looping ----
    sub_headers <- content_header %>% xml_children() %>% xml_name() %>% unique()
    
    ativos = list()
    
    # Looping por cada sub-heder para obter o conteudo em cada item ----
    for(header_name in sub_headers){
      print(header_name)
      itens <- xml_find_all(content_header, paste(".//", header_name,sep=''))
      df_colname <- itens[1] %>% xml_children() %>% xml_name()
      df_ativo <- data.frame(matrix(ncol = length(df_colname), nrow = 0))
      
      for(item in itens){
        values = (item %>% xml_children() %>% xml_text())[1:length(df_colname)] %>% data.frame(row.names = NULL) %>% t()
        df_ativo = rbind(df_ativo, values)
        
      }
      
      colnames(df_ativo) <- df_colname
      df_ativo['Tipo'] = header_name
      ativos[[header_name]]<- df_ativo
      rm(df_ativo);rm(df_colname)
    }
    
    # Consolida o resultado de cada sub-header do XML para depois juntar com todos os arquivos no objeto FundosOutput ---- 
    consolidado = dplyr::bind_rows(ativos) %>% 
      dplyr::mutate(data = lubridate::ymd(ativos$header$dtposicao),
                    fundo = ativos$header$nome)
    
    FundosOutput = dplyr::bind_rows(FundosOutput, consolidado)
    
    rm(consolidado)
    
  }
  
  # Convertendo os formatos dos dados para gerar o XLSX final ----
  FundosOutput = FundosOutput %>% 
    dplyr::mutate(quantidade = as.double(quantidade),
                  dtemissao  = lubridate::ymd(dtemissao),
                  dtoperacao = lubridate::ymd(dtoperacao),
                  dtvencimento = lubridate::ymd(dtvencimento),
                  qtdisponivel = as.double(qtdisponivel),
                  qtgarantia = as.double(qtgarantia),
                  pucompra = as.double(pucompra),
                  puvencimento = as.double(puvencimento),
                  puposicao = as.double(puposicao),
                  puemissao = as.double(puemissao),
                  principal = as.double(principal),
                  tributos = as.double(tributos),
                  valorfindisp = as.double(valorfindisp),
                  valorfinemgar = as.double(valorfinemgar),
                  coupom = as.double(coupom),
                  percindex = as.double(percindex),
                  percprovcred = as.double(percprovcred)
    ) 
  
  # Exportar para Excel o arquivo Final ----
  writexl::write_xlsx(FundosOutput, path = 'Consolidado_XML_Fundos.xlsx')
  
  writeLines(paste('ETL concluido!\n  Base de Fundos consolidada exportada path:\n', getwd(), sep='  '))
}

xmlFundosETL(path = '<Definir_Path>', formato = '.XML')