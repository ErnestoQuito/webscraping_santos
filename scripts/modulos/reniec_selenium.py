from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Reniec:
    link: str
    
    driver = None
    
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def abrir_web(self):
        self.driver.get(self.link)
    
    def establacer_user(self, user: str):
        in_user = self.driver.find_element_by_id('vusuario')
        in_user.send_keys(user)
        
    def establecer_password(self, password: str):
        in_pass = self.driver.find_element_by_id('vclave')
        in_pass.send_keys(password)

    def acceder(self):
        self.driver.find_element_by_xpath("//input[@value='Acceder']").click()

    def ingresar_documento(self, documento: str):
        in_documento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='dni']"))
        )
        in_documento.send_keys(documento)
    
    def buscar_documento(self):
        self.driver.find_element_by_xpath("//input[@value='Buscar']").click()
    
    def existe_documento(self):
        try:
            self.driver.find_element_by_class_name("mensaje").text
            return False
        except:
            return True
    
    def obtener_campos(self):
        campos = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
        )
        return campos

    def ir_datos_padres(self):
        self.driver.find_element_by_class_name('tablinks').click()
    
    def ir_nueva_consulta(self):
        self.driver.find_element_by_xpath("//input[@value='Nueva Consulta']").click()
    
    def obtener_campos_texto(self) -> list:
        campos_texto = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'textarea'))
        )
        return campos_texto

    def obtener_img_alt(self, alt: str):
        in_documento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//img[@alt='{alt}']"))
        )
        return in_documento

    def cerrar_web(self):
        if self.driver:
            self.driver.quit()
