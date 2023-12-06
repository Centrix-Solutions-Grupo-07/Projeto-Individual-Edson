import time
import pickle
import re
import nltk
import string
import mysql.connector
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from datetime import datetime
# //PARA DEPOIS//
#from nltk.stem import PorterStemmer
# //PARA DEPOIS//

# Adicionais necessários
nltk.download('punkt')
nltk.download('stopwords')
stopwords_portuguese = set(stopwords.words('portuguese'))

# //PARA DEPOIS//
# Palavras de exemplo
# palavras = ['burro', 'burra', 'burros', 'burrice']

# Inicializar o Stemmer
# stemmer = PorterStemmer()

# Realizar stemming para as palavras
# stemmed_palavras = [stemmer.stem(palavra) for palavra in palavras]

#print(stemmed_palavras)

# //PARA DEPOIS//

def funcao_BancoDados(grosseria_monitoramento):
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="TomboySupremacy2!",
        database="centrix"
    )
    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    #Dados para popular o Banco
    dataset = ['bobo', 'obviamente','óbvio','não sei','obviamente', 'óbvio','não sei','obviamente', 'óbvio','não sei', 'não posso ajudar','obviamente', 'óbvio','não sei', 'não posso ajudar', 'espera','obviamente', 'óbvio','não sei', 'não posso ajudar', 'espera','obviamente', 'óbvio', 'tá bom', 'não sei', 'não posso ajudar', 'espera','obviamente', 'óbvio', 'tá bom', 'não sei', 'não posso ajudar', 'espera','bobo', 'obviamente', 'óbvio', 'tá bom', 'não sei', 'não posso ajudar', 'espera','bobo', 'obviamente', 'óbvio', 'tá bom', 'não sei', 'não posso ajudar', 'espera','bobo', 'obviamente', 'óbvio', 'tá bom', 'não sei', 'não posso ajudar', 'espera']

    # Agora vamos inserir na tabela
    for item in dataset:
        # Verifica se já existe um registro com esse mesmo valor
        query_verificar = "SELECT palavraGrossa, quantidadeTotalAtual,dataMonitoracaoAtual FROM grosseria WHERE palavraGrossa = %s"
        cursor.execute(query_verificar, (item,))
        resultado = cursor.fetchone()
        
        # Se o valor já existir
        if resultado:
            grosseria_existente = resultado[0]
            quantidadeTotal_anterior = resultado[1]
            dataMonitoracao_anterior = resultado[2]
            # Consulta para verificar o mês atual no banco de dados
            query_verificar_mes = "SELECT MONTH(dataMonitoracaoAtual) AS mesMonitoracaoAtual FROM grosseria WHERE palavraGrossa = %s"
            # Executa a primeira consulta para obter o mês no banco de dados
            cursor.execute(query_verificar_mes, (grosseria_existente,))
            resultado = cursor.fetchone()
            
            if resultado:
                mes_monitoracao_atual = resultado[0]

                # Obtém o mês atual
                mes_atual = datetime.now().month

                # Se o mês no banco de dados for diferente do mês atual
                if mes_monitoracao_atual != mes_atual:
                    # Executa o update nos campos relacionados ao mês passado
                    query_atualizacao_passado = "UPDATE grosseria SET quantidadeTotalPassado = quantidadeTotalAtual,dataMonitoracaoPassado = dataMonitoracaoAtual WHERE palavraGrossa = %s"
                    cursor.execute(query_atualizacao_passado, (grosseria_existente,))
            # Atualiza a quantidadeTotal com o valor atual + 1
            query_atualizar = "UPDATE grosseria SET quantidadeTotalAtual = %s,dataMonitoracaoAtual = NOW() WHERE palavraGrossa = %s"
            cursor.execute(query_atualizar, (quantidadeTotal_anterior + 1,grosseria_existente))
        else:
            # Insere um novo registro
            query_inserir = "INSERT INTO grosseria (palavraGrossa, quantidadeTotalAtual, dataMonitoracaoAtual) VALUES (%s, %s, '2023-11-03 16:34:22')"
            cursor.execute(query_inserir, (item, 1))
            
            # Insere com base no monitoramento
        if len(grosseria_monitoramento) > 0:
            for item in grosseria_monitoramento:
                # Verifica se já existe um registro com esse mesmo valor
                query_verificar = "SELECT palavraGrossa, quantidadeTotal FROM grosseria WHERE palavraGrossa = %s"
                cursor.execute(query_verificar, (item,))
                resultado = cursor.fetchone()
                
                # Se o valor já existir
                if resultado:
                    grosseria_existente = resultado[0]
                    quantidadeTotal_anterior = resultado[1]
                    dataMonitoracao_anterior = resultado[2]
                    # Consulta para verificar o mês atual no banco de dados
                    query_verificar_mes = "SELECT MONTH(dataMonitoracaoAtual) AS mesMonitoracaoAtual FROM grosseria WHERE palavraGrossa = %s"
                    # Executa a primeira consulta para obter o mês no banco de dados
                    cursor.execute(query_verificar_mes, (grosseria_existente,))
                    resultado = cursor.fetchone()
            
                    if resultado:
                        mes_monitoracao_atual = resultado[0]

                        # Obtém o mês atual
                        mes_atual = datetime.now().month

                        # Se o mês no banco de dados for diferente do mês atual
                        if mes_monitoracao_atual != mes_atual:
                            # Executa o update nos campos relacionados ao mês passado
                            query_atualizacao_passado = "UPDATE grosseria SET quantidadeTotalPassado = quantidadeTotalAtual,dataMonitoracaoPassado = dataMonitoracaoAtual WHERE palavraGrossa = %s"
                            cursor.execute(query_atualizacao_passado, (grosseria_existente,))
                            # Atualiza a quantidadeTotal com o valor atual + 1
                            query_atualizar = "UPDATE grosseria SET quantidadeTotalAtual = %s,dataMonitoracaoAtual = NOW() WHERE palavraGrossa = %s"
                            cursor.execute(query_atualizar, (quantidadeTotal_anterior + 1,grosseria_existente))
                else:
                    # Insere um novo registro
                    query_inserir = "INSERT INTO grosseria (palavraGrossa, quantidadeTotal, dataMonitoracao) VALUES (%s, %s, NOW())"
                    cursor.execute(query_inserir,(item,1))
                    
                conexao.commit()

                cursor.close()
                conexao.close()

def funcao_Monitoramento():

    # Segunda etapa carregar a sessão do Operador

    # Criar um objeto options do tipo Options do Chrome
    options = Options()
    # Adicionar o mesmo argumento que usou para salvar a informação
    options.add_argument("--user-data-dir=/home/ubuntu/Desktop/chrome-data")

    # Criar um objeto driver do tipo webdriver.Chrome usando o options
    browser = webdriver.Chrome(options=options)
    # Abrir o site do WhatsApp Web
    browser.get('https://web.whatsapp.com')
    # Esperar alguns segundos para que o site seja carregado
    time.sleep(35)

    # Carregar os cookies salvos usando o pickle
    cookies = pickle.load(open("cookies.pkl", "rb"))
    # Iterar sobre os cookies e adicionar cada um ao driver
    for cookie in cookies:
        browser.add_cookie(cookie)
    # Recarregar o site
    browser.refresh()
    # Esperar alguns segundos para que o site seja atualizado
    time.sleep(10)

    selecionarConversa = browser.find_elements(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div[1]/div/div/div')
    selecionarConversa[0].click()
    time.sleep(10) # Esperar carregar os elementos da conversa

    # Pegar página atual do Selenium
    html = browser.page_source
    soup = bs(html, 'html.parser')
    ConversasRaw = soup.find(id='app').find(class_='_1Fm4m _1h2dM app-wrapper-web font-fix os-win _13Dep').find(class_='two _1jJ70').text

    # Padrão para identificar número:número
    padrao_numero_numero = re.compile(r'\d+:\d+')

    # Substituir todos os números no formato número:número por uma string vazia
    ConversasRaw_sem_numeros = padrao_numero_numero.sub('', ConversasRaw)

    # Padrão para dividir as mensagens de noite
    padrao_divisao = re.compile(r'PM')
    # Padrão para dividir as mensagens de manhã
    padrao_divisao2 = re.compile(r'AM')
    # Padrão para dividir as mensagens
    padrao_tailIn = re.compile(r'tail-in')
    # Padrão para dividir as mensagens
    padrao_tailOut = re.compile(r'tail-out')
    # Padrão para dividir as mensagens
    padrao_msg = re.compile(r'msg-dblcheck')
    
    # Dividir o texto com base no padrão
    mensagens = padrao_divisao.sub('', ConversasRaw_sem_numeros)

    # Dividir o texto com base no padrão
    mensagens = padrao_divisao2.sub('', mensagens)

    # Dividir o texto com base no padrão
    mensagens = padrao_tailIn.sub('', mensagens)

    # Dividir o texto com base no padrão
    mensagens = padrao_tailOut.sub('', mensagens)

    # Dividir o texto com base no padrão
    mensagens = padrao_msg.split(mensagens)

    # Ignorar a primeira parte do texto (não é uma mensagem) e além disso transforma em uma Lista de Strings
    mensagens = mensagens[1:]

    # Imprimir as mensagens separadas
    # for msg in mensagens:
        # print(msg.strip())
    
    # Juntar as listas de string em 1 única string
    mensagens_ProntoParaToken = ' '.join(mensagens)

    # Tokenização: dividir o texto em palavras
    palavras_Processadas = word_tokenize(mensagens_ProntoParaToken.lower())
    # print(palavras_Processadas)
    # Array de Limpeza
    limpeza = ['dá', 'pa', 'logo']

    # Remover stopwords e pontuações, possivelmente posso fazer um enorme e
    # Remover palavras que não considero úteis para minha ánalise
    palavras_pos_limpeza = [palavra for palavra in palavras_Processadas if palavra not in stopwords_portuguese and palavra not in string.punctuation and palavra not in limpeza]
    print(palavras_pos_limpeza)

    # Lista de palavras (Controle) de Cortesia e de Grosseria
    # cortesias = ['cabelo'] Não usei por enquanto
    grosseiras = ['bobo','obviamente','óbvio','não sei','não posso ajudar', 'tá bom','espera']

    # Criando dicionário de Palavras específicas
    categorias = {
        #'YES': [],   Cortesias
        'NO': []    # Grosserias
    }

    # Iterar pelas frases
    for palavra in palavras_pos_limpeza:
      #  if palavra in cortesias:
      #      categorias['YES'].append(palavra)
        if palavra in grosseiras: # elif
            categorias['NO'].append(palavra)
    grosseria_monitoramento = categorias['NO']

   # print(categorias['YES'])
    print(categorias['NO'])
    
    funcao_BancoDados(grosseria_monitoramento)

    # Contar a frequência das palavras
    # frequencia = FreqDist(palavras_pos_limpeza)

    # Exibir as 10 palavras mais frequentes
    # print(frequencia.most_common(10))

    # frequencia.plot(20)

funcao_Monitoramento()



