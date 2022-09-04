from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path= r"C:\Users\Jacyara\Documents\bot\geckodriver.exe win64.exe")
        
            
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
    
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        agora_nao = driver.find_element_by_class_name("cmbtv")
        agora_nao.click()
        self.comente_nas_fotos_com_a_hashtag()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        print("Digitando comentário...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1,3))

    def comente_nas_fotos_com_a_hashtag(self):
        i = 0
        while (1):
            
            sorteio_cell = "Link do Sorteio"
            #sorteio_driver = "Link do Sorteio"
            
            sorteios = [
               sorteio_cell
            ]
            sorteio_da_vez = random.choice(sorteios)
            driver = self.driver
            time.sleep(5)
            driver.get(sorteio_da_vez)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                
                names = open('listra.txt' , 'r')
                comments = names.read()
                comments = comments.split()
                
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(1, 20))
               
                pessoa_1 = random.choice(comments)
                pessoa_2 = random.choice(comments)
                pessoa_3 = random.choice(comments)
                marcar_2_pessoas = pessoa_1 + " " + pessoa_2
                marcar_1_pessoa = pessoa_1
                marcar_3_pessoa = pessoa_1 + " " + pessoa_2 + " " + pessoa_3
                #if sorteio_da_vez ==  sorteio_driver:
                    #self.type_like_a_person(marcar_3_pessoa, comment_input_box)
                    #print("Comentei: ", marcar_3_pessoa, " no post: ", sorteio_da_vez)
                if sorteio_da_vez == sorteio_cell:
                    self.type_like_a_person(marcar_2_pessoas, comment_input_box)
                    print("Comentei: ", marcar_2_pessoas, " no post: ", sorteio_da_vez)
               # if sorteio_da_vez == sorteio_cell:
                  #  self.type_like_a_person(marcar_1_pessoa, comment_input_box)
                   # print("Comentei: ", marcar_1_pessoa, " no post: ", sorteio_da_vez)
                time.sleep(random.randint(1, 15))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                i += 1
                print('Vezes comentadas:')
                print(i)
                time.sleep(random.randint(1, 15))
            except Exception as e:
                print(e)
                time.sleep(5)

# Entre com o usuário e senha aqui

nayaneJBot = InstagramBot("login", "Senha")
nayaneJBot.login()