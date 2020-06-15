from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

def getMessage():
    text = str(input("Digite a Mensagem: "))
    text = text.replace(',', '%2C')
    text = text.replace(' ', '%20')
    text = text.replace('?', '%3F')
    return text

def sendMessage(valores, text, option):
    i = 0
    for num in valores:
        browser.get("https://web.whatsapp.com/send?phone="+num+"&text="+text)
        try:
            element = WebDriverWait(browser, 30)
            element.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
        except NoSuchElementException as e:
            pass
            #Exceção não tratada: Se o número não existir
        finally:
            send = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)
            if option == 1:
                try: 
                    element = WebDriverWait(browser, 30)
                    element.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
                except NoSuchElementException:
                    pass
                finally:
                    send = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.CONTROL, 'v')
                    try:
                        element = WebDriverWait(browser, 30)
                        element.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div")))
                    except NoSuchElementException:
                        pass
                    finally:
                        send = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div").click()
            time.sleep(3)
            i += 1
            print("({}) Enviado para {}" .format(i, num))
    print("\nEnviado com sucesso para {} pessoas".format(i))
    browser.close()

try:
    phones = open('phone', 'r')
except:
    print("Arquivo 'phone' nao encontrado")
    sys.exit()

numeros = []
for linha in phones:
    numeros.append(linha.replace('\n', ''))

text = getMessage()
option = int(input("\n1 - Com imagem\n2 - Sem imagem\n\nDigite a opção:"))

browser = webdriver.Firefox(executable_path=r'./geckodriver')
browser.get("https://web.whatsapp.com/")
time.sleep(8)

sendMessage(numeros, text, option)