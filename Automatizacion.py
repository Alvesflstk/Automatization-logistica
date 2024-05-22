from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import PySimpleGUI as sg

class Main:
    def __init__(self,listcomand):
        
        self.listcomand = listcomand
        
        self.config_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.monitoring_actions()

    def config_options(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")

    def inicializacao(self):
        self.driver.get('https://www.google.com/maps')

    def acesar_rols(self):
        try:
            self.roles = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'hArJGc'))
            )
            self.roles.click()
        except Exception as e:
            print(f"Erro ao acessar roles: {e}")

    def seach(self,partida,destino):
        try:
            list_i_rts = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'tactile-searchbox-input'))
            )

            list_i_rts[0].send_keys(f'{partida}')
            list_i_rts[1].send_keys(f'{destino}')
            list_i_rts[1].send_keys(Keys.RETURN)
            
        except Exception as e:
            print(f"Erro ao realizar busca: {e}")

    def meios(self, response):
        try:
            meios_ts = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'OzmNAc'))
            )
            car = meios_ts[1]
            mt = meios_ts[2]

            if response == 1:
                car.click()
            else:
                mt.click()
                
        except Exception as e:
            print(f"Erro ao selecionar meio de transporte: {e}")

    def monitoring_actions(self):
        try:
            self.inicializacao()
            self.acesar_rols()
            self.seach()
            self.meios(1)
            self.meios(2)

            input("Pressione Enter para fechar o navegador...")
        except Exception as e:
            print(f"Erro durante as ações de monitoramento: {e}")
        finally:
            self.driver.quit()
            
            
class Interface:
    def __init__(self):
        self.layout = [
        [sg.Text("Digite seu nome:")],
        [sg.Input(key='-INPUT-')],
        [sg.Button("Saudar"), sg.Button("Cancelar")],
        [sg.Text(size=(40,1), key='-OUTPUT-')]
        ]
        self.configWindow()
        
    def configWindow(self):
        self.window = sg.Window("Sistem Calculate", self.layout)
       
if __name__ == "__main__":
    
    Interface()