from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle

# Primeira etapa conseguir a sessão do Operador

# Aqui seto um objeto do tipo Options do Chrome
options = Options()
# Aqui seto um caminho para salvar a informação
options.add_argument("--user-data-dir=/home/ubuntu/Desktop/chrome-data")

# Aqui seto Driver de navegação
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com')
# Esperar a requisição carregar
time.sleep(40)

# Essa parte diferente do que já utilizei antes, ela vai pegar a minha sessão do what
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
time.sleep(30)
# Fechar driver
driver.quit()
