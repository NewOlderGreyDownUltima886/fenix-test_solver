#Добро пожаловать в исходный код!
#Любознательность - наше всё!!!

#1. возвращен requests (+)
#2. есть проверка на ошибки, но не весь пользовательский ввод проверяется достаточно
#3. есть гит (+)
#4. нет парсера ввода номеров тестов
#5. нет тг бота
#6. нет защиты от временного дисконекта (+)
#7. дима пошел нахер (+++)

import os, sys
import re
import requests
import time, random, datetime, timedelta
from bs4 import BeautifulSoup
from urllib.parse import quote
import prikoli

import telebot
from telebot import types, apihelper

QUIT_BOT = False

def set_bot_token(bot_token):
    with open("bot_file", "w+") as file:
        file.write(f" {bot_token}")
    return True 

def get_bot_token():
    try:
        with open("bot_file", "r") as file:
            arr = file.readlines()
            return arr[0].strip()
    except FileNotFoundError:
        return False


while True:
    chose = -1
    try:
        while True:
            time.sleep(1)
            chose = input(f"""
--------------------------------------------------
TELEGRAM-БОТ:
1. Запустить бота
2. Изменить токен
3. Инструкция по получению токена для бота
4. Очистить экран
0. Выйти в главное меню

—>Ваш выбор: """)
            try:
                chose = int(chose)
            except Exception:
                print("Попробуйте еще раз!")
                continue
            if (chose == 1) or (chose == 2) or (chose == 3) or (chose == 0) or (chose == 4):
                break
            else:
                print("Попробуйте еще раз!")
                continue
    except:
        print("Попробуйте еще раз!")
    
    if chose == 3:
        print('''
--------------------------------------------------------
Инструкция по получению токена для тг-бота:
  1. Зайти в тг-бота @BotFather
  2. Нажать на старт
  3. Ввести команду /newbot
  4. Он предложит ввести имя будущего бота, вводите абсолютно любое (например "Бот для тестов")
  5. Дальше он предложит ввести логин бота. Вводите любое сочетание букв, но чтобы в конце оно заканчивалось на "bot" (например: "blablabla_bot" или "ewfewfwefwef_bot"). Этот логин у всех ботов, как и у пользователей, должен быть уникален, и скорее все простые названия уже заняты другими людьми.
  6. Бот пришлет токен (token to access the HTTP API) по-типу "7275770830:AAFfKHMxsуYbc584s2o93VnybVrTiJXXl54". Скопируйте его и вставьте ниже:
  7. Если вдруг удалите это смс с токеном, то отправьте @BotFather команду "/token", укажите своего бота и он пришлет вам его еще раз''')
    elif chose == 4:
        if len(sys.argv) > 1:
            if sys.argv[1] == "1":
                os.system('cls')
        else:
            os.system('clear')
    elif chose == 0:
        QUIT_BOT = True
        quit()
    
    elif chose == 2:
        user_token = input("—>Введите токен (0 - для отмены): ")
        if user_token == "0":
            print("—>Отменён ввода нового токена")
            continue
        if user_token == "":
            print("\nКажется вы ничего не ввели! Как жаль, что мы не смогли договориться. Поробуйте еще раз...")
        TOKEN = user_token
        if user_token != "":
            print(f"—>Спасибо, записал токен \"{user_token}\"...")
        set_bot_token(user_token)
    
    elif chose == 1:
        try:
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            TOKEN = ''
            
            if get_bot_token():
                TOKEN = get_bot_token()
            else:
                print('''
            --------------------------------------------------------
            Кажется вы здесь впервые! Вот вам инструкция:
            1. Зайти в тг-бота @BotFather
            2. Нажать на старт
            3. Ввести команду /newbot
            4. Он предложит ввести имя будущего бота, вводите абсолютно любое (например "Бот для тестов")
            5. Дальше он предложит ввести логин бота. Вводите любое сочетание букв, но чтобы в конце оно заканчивалось на "bot" (например: "blablabla_bot" или "ewfewfwefwef_bot"). Этот логин у всех ботов, как и у пользователей, должен быть уникален, и скорее все простые названия уже заняты другими людьми.
            6. Бот пришлет токен (token to access the HTTP API) по-типу "7275770830:AAFfKHMxsуYbc584s2o93VnybVrTiJXXl54". Скопируйте его и вставьте ниже:
            7. Если вдруг удалите это смс с токеном, то отправьте @BotFather команду "/token", укажите своего бота и он пришлет вам его еще раз
            ''')
                user_token = input("—>Введите токен (0 - для отмены): ")
                if user_token == "0":
                    print("—>Отменён ввода нового токена")
                    continue
                if user_token == "":
                    print("\nКажется вы ничего не ввели! Как жаль, что мы не смогли договориться. Поробуйте еще раз...")
                TOKEN = user_token
                if user_token != "":
                    print(f"—>Спасибо, записал токен \"{user_token}\"...")
                set_bot_token(user_token)

            apihelper.SESSION_TIME_TO_LIVE = 5 * 60
            
            try:    
                bot = telebot.TeleBot(TOKEN)
            except ValueError:
                print("В ТОКЕНЕ ОШИБКА! Попробуйте изменить его...")
                continue
                #user_token = input("Введите токен: ")
                #if user_token == "":
                #    print("\nКажется вы опять ничего не ввели и на этот раз! Как жаль, что мы не смогли договориться. Поробуйте еще раз...")
                #TOKEN = user_token
                #set_bot_token(user_token)
                #quit()
            except Exception as E:
                if "Unauthorized" in str(E):
                    print("В ТОКЕНЕ ОШИБКА! Попробуйте изменить его...")
                    continue
                    #print(f"ВЫ ВВЕЛИ НЕПРАВИЛЬНЫЙ ТОКЕН \"{TOKEN}\"\n—> Поробуйте ещё раз!")
                    #user_token = input("Введите еще раз токен: ")
                    #if user_token == "":
                    #    print("Кажется вы ничего не ввели и на этот раз! Как жаль, что мы не смогли договориться. Поробуйте еще раз...")
                    #TOKEN = user_token
                    #set_bot_token(user_token)
                    #quit()
                else:
                    print(f"!!!!!!!!!!!!!!!\n—> 1 КРИТИЧЕСКАЯ! ОШИБКА! КОТОРУЮ! Я! ВИЖУ! ВПЕРВЫЕ!, СООБЩИ! ОБ! ЭТОМ! АДМИНУ!!!!!!!!!!!!, текст ошибки: {str(E)}")
                    continue
            

            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################



            class FENIX:
                def __init__(self):
                    #Для работы с сессией
                    self.gay_words = prikoli.gay_words
                    self.headers1 = prikoli.headers1
                    self.SessionId=""

                    self.auth_bool = False

                    #главные параметры всего феникса
                    self.num_of_mistakes_ot = 1
                    self.num_of_mistakes_do = 4
                    self.time_to_wait_ot = 420
                    self.time_to_wait_do = 660

                    self.chosen_semestr = -1

                    #для решения тестов
                    #self.reshat_test_ot = -1
                    #self.reshat_test_do = -1
                    self.array_of_num_tests_to_solve = []
                    self.num_of_pred = -1
                    self.list_of_preds = []
                    self.list_of_vsex_testov = []
                    
                    self.array_to_del = []
                    
                
                def get_new_session_id(self):
                    a = requests.get("http://eport.fesmu.ru/eport/eport/Default.aspx", headers=self.headers1)
                    try:
                        set_cookies = str(a.headers["Set-Cookie"]).strip()
                        if "ASP.NET_SessionId" in set_cookies:
                            set_cookies = set_cookies[(set_cookies.find("ASP.NET_SessionId") + 18):(set_cookies.find(';'))]
                            return set_cookies
                    except KeyError:
                        print("Попробуйте с включенным интернетом!")
                        QUIT_BOT = True
                        quit()
                def set_new_session_id(self):
                    self.SessionId = self.get_new_session_id()
                    if self.SessionId != "":
                        return True
                    else:
                        return False
                def get_cookies(self):
                    cookies1 = {
                    "_ym_d":"1746367815",
                    "_ym_uid":"174636781563597601",
                    "_ym_isad":"2",
                    "_ym_visorc":"w",
                    "ASP.NET_SessionId":self.SessionId,
                    }
                    return cookies1


                #Главная функция аутентификации
                def make_a_request(self, url, data, silens=True, streaming=False, num_of_error=0, auth_mode=False, get_request=False):
                    num_of_error=num_of_error
                    try:
                        if get_request == True:
                            a = requests.get(url, headers=self.headers1, cookies=self.get_cookies(), stream=streaming)            #ДЛя GET-запросов
                            time.sleep(0.5)
                        else:   
                            a = requests.post(url, data=data, headers=self.headers1, cookies=self.get_cookies(), stream=streaming) #Для POST-запросов
                            time.sleep(0.5)
                    except Exception as E:
                        print(f'''\n----------------------------ERROR-------------------------------------------''')
                        for x in self.gay_words:
                            if x in str(E):
                                num_of_error += 1
                                num_of_error_vsego = 50
                                if num_of_error <= num_of_error_vsego:
                                    print(f"ПЛОХОЕ ИНТЕРЕНЕТ СОЕДИНЕНИЕ!!! Пробую ещё раз через 10 секунд({num_of_error}/{num_of_error_vsego})...\nGay Word: {x}\n")
                                    try:
                                        for i in range(10):
                                            time.sleep(1)
                                    except KeyboardInterrupt:
                                        print("Хорошо! Перестаю")
                                    
                                    return self.make_a_request(url, data, silens, streaming, num_of_error=num_of_error)
                                else:
                                    print(f"НЕ ПОЛУЧАЕТСЯ АВТОРИЗОВАТЬСЯ, проверьте подключение к интернету!!!\n—————>Выхожу...")
                                    QUIT_BOT = True
                                    quit()  #return False
                        print(f"НЕИЗВЕСТНАЯ ФАТАЛЬНАЯ ОШИБКА, \nописание: {E}\n—————>Выхожу...")
                        QUIT_BOT = True
                        quit() #return False


                    def test_na_diskonekt_izza_istekshey_sessii(a):
                        soup = BeautifulSoup(a.text, 'html.parser')
                        
                        b1 = soup.select('h1[id="ctl00_MainContent_Label1"]')
                        for i in range(len(b1)):
                            if "могут работать только зарегистрированные пользователи" in b1[i].text:
                                print(f"!!!СРАБОТАЛ ДИСКОННЕКТ, ПЕРЕПОДКЛЮЧАЮСЬ: {b1[i].text}")
                                return False
                            
                        b2 = soup.select('script[type="text/javascript"]')
                        for i in range(len(b2)):
                            if "необходима авторизация" in b2[i].text:
                                print(f"!!!СРАБОТАЛ ДИСКОННЕКТ, ПЕРЕПОДКЛЮЧАЮСЬ: {b2[i].text}")
                                return False
                        return True


                    if test_na_diskonekt_izza_istekshey_sessii(a):
                        if silens==False:
                            print("\n\n\n----------------------------------------------------------------------------------1")
                            print(a.status_code)
                            print("----------------------------------------------------------------------------------2")
                            print(a.text)
                        return a
                    else:
                        print(f'''\n----------------------------ERROR-------------------------------------------''')
                        if auth_mode == True:
                            print("Error, неправильный логин или пароль!!!\n—————>Выхожу...")
                            QUIT_BOT = True
                            quit()
                        else:
                            num_of_error+=1
                            num_of_error_vsego = 10
                            if num_of_error <= num_of_error_vsego:
                                print(f"\nСДОХЛА СЕССИЯ {self.get_login()}:{self.get_pass()}!!! Пробую ещё раз через 10 секунд ({num_of_error}/{num_of_error_vsego})")
                                try:
                                    for i in range(10):
                                        time.sleep(1)
                                except KeyboardInterrupt:
                                    print("Хорошо! Перестаю")
                                preres = self.auth()
                                print(f'Try to re-auth: {preres}') 
                                return self.make_a_request(url, data, silens=silens, streaming=streaming, num_of_error=num_of_error, auth_mode=auth_mode, get_request=get_request)
                            else:
                                print("Не получается авторизоваться, проверьте подключение к интернету!!!\n—————>Выхожу...")
                                QUIT_BOT = True
                                quit() #return False


                #Парочка функций для работы с файлами и выводом
                def user_input(self, str1):
                    res = input(str1)
                    if res == "admin":
                        #self.admin()
                        print("\n")
                        return self.user_input(str1)
                    else:
                        return res


                def set_login_pass(self, login1, pass1):
                    with open("pass_file", "w+") as file:
                        file.write(f"{login1}\n{pass1}")
                    return True 
                def get_login(self):
                    try:
                        with open("pass_file", "r") as file:
                            arr = file.readlines()
                            return arr[0].strip()
                    except FileNotFoundError:
                        return False
                def get_pass(self):
                    try:
                        with open("pass_file", "r") as file:
                            arr = file.readlines()
                            return arr[1].strip()
                    except FileNotFoundError:
                        return False




                #Авторизация
                #POST /eport/eport/Default.aspx
                # возвращает тру\фолс
                def auth(self, login1="", password1="", silence=False):
                    if self.set_new_session_id():
                        if silence == False: print(f"Session ID({self.SessionId}) установлен, пытаюсь войти...")
                        if (login1 == "") and (password1 == ""):
                            login1 = self.get_login()
                            password1 = self.get_pass()
                            print(f"Пробую зайти в аккаунт {login1}:{password1}...\n")
                            if (login1 == False) or (password1 == False):
                                print("ERROR, НЕ СУЩЕСТВУЕТ ФАЙЛА С ЛОГИНОМ И ПАРОЛЕМ!!!\n—————>Выхожу...")
                                QUIT_BOT = True
                                quit()
                        else:
                            print(f"Пробую зайти в аккаунт {login1}:{password1}...\n")
                        
                        data_auth = f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKLTM5Mjc2OTQzMQ9kFgJmD2QWAgIDD2QWAgIBD2QWAgIFDw8WAh4EVGV4dAXQAtCX0LAg0YHRg9GC0LrQuCDRg9C90LjQutCw0LvRjNC90YvRhSDQsNCy0YLQvtGA0LjQt9C40YDQvtCy0LDQvdC90YvRhSDQv9C%2B0LvRjNC30L7QstCw0YLQtdC70LXQuSDQvdCwINC%2F0L7RgNGC0LDQu9C1OiA3NzAgIDxiciAvPtCh0YDQtdC00L3QtdC1INCy0YDQtdC80Y8g0LLRi9C%2F0L7Qu9C90LXQvdC40Y8gMSDQt9Cw0LTQsNC90LjRjyDQv9C%2B0YHQu9C10LTQvdC40YUgNTAg0YDQtdC30YPQu9GM0YLQsNGC0LjQstC90YvRhSDRgtC10YHRgtC%2B0LIgMTQg0YHQtdC60YPQvdC0PGJyLyA%2B0KHQtdC50YfQsNGBINC%2F0L7QtNC60LvRjtGH0LXQvdC40Lkg0Log0L%2FQvtGA0YLQsNC70YM6IDYzMWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMWYnd7fFZyValq0x%2B30B7kDIWqfTBgE1HUa5%2Fne5VLQz&__VIEWSTATEGENERATOR=73D4C735&__EVENTVALIDATION=%2FwEdAANykW%2Fz6ZjgBrPJhiB0FU0SUN0eEH6RAZcaSKVdt8S4X7osef1mutGT26WuFCdWwFZsovP8KXv0BZyweEkBDqJpWQ1Mw3YxYEw8xGAX44%2FbtA%3D%3D&ctl00%24MainContent%24UserText={login1}&ctl00%24MainContent%24PassText={password1}&ctl00%24MainContent%24ASPxButton1=&DXScript=1_42%2C1_75%2C2_27"
                        requst1 = self.make_a_request("http://eport.fesmu.ru/eport/eport/Default.aspx", data_auth, auth_mode=True)#, start=True)
                        soup = BeautifulSoup(requst1.text, 'html.parser')
                        
                        b = soup.select('span[id="ctl00_MainContent_Label1"]')
                        if len(b) > 0:
                            if "Здравствуйте" in b[0].text:
                                print("\n--------------------------------------------------")
                                privetstvie = f'\n{str(b[0].text)[:-33]}!'
                                if silence == False:
                                    print(privetstvie)
                                return privetstvie
                            else:
                                print(f"ERROR AUTH (1) < error: {b}")
                                return False
                        print("Ошибка, не получилось войти в аккаунт, попробуйте еще раз!!!")
                        return False
                    else:
                        print("Проверьте подключение к интернету")
                        QUIT_BOT = True
                        quit()

                #Войти в тест с известным num_pred и num_test
                #POST /eport/eport/studtst1.aspx HTTP/1.1
                def enter_current_test(self, num_of_pred=0, num_of_test=0):
                    num_of_pred = str(num_of_pred)
                    num_of_test = str(num_of_test)
                    data_enter_current_test=f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUIOTk1NDMwOTQPZBYCZg9kFgICAw9kFgJmD2QWAgIJD2QWBAIDD2QWAmYPZBYCZg9kFgJmD2QWAgIBDxQrAAUPFgIeD0RhdGFTb3VyY2VCb3VuZGdkZGQ8KwAHAQYPZBAWAgIBAgIWAhQrAAEWAh4PQ29sVmlzaWJsZUluZGV4ZhQrAAEWAh8BAgFkFgBkAgcPZBYCZg9kFgJmD2QWAmYPZBYCAgEPFCsABWRkZDwrAAcBBg9kEBYCZgIBFgIUKwABFgIfAWYUKwABFgIfAQIBZBYAZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjcFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjm6%2BEbUEKpaxmSv00E%2B%2FJiuKcZ%2BYI%2BIkpp3rzk2vaUFAA%3D%3D&__VIEWSTATEGENERATOR=847F47AD&__EVENTVALIDATION=%2FwEdAAeH8wh4QiiJKgOuKnFFkPWbI7ZJDWlRgaefdPW8BTEVtXw%2BikVKJJfrT0ndBbXKBTA39nUTQDb0GEkh6LDT5SpRsAIaIhbklmBqr8w%2BPxD292wBCiQy8HT9gxcspUtWdqpbDCDdUSb6jcSCho5zpwlSvNMTFvzkvoYxtvqO8J0ljItyMFkzxVGQu2RBvSrJ7No%3D&ctl00%24MainContent%24hfPred={num_of_pred}&ctl00%24MainContent%24hfTest={num_of_test}&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2DeletedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2InsertedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel1%24ASPxListBox2=System.Data.DataRowView&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3DeletedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3InsertedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel2%24ASPxListBox3=System.Data.DataRowView&ctl00%24MainContent%24ASPxButton1=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C1_41%2C2_36"
                    a  = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst1.aspx", data_enter_current_test)
                    return a


                ###################################################################################################################
                ####################################################################################################################
                #Выбрать тест из списка и войти в него
                #POST /eport/eport/startstu.aspx HTTP/1.1  - 1 
                #POST /eport/eport/studtst1.aspx HTTP/1.1  - 2
                def print_predmets_and_chose_it_step1(self):
                    #1 - Подгружаем список предметов
                    result = []
                    data_chose_some_test_from_list1 ="------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ToolkitScriptManager1_HiddenField\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__EVENTTARGET\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__EVENTARGUMENT\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__VIEWSTATE\"\x0d\x0a\x0d\x0a/wEPDwUKMTE4NDI1MjM5MQ9kFgJmD2QWAgIDD2QWAmYPFgIeB2VuY3R5cGUFE211bHRpcGFydC9mb3JtLWRhdGEWBgIPD2QWDAIBDw8WAh4EVGV4dAWCAdCX0LTRgNCw0LLRgdGC0LLRg9C50YLQtSAg0KHQotCQ0J3QmNCh0JvQkNCSINCh0KLQkNCd0JjQodCb0JDQktCe0JLQmNCnLCDQstGL0LHQtdGA0LjRgtC1INC90YPQttC90YvQuSDRgNCw0LfQtNC10Lsg0YDQsNCx0L7RgtGLOiBkZAILDw8WAh8BBRw8dGFibGUgY2xhc3M9J21lc3MnPjwvdGFibGU+ZGQCDQ8PFgIfAQXaCTx0YWJsZSBjbGFzcz0nbWVzcyc+PHRyPjx0ZD48YSBocmVmPSdSZWFkTXNnLmFzcHg/aWQ9MjEwMDA2Jz7QlNCXINC6INGC0LXQvNC1IDEzLCAi0J/QsNC70LvQuNCw0YIuINC/0L7QvNC+0YnRjCIsINC30LDRh9C10YIsIDQg0YHQtdC80LXRgdGC0YAuPC9hPjwvdGQ+PHRkPjA0LjA1LjIwMjUgMTU6MDc8L3RkPjx0ZD48aW1nIHNyYz0ncGZpbGUuZ2lmJyBhbHQ9J9CY0LzQtdC10YLRgdGPINCy0LvQvtC20LXQvdC90YvQuSDRhNCw0LnQuycvPjwvdGQ+PHRkPiA8L3RkPjwvdHI+PHRyPjx0ZD48YSBocmVmPSdSZWFkTXNnLmFzcHg/aWQ9MjA5NjUxJz7QniDRgtC10LvQtdCz0YDQsNC8LdC60LDQvdCw0LvQtTwvYT48L3RkPjx0ZD4yOC4wNC4yMDI1IDE1OjA2PC90ZD48dGQ+PC90ZD48dGQ+PHNwYW4gc3R5bGU9ImNvbG9yOiAjMDA4ODAwIj4o0J/RgNC+0YHQvNC+0YLRgCAzMC4wNC4yMDI1IDEyOjAyKTwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD48YSBocmVmPSdSZWFkTXNnLmFzcHg/aWQ9MjA5NDk0Jz7QlNC+0LzQsNGI0L3QtdC1INC30LDQtNCw0L3QuNC1INC00LvRjyDQn9CXIOKEliAxMiwg0KHQlDwvYT48L3RkPjx0ZD4yNS4wNC4yMDI1IDE3OjU5PC90ZD48dGQ+PGltZyBzcmM9J3BmaWxlLmdpZicgYWx0PSfQmNC80LXQtdGC0YHRjyDQstC70L7QttC10L3QvdGL0Lkg0YTQsNC50LsnLz48L3RkPjx0ZD4gPC90ZD48L3RyPjx0cj48dGQ+PGEgaHJlZj0nUmVhZE1zZy5hc3B4P2lkPTIwODY4MSc+0JPQn9C10YDQtdC90L7RgSDQvtGC0YDQsNCx0LDRgtGL0LLQsNC90LjRjyDQt9Cw0L3Rj9GC0LjRjy48L2E+PC90ZD48dGQ+MDguMDQuMjAyNSAxNDo0NDwvdGQ+PHRkPjwvdGQ+PHRkPjxzcGFuIHN0eWxlPSJjb2xvcjogIzAwODgwMCI+KNCf0YDQvtGB0LzQvtGC0YAgMTAuMDQuMjAyNSAyMzoxMSk8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+PGEgaHJlZj0nUmVhZE1zZy5hc3B4P2lkPTIwODYyNCc+0JTQvtC80LDRiNC90LXQtSDQt9Cw0LTQsNC90LjQtSDQtNC70Y8g0J/QlyDihJYxMSwg0KHQlC4gMiDQuiwg0JvQpDwvYT48L3RkPjx0ZD4wNy4wNC4yMDI1IDE2OjE3PC90ZD48dGQ+PGltZyBzcmM9J3BmaWxlLmdpZicgYWx0PSfQmNC80LXQtdGC0YHRjyDQstC70L7QttC10L3QvdGL0Lkg0YTQsNC50LsnLz48L3RkPjx0ZD48c3BhbiBzdHlsZT0iY29sb3I6ICMwMDg4MDAiPijQn9GA0L7RgdC80L7RgtGAIDExLjA0LjIwMjUgMTI6NTgpPC9zcGFuPjwvdGQ+PC90cj48L3RhYmxlPmRkAg8PFCsABg8WAh8BBSPQn9GA0LXQtNGL0LTRg9GJ0LjQuSDRgdC10LzQtdGB0YLRgGRkZGRkPCsABgEAFgIeEVNwcml0ZUNzc0ZpbGVQYXRoBSR+L0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAhEPPCsABQEADxYCHgVWYWx1ZQUBM2RkAhUPDxYCHwEFigLQn9GA0Lgg0L3QtdC+0LHRhdC+0LTQuNC80L7RgdGC0Lgg0YDQsNCx0L7RgtGLINGBINGC0LXRgdGC0LDQvNC4INC40LvQuCDQt9Cw0LTQsNGH0LDQvNC4INC/0YDQtdC00YvQtNGD0YnQuNGFINGB0LXQvNC10YHRgtGA0L7QsiAtINCy0LLQtdC00LjRgtC1INC90YPQttC90YvQuSDRgdC10LzQtdGB0YLRgCwg0LrQu9C40LrQvdC40YLQtSDRjdGC0YMg0LrQvdC+0L/QutGDLCDQt9Cw0YLQtdC8INCy0YvQsdC10YDQuNGC0LUg0L3Rg9C20L3Ri9C5INGA0LDQt9C00LXQu2RkAhEPPCsABQEADxYCHwMFATRkZAITD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWBAILDxQrAAUPFgIeD0RhdGFTb3VyY2VCb3VuZGdkZGQ8KwAHAQYPZBAWAWYWARQrAAEWAh4PQ29sVmlzaWJsZUluZGV4ZmQWAGQCDQ9kFgJmD2QWAmYPZBYCZg9kFgICAQ8UKwAFZGRkPCsABwEGD2QQFgFmFgEUKwABFgIfBWZkFgBkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYSBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTgFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjExBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTMFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b243BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMQUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjIFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b240BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE2BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjAFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xNAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjYFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24zBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTcFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xOQUjY3RsMDAkTWFpbkNvbnRlbnQkQVNQeFBvcHVwQ29udHJvbDEFMGN0bDAwJE1haW5Db250ZW50JEFTUHhQb3B1cENvbnRyb2wxJEFTUHhCdXR0b24xMtz5qfbiMbMeISAR/QvG06v5dpRCChvKqSK05ZSRup7m\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__VIEWSTATEGENERATOR\"\x0d\x0a\x0d\x0a556E0939\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__EVENTVALIDATION\"\x0d\x0a\x0d\x0a/wEdAAsLNa6a+9G22QqI86rItVBI05GkTiFJ5RGCGZo4MFlAWmJX/zM4Fq62BChlnvEOcV3H/Y6Ii2DoqGxCrv3qHaubI7ZJDWlRgaefdPW8BTEVtfksz20s2aJuEs5x2iFvUXC/Cz5d6MynVZDCnI40CgFMDJH1HO5EJDXub4y4Eu52UlPcgdOU1mpwY+veTx5eZwxMbGvsjNRUDd20juN1ZU1pJbOyFoUUWZYCdLvCz9c8nk/PEZpnaVcCpNnaj/+3aAnk78Bg6t2TRTu0+rVkX32c\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hftxdescr\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hftyp\"\x0d\x0a\x0d\x0a0\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hftxt\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hfPred\"\x0d\x0a\x0d\x0a-1\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hfPrep\"\x0d\x0a\x0d\x0a-1\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hfSem\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxTextBox2\"\x0d\x0a\x0d\x0a3\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxButton5\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxTextBox3\"\x0d\x0a\x0d\x0a4\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1WS\"\x0d\x0a\x0d\x0a0:0:-1:50:-10000:0:955px:500px:1\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$ASPxTextBox1\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$ASPxMemo1\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxListBox1DeletedItems\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxListBox1InsertedItems\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxListBox1CustomCallback\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$ASPxListBox1\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxCallbackPanel_ASPxListBox3DeletedItems\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxCallbackPanel_ASPxListBox3InsertedItems\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxCallbackPanel_ASPxListBox3CustomCallback\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$ASPxCallbackPanel$ASPxListBox3\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$FileUpload1\"; filename=\"\"\x0d\x0aContent-Type: application/octet-stream\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"DXScript\"\x0d\x0a\x0d\x0a1_42,1_75,2_27,2_34,2_41,1_68,1_65,2_36,1_41,2_40\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB--\x0d\x0a"
                    a = self.make_a_request("http://eport.fesmu.ru/eport/eport/startstu.aspx", data_chose_some_test_from_list1)
                    soup = BeautifulSoup(a.text, 'html.parser')
                    pred_list = soup.select('table[id="ctl00_MainContent_ASPxPopupControl1_ASPxListBox1_LBT"] > tr > td ')
                    
                    #2 - Выводим список предметов
                    itogoviy_print = ""
                    itogovyi_array = []
                    itogoviy_print += "\n--------------------------------------------------\nДоступные вам тесты:"
                    for i in range(len(pred_list)):
                        num = str(i+1)
                        space = ""
                        if i < 9: space += " "
                        res = f"\t{num}.{space} {pred_list[i].text}"
                        itogoviy_print += res
                        itogovyi_array.append([num, pred_list[i].text])
                    itogoviy_print += "\t0.  Вернуться в меню"
                    print(itogoviy_print)
                    return itogovyi_array
                    #print(itogoviy_print) 

                    #3 - Спрашиваем номер предмета
                    #try:
                    #    num_of_pred = int(self.user_input("\nВыберите предмет из списка: ")) - 1
                    #except ValueError:
                    #    print("hui1")
                    #    return False
                    #if num_of_pred == -1:
                    #    return -1
                    #if (num_of_pred > (len(pred_list)-1)) or (num_of_pred < 0):
                    #    print("hui2")
                    #    return False
                    



                ###################################################################################################################
                ####################################################################################################################    
                def print_tests_of_predmet_by_its_index_and_chose_test_step2(self, num_of_pred):
                    #1 - Подгружаем список тестов
                    data_chose_some_test_from_list2 = f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUIOTk1NDMwOTQPZBYCZg9kFgICAw9kFgJmD2QWAgIJD2QWBAIDD2QWAmYPZBYCZg9kFgJmD2QWAgIBDxQrAAUPFgIeD0RhdGFTb3VyY2VCb3VuZGdkZGQ8KwAHAQYPZBAWAgIBAgIWAhQrAAEWAh4PQ29sVmlzaWJsZUluZGV4ZhQrAAEWAh8BAgFkFgBkAgcPZBYCZg9kFgJmD2QWAmYPZBYCAgEPFCsABWRkZDwrAAcBBg9kEBYCZgIBFgIUKwABFgIfAWYUKwABFgIfAQIBZBYAZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjcFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjm6%2BEbUEKpaxmSv00E%2B%2FJiuKcZ%2BYI%2BIkpp3rzk2vaUFAA%3D%3D&__VIEWSTATEGENERATOR=847F47AD&__EVENTVALIDATION=%2FwEdAAeH8wh4QiiJKgOuKnFFkPWbI7ZJDWlRgaefdPW8BTEVtXw%2BikVKJJfrT0ndBbXKBTA39nUTQDb0GEkh6LDT5SpRsAIaIhbklmBqr8w%2BPxD292wBCiQy8HT9gxcspUtWdqpbDCDdUSb6jcSCho5zpwlSvNMTFvzkvoYxtvqO8J0ljItyMFkzxVGQu2RBvSrJ7No%3D&ctl00%24MainContent%24hfPred={num_of_pred}&ctl00%24MainContent%24hfTest=100&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2DeletedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2InsertedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel1%24ASPxListBox2=System.Data.DataRowView&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3DeletedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3InsertedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel2%24ASPxListBox3=System.Data.DataRowView&ctl00%24MainContent%24ASPxButton1=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C1_41%2C2_36"
                    a2 = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst1.aspx", data_chose_some_test_from_list2)
                    soup = BeautifulSoup(a2.text, 'html.parser')
                    test_num_list = soup.select('table[id="ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3_LBT"] > tr > td[class="dxeListBoxItem_Aqua dxeFTM"]')
                    test_name_list = soup.select('table[id="ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3_LBT"] > tr > td[class="dxeListBoxItem_Aqua dxeLTM"]')
                    
                    new_list_of_persent = [[0 for i in range(len(test_name_list))], [0 for i in range(len(test_name_list))]]
                    
                    #нужно сравнить имена всех тестов поочереди с имеющимися списком большой кучи уже решенных и выбрать тот где больше процент 
                    results_array = self.check_all_results_of_tests_by_num_of_pred(num_of_pred=num_of_pred)
                    for i in range(len(test_name_list)):
                        for j in range(len(results_array)-1): #j += 1
                            j += 1
                            if str(results_array[j][0].text).strip() in str(test_name_list[i].text).strip():
                                #print(f"SOVPADENIE NAIDENO: {str(results_array[j][0].text).strip()}  —>  {str(test_name_list[i].text).strip()}")
                                if int(str(results_array[j][1].text).strip()) >= new_list_of_persent[0][i]: 
                                    new_list_of_persent[0][i] = int(str(results_array[j][1].text).strip())
                                    new_list_of_persent[1][i] = str(results_array[j][0].text).strip()

                    
                    #2 - Выводим список тестов и спрашиваем с какого по какой тест
                    itogoviy_print = ""
                    itogoviy_array = []
                    for i in range(len(test_name_list)):
                        num = str(i+1)
                        
                        space = ""
                        if i < 9: 
                            space += " "
                        
                        if new_list_of_persent[0][i] > 0:
                            if new_list_of_persent[0][i] < 100:
                                persent = " " + str(new_list_of_persent[0][i]) + "%"
                            else:
                                persent = str(new_list_of_persent[0][i]) + "%"
                        elif new_list_of_persent[0][i] == 0:
                            persent = "----"
                        else:
                            persent = "----"

                        num_test = str(test_num_list[i].text)

                        our_len = len(num_test)
                        while our_len < 6: 
                            num_test += " "
                            our_len = len(num_test)
                        
                        name_test = str(test_name_list[i].text).strip()
                        
                        #формируем процент выполненности или невыполненности:
                        res = f"\t{num}.{space} ({persent}) {num_test} | {name_test}\n"
                        itogoviy_print = itogoviy_print + res
                        itogoviy_array.append([num, persent, num_test, name_test])
                    #itogoviy_print += ("\t0.  Вернуться в меню")
                    print("ITOG   :" + itogoviy_print)
                    return [itogoviy_print, itogoviy_array]


                #Выбрать вопрос
                #POST /eport/eport/studtst2.aspx HTTP/1.1
                def select_question(self, num_of_question="1"):
                    data_select_question=f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTUwNzg4NDI2OQ9kFgJmD2QWAgIDD2QWAgIBD2QWAgIDD2QWQgIBDzwrAAQBAA8WAh4FVmFsdWUFUygyKSDQo9GF0L7QtCDQt9CwINCx0L7Qu9GM0L3Ri9C80Lgg0LIg0L%2FQtdGA0LjQvtC%2F0LXRgNCw0YLQuNCy0L3QvtC8INC%2F0LXRgNC40L7QtNC1ZGQCCQ88KwAEAQAPFgIfAAUr0JjQtNC10L3RgtC40YTQuNC60LDRgtC%2B0YAg0YLQtdGB0YLQsCAxMzczNWRkAgsPFCsABA8WAh8ABSvQktCw0Ygg0LvQuNC80LjRgiDQstGA0LXQvNC10L3QuCAxOCDQvNC40L0uZDwrAAwBABYEHglGb3JlQ29sb3IKTx4EXyFTQgIEZGRkAg8PFCsABmRkZGQ8KwAHAQAWBB4LQ3NzRmlsZVBhdGgFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHgpDc3NQb3N0Zml4BQRBcXVhPCsABgEAFgIeEVNwcml0ZUNzc0ZpbGVQYXRoBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAhEPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAITDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCFQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAhcPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIZDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCGw8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAh0PFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIfDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCIQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAiMPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIlDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCJw8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAikPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIrDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCLQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAi8PFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIxDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCMw8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAjUPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAI3DxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCOQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAjsPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAI9DxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCPw8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAkEPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAJDDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCRQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAkcPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAJJDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFiEFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24wNAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjAyBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMDMFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMgUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjMFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b240BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNQUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjYFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b243BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjkFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xMAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjExBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTIFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xMwUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE0BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTUFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xNgUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE3BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTgFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xOQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjIwBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjEFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yMgUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjIzBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjQFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjI2BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjcFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yOAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjI5BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMzDtYe90Z6nu2QDSkLRvblOV03MTQ%2BTm0ytfqvbm%2BoOJjg%3D%3D&__VIEWSTATEGENERATOR=4F4B5F1E&ctl00%24MainContent%24ASPxButton{num_of_question}=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40"
                    a = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst2.aspx", data_select_question)
                    return a
                #Тыкнуть первый и к следующему
                #POST /eport/eport/studtst3.aspx HTTP/1.1
                def check_first_and_next(self,):
                    data_check_first_and_next = "ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTI5MTM5NzM3Nw9kFgJmD2QWAgIDD2QWAmYPZBYCAg8PZBYSAgEPPCsABAEADxYCHgVWYWx1ZQUYKDIpINCf0L7Qt9C90LDQvdC40LUgLSAzZGQCBw88KwAEAQAPFgIfAAUQ0JfQsNC00LDQvdC40LUgMWRkAgkPFCsABA8WAh8ABSvQktCw0Ygg0LvQuNC80LjRgiDQstGA0LXQvNC10L3QuCAxOSDQvNC40L0uZDwrAAwBABYEHglGb3JlQ29sb3IKTx4EXyFTQgIEZGRkAgsPDxYCHgRUZXh0BXombmJzcDvQrdC80L%2FQuNGA0LjRh9C10YHQutC40LUg0LzQtdGC0L7QtNGLINC90LDRg9GH0L3QvtCz0L4g0LjRgdGB0LvQtdC00L7QstCw0L3QuNGPINC40YHQutC70Y7Rh9Cw0Y7RgjombmJzcDsmbmJzcDsgPGJyPmRkAg8PDxYCHwMFHiZuYnNwOzEuINC90LDQsdC70Y7QtNC10L3QuNC1O2RkAhMPDxYCHwMFICZuYnNwOzIuINGN0LrRgdC%2F0LXRgNC40LzQtdC90YI7ZGQCFw8PFgIfAwUhJm5ic3A7My4g0YTQvtGA0LzQsNC70LjQt9Cw0YbQuNGOZGQCGw8PFgIfAwUcJm5ic3A7NC4g0YHRgNCw0LLQvdC10L3QuNC1LmRkAh8PDxYCHwMFGyZuYnNwOzUuINC40LfQvNC10YDQtdC90LjQtWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjA0%2Bk22ByzKq5L7zouSrrJbMziS20QR38bdXSKqlADvvqw%3D&__VIEWSTATEGENERATOR=A8B80323&__EVENTVALIDATION=%2FwEdAAc%2FlZpllc25PN%2BYPogZdEuvCa17vhDUriBurXCsNy590WMU%2Ff8RYiHeDshdCQG6KXsl%2BbxYKsnWKi1oDF%2BSPbsJHS3vs9PY66cqRnl9zzvdQgrZ%2B0y1djOQFJQdjlbLnVhP%2FHXZRS6bBCR%2FaTH01z%2B9bOik%2B0yMqvUzm3kYLHgnd9IAIvs1oV7es8UR7FcUYQ4%3D&ctl00%24MainContent%24hfo1=1&ctl00%24MainContent%24hfo2=0&ctl00%24MainContent%24hfo3=0&ctl00%24MainContent%24hfo4=0&ctl00%24MainContent%24hfo5=0&ctl00%24MainContent%24hf1=0&ctl00%24MainContent%24ASPxButton5=&ctl00%24MainContent%24ASPxCheckBox1=C&ctl00%24MainContent%24ASPxCheckBox2=U&ctl00%24MainContent%24ASPxCheckBox3=U&ctl00%24MainContent%24ASPxCheckBox4=U&ctl00%24MainContent%24ASPxCheckBox5=U&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C2_30"
                    a = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst3.aspx", data_check_first_and_next, streaming=False)
                    return a
                #Тыкнуть первый и к следующему
                #POST /eport/eport/studtst3.aspx HTTP/1.1
                def check_some_case_and_next(self, array1):
                    data_check_some_case_and_next = f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTI5MTM5NzM3Nw9kFgJmD2QWAgIDD2QWAmYPZBYCAg8PZBYSAgEPPCsABAEADxYCHgVWYWx1ZQUYKDIpINCf0L7Qt9C90LDQvdC40LUgLSAzZGQCBw88KwAEAQAPFgIfAAUQ0JfQsNC00LDQvdC40LUgMWRkAgkPFCsABA8WAh8ABSvQktCw0Ygg0LvQuNC80LjRgiDQstGA0LXQvNC10L3QuCAxOSDQvNC40L0uZDwrAAwBABYEHglGb3JlQ29sb3IKTx4EXyFTQgIEZGRkAgsPDxYCHgRUZXh0BXombmJzcDvQrdC80L%2FQuNGA0LjRh9C10YHQutC40LUg0LzQtdGC0L7QtNGLINC90LDRg9GH0L3QvtCz0L4g0LjRgdGB0LvQtdC00L7QstCw0L3QuNGPINC40YHQutC70Y7Rh9Cw0Y7RgjombmJzcDsmbmJzcDsgPGJyPmRkAg8PDxYCHwMFHiZuYnNwOzEuINC90LDQsdC70Y7QtNC10L3QuNC1O2RkAhMPDxYCHwMFICZuYnNwOzIuINGN0LrRgdC%2F0LXRgNC40LzQtdC90YI7ZGQCFw8PFgIfAwUhJm5ic3A7My4g0YTQvtGA0LzQsNC70LjQt9Cw0YbQuNGOZGQCGw8PFgIfAwUcJm5ic3A7NC4g0YHRgNCw0LLQvdC10L3QuNC1LmRkAh8PDxYCHwMFGyZuYnNwOzUuINC40LfQvNC10YDQtdC90LjQtWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjA0%2Bk22ByzKq5L7zouSrrJbMziS20QR38bdXSKqlADvvqw%3D&__VIEWSTATEGENERATOR=A8B80323&__EVENTVALIDATION=%2FwEdAAc%2FlZpllc25PN%2BYPogZdEuvCa17vhDUriBurXCsNy590WMU%2Ff8RYiHeDshdCQG6KXsl%2BbxYKsnWKi1oDF%2BSPbsJHS3vs9PY66cqRnl9zzvdQgrZ%2B0y1djOQFJQdjlbLnVhP%2FHXZRS6bBCR%2FaTH01z%2B9bOik%2B0yMqvUzm3kYLHgnd9IAIvs1oV7es8UR7FcUYQ4%3D&ctl00%24MainContent%24hfo1={array1[0][0]}&ctl00%24MainContent%24hfo2={array1[0][1]}&ctl00%24MainContent%24hfo3={array1[0][2]}&ctl00%24MainContent%24hfo4={array1[0][3]}&ctl00%24MainContent%24hfo5={array1[0][4]}&ctl00%24MainContent%24hf1=0&ctl00%24MainContent%24ASPxButton5=&ctl00%24MainContent%24ASPxCheckBox1={array1[1][0]}&ctl00%24MainContent%24ASPxCheckBox2={array1[1][1]}&ctl00%24MainContent%24ASPxCheckBox3={array1[1][2]}&ctl00%24MainContent%24ASPxCheckBox4={array1[1][3]}&ctl00%24MainContent%24ASPxCheckBox5={array1[1][4]}&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C2_30"
                    self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst3.aspx", data_check_some_case_and_next)
                    return array1[0]
                    #print(":", data_check_some_case_and_next)

                #Тыкнуть первый и в меню
                #POST /eport/eport/studtst3.aspx HTTP/1.1
                def check_first_and_return_main_menu(self, ):
                    data_check_first_and_return_main_menu = "ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTI5MTM5NzM3Nw9kFgJmD2QWAgIDD2QWAmYPZBYCAg8PZBYSAgEPPCsABAEADxYCHgVWYWx1ZQVTKDIpINCj0YXQvtC0INC30LAg0LHQvtC70YzQvdGL0LzQuCDQsiDQv9C10YDQuNC%2B0L%2FQtdGA0LDRgtC40LLQvdC%2B0Lwg0L%2FQtdGA0LjQvtC00LVkZAIHDzwrAAQBAA8WAh8ABRHQl9Cw0LTQsNC90LjQtSAyMmRkAgkPFCsABA8WAh8ABSrQktCw0Ygg0LvQuNC80LjRgiDQstGA0LXQvNC10L3QuCA0INC80LjQvS5kPCsADAEAFgQeCUZvcmVDb2xvcgorHgRfIVNCAgRkZGQCCw8PFgIeBFRleHQFWdCc0LXRgNGLINC%2F0YDQuCDQt9Cw0LTQtdGA0LbQutC1INC80L7Rh9C10LjRgdC%2F0YPRgdC60LDQvdC40Y8g0L%2FQvtGB0LvQtSDQvtC%2F0LXRgNCw0YbQuNC4ZGQCDw8PFgIfAwVNMS4g0J%2FRgNC40LzQtdC90LXQvdC40LUg0L%2FRg9C30YvRgNGPINGB0L4g0LvRjNC00L7QvCDQvdCwINC90LjQtyDQttC40LLQvtGC0LBkZAITDw8WAh8DBSwyLiDQvdCw0LfQvdCw0YfQtdC90LjQtSDQvNC%2B0YfQtdCz0L7QvdC90YvRhWRkAhcPDxYCHwMFTzMuINCy0L3Rg9GC0YDQuNCy0LXQvdC90L7QtSDQstCy0LXQtNC10L3QuNC1IDUlINGA0LDRgdGC0LLQvtGA0LAg0LPQu9GO0LrQvtC30YtkZAIbDw8WAh8DBWM0LiDQv9GA0LjQvNC10L3QtdC90LjQtSDRgtC10L%2FQu9C%2B0Lkg0LPRgNC10LvQutC4INC90LAg0L7QsdC70LDRgdGC0Ywg0LzQvtGH0LXQstC%2B0LPQviDQv9GD0LfRi9GA0Y9kZAIfDw8WAh8DBQFfZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b241BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMDQE5T9V7VMreWdfpku7yNIDDWy4F0wCwHlTSIdKybDHIQ%3D%3D&__VIEWSTATEGENERATOR=A8B80323&__EVENTVALIDATION=%2FwEdAAfDRLP7NE8mELLiT2ZK%2FjipCa17vhDUriBurXCsNy590WMU%2Ff8RYiHeDshdCQG6KXsl%2BbxYKsnWKi1oDF%2BSPbsJHS3vs9PY66cqRnl9zzvdQgrZ%2B0y1djOQFJQdjlbLnVhP%2FHXZRS6bBCR%2FaTH01z%2B9zErVTJvNAHMQny1oGGVfJe3IXe%2FaUiAq3S3lPvQuuas%3D&ctl00%24MainContent%24hfo1=1&ctl00%24MainContent%24hfo2=0&ctl00%24MainContent%24hfo3=0&ctl00%24MainContent%24hfo4=0&ctl00%24MainContent%24hfo5=0&ctl00%24MainContent%24hf1=0&ctl00%24MainContent%24ASPxButton04=&ctl00%24MainContent%24ASPxCheckBox1=C&ctl00%24MainContent%24ASPxCheckBox2=U&ctl00%24MainContent%24ASPxCheckBox3=U&ctl00%24MainContent%24ASPxCheckBox4=U&ctl00%24MainContent%24ASPxCheckBox5=U&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C2_30"
                    a = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst3.aspx", data_check_first_and_return_main_menu)
                    return a





                # ЗАЙТИ НА ПЯТЕРКУ
                #GET /eport/eport/studtst5.aspx HTTP/1.1
                def go_to_check_answer5(self):
                    a = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst5.aspx", "", get_request=True)

                    #Проверка на ошибку с невыполненным заданием
                    soup = BeautifulSoup(a.text, 'html.parser')
                    b1 = soup.select('script[src^="/eport/WebResource.axd"] ~ script[type="text/javascript"]')
                    for i in range(len(b1)): 
                        if "Задание не было выполнено" in b1[i].text:
                            return False

                    soup = BeautifulSoup(a.text, 'html.parser')
                    b = soup.select('table.btntest > tr > td > span[id^="ctl00_MainContent_Label"]')
                    answers_array = [["0" for i in range(5)],["U" for i in range(5)]]
                    #print("———>Before: ", answers_array)
                    for i in range(len(b)-1):
                        if "Salmon" in str(b[i+1]):
                            answers_array[0][i] = "1"
                            answers_array[1][i] = "C"
                        elif "Aquamarine" in str(b[i+1]):
                            answers_array[0][i] = "1"
                            answers_array[1][i] = "C"
                        else:
                            answers_array[0][i] = "0"
                            answers_array[1][i] = "U"
                    #print("———>Answers:", answers_array)

                    return answers_array



                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                def answer_all_questions(self,):
                    self.select_question("1")    
                    for i in range(30):
                        space = ""
                        if (i+1) < 10: space = " "
                        

                        var1 = self.go_to_check_answer5()
                        
                        if var1 == False:
                            return True

                        new_list = self.check_some_case_and_next(var1)
                        
                        print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Вопрос {i+1}{space}: {new_list}")
                                            
                    return False

                #check_results_of_tests_by_num_of_pred
                #POST /eport/eport/studtst1.aspx HTTP/1.1
                def check_all_results_of_tests_by_num_of_pred(self, num_of_pred=0):
                    data_check_results_of_tests_by_num_of_pred = f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUIOTk1NDMwOTQPZBYCZg9kFgICAw9kFgJmD2QWAgIJD2QWBAIDD2QWAmYPZBYCZg9kFgJmD2QWAgIBDxQrAAUPFgIeD0RhdGFTb3VyY2VCb3VuZGdkZGQ8KwAHAQYPZBAWAgIBAgIWAhQrAAEWAh4PQ29sVmlzaWJsZUluZGV4ZhQrAAEWAh8BAgFkFgBkAgcPZBYCZg9kFgJmD2QWAmYPZBYCAgEPFCsABWRkZDwrAAcBBg9kEBYCZgIBFgIUKwABFgIfAWYUKwABFgIfAQIBZBYAZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjcFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjm6%2BEbUEKpaxmSv00E%2B%2FJiuKcZ%2BYI%2BIkpp3rzk2vaUFAA%3D%3D&__VIEWSTATEGENERATOR=847F47AD&__EVENTVALIDATION=%2FwEdAAeH8wh4QiiJKgOuKnFFkPWbI7ZJDWlRgaefdPW8BTEVtXw%2BikVKJJfrT0ndBbXKBTA39nUTQDb0GEkh6LDT5SpRsAIaIhbklmBqr8w%2BPxD292wBCiQy8HT9gxcspUtWdqpbDCDdUSb6jcSCho5zpwlSvNMTFvzkvoYxtvqO8J0ljItyMFkzxVGQu2RBvSrJ7No%3D&ctl00%24MainContent%24hfPred={str(num_of_pred)}&ctl00%24MainContent%24hfTest=-1&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2DeletedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2InsertedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel1%24ASPxListBox2=System.Data.DataRowView&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3DeletedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3InsertedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel2%24ASPxListBox3=&ctl00%24MainContent%24ASPxButton9=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C1_41%2C2_36"
                    a = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst1.aspx", data_check_results_of_tests_by_num_of_pred)
                    result_array = []
                    del result_array[:]
                    #<span id="ctl00_MainContent_Label1"><table class="testved">
                    soup = BeautifulSoup(a.text, 'html.parser')
                    b = soup.select('span[id="ctl00_MainContent_Label1"] > table[class="testved"] > tr')
                    for i in range(len(b)):
                        b[i] = b[i].select('td')
                        #for j in range(len(b[i])):
                            #b[i][j] = b[i][j].select('tr')
                    return b
                

                #Завершить тест из теста
                #POST /eport/eport/studtst2.aspx HTTP/1.1
                def close_test(self, num_pred_r=-1, num_testing=-1):
                    data_close_test = "ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTUwNzg4NDI2OQ9kFgJmD2QWAgIDD2QWAgIBD2QWAgIDD2QWQgIBDzwrAAQBAA8WAh4FVmFsdWUFKCgxKSDQoNGD0YHRgdC60LDRjyDRhNC40LvQvtGB0L7RhNC40Y8gLTFkZAIJDzwrAAQBAA8WAh8ABSvQmNC00LXQvdGC0LjRhNC40LrQsNGC0L7RgCDRgtC10YHRgtCwIDEyNDUwZGQCCw8UKwAEDxYCHwAFKtCS0LDRiCDQu9C40LzQuNGCINCy0YDQtdC80LXQvdC4IDIg0LzQuNC9LmQ8KwAMAQAWBB4JRm9yZUNvbG9yCqABHgRfIVNCAgRkZGQCDw8UKwAGZGRkZDwrAAcBABYEHgtDc3NGaWxlUGF0aAUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHgpDc3NQb3N0Zml4BQVHbGFzczwrAAYBABYCHhFTcHJpdGVDc3NGaWxlUGF0aAUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCEQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAhMPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIVDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCFw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAhkPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIbDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCHQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAh8PFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIhDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCIw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAiUPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAInDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCKQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAisPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAItDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCLw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAjEPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIzDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCNQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAjcPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAI5DxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCOw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAj0PFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAI%2FDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCQQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAkMPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAJFDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCRw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAkkPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WIQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjA0BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMDIFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24wMwUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjEFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMwUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjQFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b241BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNgUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjcFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b244BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjEwBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTEFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xMgUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjEzBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTQFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE2BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTcFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xOAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE5BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjAFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yMQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjIyBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjMFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yNAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjI1BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjYFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yNwUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjI4BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjkFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24zMGNg%2Btc0Yd%2B%2BfMAWH2wgXducRETufa9xvvwxgDjN4cZ%2F&__VIEWSTATEGENERATOR=4F4B5F1E&ctl00%24MainContent%24ASPxButton03=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40"
                    a = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst2.aspx", data_close_test)
                    def test_na_zakritiy_test_izza_istekshego_vremeni(a):
                        soup = BeautifulSoup(a.text, 'html.parser')
                        b4 = soup.select('h1')
                        
                        for i, item in enumerate(b4):
                            if "Ошибка сервера" in item.text:
                                return False
                        if "Эта страница ошибки может содержать важные данные, так как ASP.NET настроено на показ подробных сообщений об ошибках с помощью" in str(a):
                            return False
                        
                        #print("Всё хорошо, тест закрылся")
                        return True
                    
                    if test_na_zakritiy_test_izza_istekshego_vremeni(a):
                        return True
                    else:
                        #print("\n\nстарый ааааааааааааа\n\n")
                        #print(a.request.body)
                        #print(a.text)
                        a = self.enter_current_test(num_pred_r, num_testing)  #входим

                        soup = BeautifulSoup(a.text, 'html.parser')
                        b4 = soup.select('h1')
                        
                        for i, item in enumerate(b4):
                            if "Ошибка сервера" in item.text:
                                print("\n\n\n\n\n\n\n Последний раз пробую решить мирно реауфом, жду 10 секунд....")
                                try:
                                    for i in range(10):
                                        time.sleep(1)
                                except KeyboardInterrupt:
                                    print("Хорошо! Перестаю")
                                self.auth()
                                a = self.enter_current_test(num_pred_r, num_testing) 




                        soup = BeautifulSoup(a.text, 'html.parser')
                        
                        # 1 проверка на уже прорешанный ранее тест с результатом меньше 70 %
                        b2 = soup.select('label[id="ctl00_MainContent_ASPxLabel10"]')
                        for i in range(len(b2)): 
                            if "Просмотр ответов заданий возможен только при выполнении не менее 70% теста" in b2[i].text:
                                print(f"\n!!!ТЕСТ НЕ ОТКРЫТ (1), ПРОБУЮ ЕГО ЗАКРЫТЬ...")
                                self.close_test_70_error()
                                return a
                        
                        # 2 проверка на решенный ранее более чем на 70+ тест
                        b3 = soup.select('label[id="ctl00_MainContent_ASPxLabel8"]')
                        for i in range(len(b3)): 
                            if "Всего правильных ответов" in b3[i].text:
                                print(f"\n!!!ТЕСТ НЕ ОТКРЫТ (2), ПРОБУЮ ЕГО ЗАКРЫТЬ...")
                                self.close_test(num_pred_r, num_testing)
                                break
                    
                    print("!!!!!!!!!!!!!!ЧТОТО ПОШЛО НЕ ТАК, НЕ ХОЧЕТ ЗАКРЫВАТЬСЯ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    #print("\n\nновый аааааааааааа\n\n\n")
                    #print(a.request.body)
                    #print(a.text)
                    print("\n\n")
                    return self.close_test(num_pred_r, num_testing)


                        
                    


                #Завершить тест при меньше 70 % ошибке
                #POST /eport/eport/studtst4.aspx HTTP/1.1
                def close_test_70_error(self):
                    data_close_test = "ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTQ4OTc2MzU4MA9kFgJmD2QWAgIDD2QWAgIBD2QWAgIDD2QWRgIBDzwrAAQBAA8WAh4FVmFsdWUFKCgxKSDQoNGD0YHRgdC60LDRjyDRhNC40LvQvtGB0L7RhNC40Y8gLTFkZAIFDw8WAh4EVGV4dGVkZAIHDw8WBh8BZR4JRm9yZUNvbG9yCpEBHgRfIVNCAgRkZAITDzwrAAQBAA8WAh8ABQEgZGQCFQ8UKwAEDxYCHwAFiQHQn9GA0L7RgdC80L7RgtGAINC%2B0YLQstC10YLQvtCyINC30LDQtNCw0L3QuNC5INCy0L7Qt9C80L7QttC10L0g0YLQvtC70YzQutC%2BINC%2F0YDQuCDQstGL0L%2FQvtC70L3QtdC90LjQuCDQvdC1INC80LXQvdC10LUgNzAlINGC0LXRgdGC0LAuIGQ8KwAMAQAWBh8CCpEBHglGb250X1NpemUoKiJTeXN0ZW0uV2ViLlVJLldlYkNvbnRyb2xzLkZvbnRVbml0BDI1cHQfAwKECGRkZAIXDxQrAAYPFgIeB1Zpc2libGVoZGRkZDwrAAcBABYEHgtDc3NGaWxlUGF0aAUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MeCkNzc1Bvc3RmaXgFB1JlZFdpbmU8KwAGAQAWAh4RU3ByaXRlQ3NzRmlsZVBhdGgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCGQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAhsPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBwUFR2xhc3M8KwAGAQAWAh8IBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIdDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCHw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAiEPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAIjDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwcFBUdsYXNzPCsABgEAFgIfCAUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCJQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAicPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAIpDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCKw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAi0PFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBwUFR2xhc3M8KwAGAQAWAh8IBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIvDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwcFBUdsYXNzPCsABgEAFgIfCAUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCMQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAjMPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAI1DxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCNw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAjkPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAI7DxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCPQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAj8PFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBwUFR2xhc3M8KwAGAQAWAh8IBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAJBDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCQw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8HBQVHbGFzczwrAAYBABYCHwgFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAkUPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAJHDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCSQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAksPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAJNDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCTw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAlEPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjAz1nJ55AxZ4GtGPuU7FLyU46WjfL997Ctb045KzUnZOCI%3D&__VIEWSTATEGENERATOR=6D81C9BC&ctl00%24MainContent%24ASPxButton03="
                    a = self.make_a_request("http://eport.fesmu.ru/eport/eport/studtst4.aspx", data_close_test)
                    return a 

                def try_to_check_all(self):
                    self.select_question("1")
                    for i in range(30):
                        self.check_first_and_next()



                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                '''def check_all_first_cases_and_verify(self, num_of_error=0):
                    num_of_error += 1
                    num_of_error_vsego = 50
                    if num_of_error <=num_of_error_vsego:
                        self.try_to_check_all()

                        res = self.check_first_and_return_main_menu()
                        soub = BeautifulSoup(res.text, 'html.parser')
                        a = soub.select('table[class="btntest"] > tr > td > table > tr > td[id^="ctl00_MainContent_ASPxButton"]')
                        if len(a) == 30:
                            for i, item in enumerate(a):
                                if 'class="dxbButton_Aqua"' in str(item):
                                    print(f'Внимание!, {i+1} вопрос не прорешан, пробую еще раз ({num_of_error}/{num_of_error_vsego})...')
                                    return self.check_all_first_cases_and_verify(num_of_error=num_of_error)
                        else:
                            print(f'Внимание!, что-то пошло не так, пробую еще раз ({num_of_error}/{num_of_error_vsego})...')
                            return self.check_all_first_cases_and_verify(num_of_error=num_of_error)
                        return True
                    else:
                        print("Не получается, извините, завершаю работу программы")
                        quit()'''
                def check_all_first_cases_and_verify(self, num_of_error=0):
                    #num_of_error += 1
                    num_of_error_vsego = 50
                    if num_of_error <=num_of_error_vsego:
                        self.try_to_check_all()
                        res = self.check_first_and_return_main_menu()
                        def proverka(res, num_of_error=0):
                            num_of_error += 1
                            soub = BeautifulSoup(res.text, 'html.parser')
                            a = soub.select('table[class="btntest"] > tr > td > table > tr > td[id^="ctl00_MainContent_ASPxButton"]')
                            if len(a) == 30:
                                for i, item in enumerate(a):
                                    if 'class="dxbButton_Aqua"' in str(item):
                                        print(f'Внимание!, {i+1} вопрос не прорешан, пробую дотыкать его ({num_of_error}/{num_of_error_vsego})...')
                                        self.select_question(str(i+1))
                                        res = self.check_first_and_return_main_menu()
                                        return proverka(res, num_of_error=num_of_error)
                            else:
                                print(f'Внимание!, что-то пошло не так, пробую еще раз ({num_of_error}/{num_of_error_vsego})...')
                                res = self.check_first_and_return_main_menu()
                                return proverka(res, num_of_error=num_of_error)
                                #return self.check_all_first_cases_and_verify(num_of_error=num_of_error)
                            return True
                        return proverka(res)
                    else:
                        print("Не получается, извините, завершаю работу программы")
                        QUIT_BOT = True
                        quit()


            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################

            def make_keyboard(main_array): # [["NAME_OF_BUTTON", CALLBACK_DATA]]
                keyboard = types.InlineKeyboardMarkup()
                for i in main_array:
                    key = types.InlineKeyboardButton(text=str(i[0]), callback_data=str(i[1]))
                    keyboard.add(key)
                return keyboard

            def make_keyboard_for_non_known_len_of_array(main_array, poryadok, return_key=False):
                keyboard = types.InlineKeyboardMarkup()
                for i, j in enumerate(main_array):
                    #print('\n\n\n\n', i, j)
                    key = types.InlineKeyboardButton(text=str(j[0] + ". " + j[1]), callback_data=str(i+poryadok))
                    keyboard.add(key)
                if return_key == True:
                    keyboard.add(types.InlineKeyboardButton(text=str('Вернуться в меню'), callback_data=str(-1)))
                return keyboard

            def get_keyboard(num, option1=-1):
                #ГЛАВНОЕ МЕНЮ
                if num == 0:   return make_keyboard([['1', 0], ['2', 1], ['3', 2],])# ['4', 3]])
                #ВЫБОР ТАРИФА
                if num == 2: return make_keyboard([['Мини - 150₽', 11], ['Медиум - 300₽', 12], ['VIP - 480₽', 13], ['Вернуться...', "return_main"]])

            ######################## ГЛАВНЫЙ МАССИВ ПОЛЬЗОВАТЕЛЕЙ И ИХ ГЛАВНЫХ СМС (хранит пары ключ(Id) значение (массив смс которые нужно будет удалить))
            array_message = dict()  

            ######################## ВРЕМЕННЫЕ СМС КОТОРЫЕ НУЖНО УДАЛЯТЬ (хранит пары ключ(Id) значение (массив смс которые нужно будет удалить) как предыдущий)
            temp_messages = dict()


            ######################## DELETE MESSAGES` ARRAY
            def del_msg(chat_id, msg_id_array):  #msg_id - array
                #time.sleep(0.2)
                try:
                    if len(msg_id_array) != 0:
                        print("\n--—-----------------------------------------\nПОЛУЧЕН ЗАПРОС НА УДАЛЕНИЕ:", msg_id_array)
                        try:
                            bot.delete_messages(chat_id, msg_id_array)
                            #print("Успешно удалено смс в телеграмме")
                            print("------> УДАЛЕНИЕ ПРОШЛО БЕЗ ОШИБОК, ОЧИЩАЮ МАССИВ")
                            msg_id_array.clear()
                            return True
                        except Exception as e:
                            print('Не получилось удалить смс в телеграмме', msg_id_array, e)
                            print("    ERROR 2: (ошибка удаления смс)", e, " ВХОЖУ ЕЩЕ РАЗ В СЕБЯ ДЛЯ ПОПЫТКИ ЕЩЕ РАЗ!!!!!!!!!!!!!!!")
                            del_msg(chat_id, msg_id_array)
                    else:
                        print("СПИСОК НА УДАЛЕНИЕ ПУСТОЙ!!!!")
                        return True
                except Exception as e:
                    print("    ERROR 1: (глобальная ошибка)", e, " ВХОЖУ ЕЩЕ РАЗ В СЕБЯ ДЛЯ ПОПЫТКИ ЕЩЕ РАЗ!!!!!!!!!!!!!!!")
                    del_msg(chat_id, msg_id_array)

            def init_new_dict(message):
                chat_id = message.chat.id
                print('''\n--—-----------------------------------------''')
                print(str(message.from_user.username) + "(" +str(message.from_user.id) +", " + str(message.chat.id) +  ")" +  " нажал /start ")
                print("array_message before:", array_message)
                if chat_id in array_message:
                    if len(array_message[chat_id]) == 0:
                        print(" —> TO DO NOTHING, LEN(DICT)=0")
                    else:
                        print(" —> CLEAN ALL MSG IN array_message:")
                        del_msg(chat_id, array_message[chat_id])
                        #array_message[chat_id].clear()
                else:
                    array_message[chat_id] = []
                    temp_messages[chat_id] = []
                    print(" —> INITIALIZATION NEW USER`s DICTS ")



            @bot.message_handler(commands=['help'])
            def help_func(msg):
                bot.send_message(msg.from_user.id, text='Используйте командy /start для запуска бота!') 


            fenix = FENIX()



            ############################################################
            ######   ГЛАВНАЯ ФУНКЦИЯ    ################################
            ############################################################
            ############################################################
            @bot.message_handler(commands=['start', 'start2'])
            def start_func(message):
                print("\nCLEAR_STEP_HANDLER:", bot.clear_step_handler_by_chat_id(message.chat.id))
                try:
                    print(del_msg(message.chat.id, fenix.array_to_del))
                except Exception as E:
                    print(f"pohui: {E}")
                init_new_dict(message)
                errors = ''
                if fenix.num_of_mistakes_ot == fenix.num_of_mistakes_do:
                    errors = f"{fenix.num_of_mistakes_ot} шт"
                else:
                    errors = f"{fenix.num_of_mistakes_ot}-{fenix.num_of_mistakes_do}"
                times = ''
                if fenix.time_to_wait_ot == fenix.time_to_wait_do:
                    times = f"{fenix.time_to_wait_ot} сек"
                else:
                    times = f"{fenix.time_to_wait_ot}-{fenix.time_to_wait_do}"
                
                key_new = make_keyboard([['1. Решить тесты', 0],
                                        [f'2. Изменить ошибки ({errors})', 1], 
                                        [f'3. Изменить время ожидания ({times})   ', 2], 
                                        ['4. Изменить данные аккаунта', 3],
                                        ['5. Выключить бота', 4]])

                sms = bot.send_message(message.from_user.id, text="""Выберите действие:"""
                                    , reply_markup=key_new)
                #array_message[message.chat.id].append(message.message_id) - сообщение пользователя /start
                
                if len(array_message[message.chat.id]) != 0:
                    print("\n----------------------------------\nWARNING - ОСТАЛОСЬ НЕКОТОРОЕ КОЛИЧЕСТВО СООБЩЕНИЙ В СПИСКЕ - УДАЛЯЮ !!!")
                    del_msg(message.chat.id, array_message[message.chat.id])
                
                array_message[message.chat.id].append(sms.id)
                print("array_message after:", array_message)


            ############################################################
            ############################################################
            @bot.callback_query_handler(func=lambda call: call.data == '-1')
            def return_to_start_message(call):
                print("\nCLEAR_STEP_HANDLER:", bot.clear_step_handler_by_chat_id(call.message.chat.id))
                try:
                    print(del_msg(call.message.chat.id, fenix.array_to_del))
                except Exception as E:
                    print(f"pohui: {E}")
                errors = ''
                if fenix.num_of_mistakes_ot == fenix.num_of_mistakes_do:
                    errors = f"{fenix.num_of_mistakes_ot} шт"
                else:
                    errors = f"{fenix.num_of_mistakes_ot}-{fenix.num_of_mistakes_do}"
                times = ''
                if fenix.time_to_wait_ot == fenix.time_to_wait_do:
                    times = f"{fenix.time_to_wait_ot} сек"
                else:
                    times = f"{fenix.time_to_wait_ot}-{fenix.time_to_wait_do}"
                
                key_new = make_keyboard([['1. Решить тесты', 0],
                                        [f'2. Изменить ошибки ({errors})', 1], 
                                        [f'3. Изменить время ожидания ({times})   ', 2], 
                                        ['4. Изменить данные аккаунта', 3],
                                        ['5. Выключить бота', 4]])
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=array_message[call.message.chat.id][0], 
                    text="""Выберите действие:""", reply_markup=key_new)  


            @bot.callback_query_handler(func=lambda call: call.data == '4')
            def quit_from_gui(call):
                sms = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"✅До скорой встречи через 3...")
                x = 3
                time.sleep(1)
                while x != 1:
                    x = x - 1
                    sms = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"✅До скорой встречи через {x}...")
                    time.sleep(1)
                if del_msg(call.message.chat.id, [sms.id]):
                    print(f" ——> УДАЛЕНЫ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}]")
                else:
                    print(f" ——> ERROR: НЕ ПОЛУЧИЛОСЬ УДАЛИТЬ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}]")
                try:
                    bot.stop_bot()
                except Exception:
                    pass
                print("\n--------------------------------------------------\nОстанавливаю бота, подождите!...\n")
                QUIT_BOT = True
                print('1')
                bot.stop_bot()
                print('2')
                #quit()
                #print('3')
                #quit()
                #print('4')
                

            ###########################################################################
            ###########################################################################
            ## ДЛЯ ПАРСИНГА ВВОДИМЫХ ИНТЕРВАЛОВ ОШИБОК И ВРЕМЕНИ ######################
            def parse_interval(message):
                try:
                    a = message
                    razdel = a.find('-')
                    if razdel == -1:
                        try:
                            num0 = int(a)
                            return [num0, num0]
                        except:
                            return False
                    num1 = int(a[:razdel])
                    num2 = int(a[razdel+1:])
                    return [num1, num2]
                except Exception as E:
                    print(f"ERROR: {str(E)}")
                    return False


            #####   ОШИБКИ   ##########################################################
            @bot.callback_query_handler(func=lambda call: call.data == '1')
            def change_error(call):
                print("\n----------------------------------")
                print("Введите количество ошибок\nПримечание: можно указать как точное количество ошибок (например \"3\" или \"0\"), так и интервал, среди значений которого каждый раз количество ошибок будет выбираться случайно (например \"2-5\")")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите количество ошибок\nПримечание: можно указать как точное количество ошибок (например \"3\" или \"0\"), так и интервал, среди значений которого каждый раз количество ошибок будет выбираться случайно (например \"2-5\")", reply_markup=make_keyboard([['Отменить ввод❌', -1]]))  
                bot.register_next_step_handler(call.message, change_error_next_step, call)
            def change_error_next_step(message, call):
                a = message.text
                error = False
                try:
                    if parse_interval(a):
                        error = False
                        num1, num2 = parse_interval(a)
                        if num1 < 0 : error = True
                        if num2 > 30 : error = True
                        if num1 > num2: error = True
                        if error:
                            print(f"Вы допустили ошибку при вводе диапозона ошибок! Вы ввели: {a}")
                            sms = bot.send_message(message.from_user.id, text=f"❌Не получилось установить \"{a}\" ошибок!\nСообщения будут удалены через 2...")
                        else:
                            fenix.num_of_mistakes_ot = num1
                            fenix.num_of_mistakes_do = num2
                            errors = ''
                            if fenix.num_of_mistakes_ot == fenix.num_of_mistakes_do:
                                errors = f"{fenix.num_of_mistakes_ot} шт"
                            else:
                                errors = f"от {fenix.num_of_mistakes_ot} до {fenix.num_of_mistakes_do} шт"

                            sms = bot.send_message(message.from_user.id, text=f"✅Установлено количество ошибок {errors}\nСообщения будут удалены через 2...")
                            print(f"Установлено рандомное колиество ошибок от {num1} до {num2}")
                    else:
                        error = True
                        print(f"Вы допустили ошибку при вводе диапозона ошибок! Вы ввели: {a}")
                        sms = bot.send_message(message.from_user.id, text=f"❌Не получилось установить \"{a}\" ошибок!\nСообщения будут удалены через 2...")
                except ValueError:
                    error = True
                    print(f"Вы допустили ошибку при вводе диапозона ошибок! Вы ввели: {a}")
                    sms = bot.send_message(message.from_user.id, text=f"❌Не получилось установить \"{a}\" ошибок!\nСообщения будут удалены через 2...")
                    print('''\n--—-----------------------------------------''')
                #repeat
                if fenix.num_of_mistakes_ot == fenix.num_of_mistakes_do:
                    errors = f"{fenix.num_of_mistakes_ot} шт"
                else:
                    errors = f"от {fenix.num_of_mistakes_ot} до {fenix.num_of_mistakes_do} шт"
                #И теперь удаляем их
                x = 2
                time.sleep(1)
                while x != 1:
                    x = x - 1
                    if error:
                        sms = bot.edit_message_text(chat_id=message.chat.id, message_id=sms.id, text=f"❌Не получилось установить \"{a}\" ошибок!\nСообщения будут удалены через {x}...")
                    else:
                        sms = bot.edit_message_text(chat_id=message.chat.id, message_id=sms.id, text=f"✅Установлено количество ошибок {errors}\nСообщения будут удалены через {x}...")
                    time.sleep(1)
                if del_msg(message.chat.id, [sms.id, message.message_id]):
                    print(f" ——> УДАЛЕНЫ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}, {message.message_id}]")
                else:
                    print(f" ——> ERROR: НЕ ПОЛУЧИЛОСЬ УДАЛИТЬ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}, {message.message_id}]")
                try:
                    return_to_start_message(call)
                except Exception as E:
                    print(f"pohui: {E}")



            #####   ВРЕМЯ   ###########################################################
            @bot.callback_query_handler(func=lambda call: call.data == '2')
            def change_time_interval(call):  
                print("\n----------------------------------")
                print("Введите время ожидания в секундах\nПримечание: можно указать как точное количество секундах (например \"300\" или \"420\"), так и интервал, среди значений которого каждый раз количество ошибок будет выбираться случайно (например \"320-480\")")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите время ожидания в секундах\nПримечание: можно указать как точное количество секундах (например \"300\" или \"420\"), так и интервал, среди значений которого каждый раз количество ошибок будет выбираться случайно (например \"320-480\")", reply_markup=make_keyboard([['Отменить ввод❌', -1]]))  
                bot.register_next_step_handler(call.message, change_time_interval_next_step, call)
            def change_time_interval_next_step(message, call):
                a = message.text
                error = False
                try:
                    if parse_interval(a):
                        error = False
                        num1, num2 = parse_interval(a)
                        if num1 < 0 : error = True
                        if num2 > 1200 : error = True
                        if num1 > num2: error = True
                        if error:
                            print(f"1Вы допустили ошибку при вводе диапозона ожидаемого времени! Вы ввели: {a}")
                            sms = bot.send_message(message.from_user.id, text=f"❌Не получилось установить дипозон \"{a}\" для ожидаемого времени!\nСообщения будут удалены через 2...")
                        else:
                            fenix.time_to_wait_ot = num1
                            fenix.time_to_wait_do = num2
                            times = ''
                            if fenix.time_to_wait_ot == fenix.time_to_wait_do:
                                times = f"{fenix.time_to_wait_ot} сек"
                            else:
                                times = f"от {fenix.time_to_wait_ot} до {fenix.time_to_wait_do} сек"
                            sms = bot.send_message(message.from_user.id, text=f"✅Установлено время ожидания {times}\nСообщения будут удалены через 2...")
                            print(f"Установлено рандомное колиество ошибок от {num1} до {num2}")
                    else:
                        error = True
                        print(f"2Вы допустили ошибку при вводе диапозона ошибок! Вы ввели: {a}")
                        sms = bot.send_message(message.from_user.id, text=f"❌Не получилось установить дипозон \"{a}\" для ожидаемого времени!\nСообщения будут удалены через 2...")
                except ValueError:
                    error = True
                    print(f"3Вы допустили ошибку при вводе диапозона ошибок! Вы ввели: {a}")
                    sms = bot.send_message(message.from_user.id, text=f"❌Не получилось установить дипозон \"{a}\" для ожидаемого времени!\nСообщения будут удалены через 2...")
                    print('''\n--—-----------------------------------------''')
                #repeat
                if fenix.time_to_wait_ot == fenix.time_to_wait_do:
                    times = f"{fenix.time_to_wait_ot} сек"
                else:
                    times = f"от {fenix.time_to_wait_ot} до {fenix.time_to_wait_do} сек"
                #И теперь удаляем их
                x = 2
                time.sleep(1)
                while x != 1:
                    x = x - 1
                    if error:
                        sms = bot.edit_message_text(chat_id=message.chat.id, message_id=sms.id, text=f"❌Не получилось установить дипозон \"{a}\" для ожидаемого времени!\nСообщения будут удалены через {x}...")
                    else:
                        sms = bot.edit_message_text(chat_id=message.chat.id, message_id=sms.id, text=f"✅Установлено время ожидания {times}\nСообщения будут удалены через {x}...")
                    time.sleep(1)
                if del_msg(message.chat.id, [sms.id, message.message_id]):
                    print(f" ——> УДАЛЕНЫ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}, {message.message_id}]")
                else:
                    print(f" ——> ERROR: НЕ ПОЛУЧИЛОСЬ УДАЛИТЬ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}, {message.message_id}]")
                try:
                    return_to_start_message(call)
                except Exception as E:
                    print(f"pohui: {E}")


            ###########################################################################
            @bot.callback_query_handler(func=lambda call: call.data == '0')
            def test_solver(call):
                try:
                    print(del_msg(call.message.chat.id, fenix.array_to_del))
                except Exception as E:
                    print(f"pohui: {E}")
                print("\nCLEAR_STEP_HANDLER:", bot.clear_step_handler_by_chat_id(call.message.chat.id))
                print("iamhere1")
                if fenix.get_login() and fenix.get_pass():
                    print("iamhere2")
                    privetstvie = fenix.auth()
                    if privetstvie:
                        print("iamhere3")
                        start_to_solve_test(call, privetstvie)
                    else:
                        print("iamhere4")
                        sms = bot.send_message(call.message.chat.id, text=f"❌Кажется в данных ошибка!!! Попробуйте изменить логин или пароль\nСообщения будут удалены через 2...")
                        print("Кажется в данных ошибка!!! Попробуйте изменить логин или пароль\nСообщения будут удалены через 2...")
                        x = 2
                        time.sleep(1)
                        while x != 1:
                            x = x - 1
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=sms.id, text=f"❌Кажется в данных ошибка!!! Попробуйте изменить логин или пароль\nСообщения будут удалены через {x}...")
                            time.sleep(1)
                        if del_msg(call.message.chat.id, [sms.id]):
                            print(f" ——> УДАЛЕНЫ НЕНУЖНЫЕ СООБЩЕНИЯ:  {fenix.array_to_del}")
                        else:
                            print(f" ——> ERROR: НЕ ПОЛУЧИЛОСЬ УДАЛИТЬ НЕНУЖНЫЕ СООБЩЕНИЯ:  {fenix.array_to_del}")
                else:
                    print("iamhere5")
                    enter_new_data_LOGIN(call)
            
            @bot.callback_query_handler(func=lambda call: call.data == '3')
            def enter_new_data_LOGIN(call):
                print("iamhere6")
                fenix.array_to_del = []
                log1 = fenix.get_login()
                pass1 = fenix.get_pass()
                if log1 == False: log1 = "-"
                if pass1 == False: pass1 = "-"
                to_print = f"Ваши данные\nЛогин: {log1}\nПароль: {pass1}"
                sms = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                    text=f"""{to_print}""", reply_markup=make_keyboard([['Отменить ввод❌', '-3']]))  
                print("Введите логин:")
                sms = bot.send_message(call.message.chat.id, text=f"Введите свой логин:")
                fenix.array_to_del.append(sms.id)
                bot.register_next_step_handler(call.message, enter_new_data_PASSWORD, call)
            def enter_new_data_PASSWORD(message, call):
                login = message.text
                sms = bot.send_message(message.from_user.id, text=f"Введите свой пароль:")
                print('Введите пароль:')
                fenix.array_to_del.append(message.message_id)
                fenix.array_to_del.append(sms.id)
                bot.register_next_step_handler(message, write_login_and_password, call, login)
            def write_login_and_password(message, call, login):
                passw = message.text
                fenix.set_login_pass(login1=quote(login), pass1=quote(passw))
                print(f"Спасибо! Записал в файл {login}:{passw}...")
                sms = bot.send_message(message.from_user.id, text=f"✅Спасибо! Записал в файл {login}:{passw}\nСообщения будут удалены чере 2...")
                fenix.array_to_del.append(message.message_id)
                fenix.array_to_del.append(sms.id)
                x = 2
                time.sleep(1)
                while x != 1:
                    x = x - 1
                    bot.edit_message_text(chat_id=message.chat.id, message_id=sms.id, text=f"✅Спасибо! Записал в файл {login}:{passw}\nСообщения будут удалены через {x}...")
                    time.sleep(1)
                if del_msg(message.chat.id, fenix.array_to_del):
                    print(f" ——> УДАЛЕНЫ НЕНУЖНЫЕ СООБЩЕНИЯ:  {fenix.array_to_del}")
                else:
                    print(f" ——> ERROR: НЕ ПОЛУЧИЛОСЬ УДАЛИТЬ НЕНУЖНЫЕ СООБЩЕНИЯ:  {fenix.array_to_del}")
                try:
                    return_to_start_message(call)
                except Exception as E:
                    print(f"pohui: {E}")

            @bot.callback_query_handler(func=lambda call: call.data == '-3')
            def return_to_main_menu_and_clear_temporary_messages(call):
                print("\nCLEAR_STEP_HANDLER:", bot.clear_step_handler_by_chat_id(call.message.chat.id))
                print("Deletind msgs:", del_msg(call.message.chat.id, fenix.array_to_del))
                return_to_start_message(call)	

            def start_to_solve_test(call, privetstvie):
                print("okkkkkkkkkkkkkkkkkkkk")
                fenix.list_of_preds = fenix.print_predmets_and_chose_it_step1()
                new_key = make_keyboard_for_non_known_len_of_array(fenix.list_of_preds, 20, return_key=True)
                #sms = bot.send_message(call.message.chat.id, text=f"Доступные вам тесты:", reply_markup=new_key)
                sms = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                    text=f"""{privetstvie}\n\nВыберите предмет:""", reply_markup=new_key)  





            ############ФУНКЦИЯ ВЫВОДА СПИСКА ТЕСТОВ ПО ТЫКНУТОМУ ПРЕДМЕТУ
            @bot.callback_query_handler(func=lambda call: int(call.data) >= 20 and int(call.data) <= 39) 
            def chose_PREDMET(call):
                print('\n--------------------------\n', int(call.data), '->', int(call.data)-20)
                fenix.num_of_pred = int(call.data)-20
                res = fenix.print_tests_of_predmet_by_its_index_and_chose_test_step2(int(call.data)-20)
                string_of_tests = res[0]
                fenix.list_of_vsex_testov = res[1]
                try:
                    sms = bot.edit_message_text(chat_id=call.message.chat.id, message_id=array_message[call.message.chat.id][0],
            text=f"Выберите номера тестов \nПРИМЕР: 1-4, 7, 13-15, 17-20, 21\n{string_of_tests}", 
            reply_markup=make_keyboard(([['Вернуться к выбору предмета', 0], ['Вернуться в меню', -1],])))
                except Exception as E:
                    print(f"pohui1: {E}")
                bot.register_next_step_handler(call.message, chose_TEST, int(call.data)-20) #index_of_pred
                
                


            #########АЛЬТЕРНАТИВА ЕСЛИ ЧЕЛ ВЫБРАЛ НОМЕРА ТЕСТОВ И ОТКАЗАЛСЯ ОТ НИХ
            @bot.callback_query_handler(func=lambda call: int(call.data) >= 40 and int(call.data) <= 59) 
            def chose_PREDMET_AFTER_NO_ACCEPTY_CHOSEN_NUM_OF_TEST(call):
                try:
                    print("\nCLEAR_STEP_HANDLER:", bot.clear_step_handler_by_chat_id(call.message.chat.id))
                except Exception as E:
                    print(f"pohui2: {E}")
                try:
                    print("2. Deletind msgs:", del_msg(call.message.chat.id, fenix.array_to_del))
                except Exception as E:
                    print(f"pohui3: {E}")
                print('\n--------------------------\n', int(call.data), '->', int(call.data)-40)
                fenix.num_of_pred = int(call.data)-40
                bot.register_next_step_handler(call.message, chose_TEST, int(call.data)-40) #index_of_pred



            def parse_num_of_tests(str_to_parse):
                res = re.split(",|;", str_to_parse)
                res2 = []	
                itog_print = "Решаю тесты: "
                
                for i, j in enumerate(res):
                    res[i] = j.strip()
                    razdel = res[i].find('-')
                    if razdel != -1:
                        num1 = res[i][:razdel]
                        num2 = res[i][razdel+1:]
                        #print(razdel, num1, num2)
                        if i == (len(res)-1):
                            itog_print += f"c {num1} по {num2}, верно?"
                        else:
                            itog_print += f"c {num1} по {num2}, "
                        for X in range(int(num1), int(num2)+1):
                            res2.append(str(X))
                    else:
                        res2.append(j.strip())	
                        if i == (len(res)-1):
                            itog_print += f"{j.strip()}, верно?"
                        else:
                            itog_print += f"{j.strip()}, "
                print(itog_print)
                return [res2, itog_print]

            def chose_TEST(message, index_of_pred):
                inputed_test_by_user = message.text
                fenix.array_to_del.append(message.message_id)
                print("User input:", inputed_test_by_user)
                parse_res = parse_num_of_tests(inputed_test_by_user)
                sms = bot.send_message(message.chat.id, text=parse_res[1], reply_markup=make_keyboard([['Да✅', 60],['Нет❌', index_of_pred+40]]))
                fenix.array_to_del.append(sms.id)
                fenix.array_of_num_tests_to_solve = parse_res[0]

            #@bot.callback_query_handler(func=lambda call: int(call.data) == 30) 
            #def ret(call):


            @bot.callback_query_handler(func=lambda call: int(call.data) == 60) 
            def start_to_solve_tests(call):
                sms = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text=f"✅Начинаю прорешивать тесты через 3...")
                x = 3
                time.sleep(1)
                while x != 1:
                    x = x - 1
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=sms.id, text=f"✅Начинаю прорешивать тесты через {x}...")
                    time.sleep(1)
                if del_msg(call.message.chat.id, [sms.id]):
                    print(f" ——> УДАЛЕНЫ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}, {call.message.message_id}]")
                else:
                    print(f" ——> ERROR: НЕ ПОЛУЧИЛОСЬ УДАЛИТЬ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}, {call.message.message_id}]")
                
                solve_test_by_indexes_of_tests(call)

            ##################### УДАЛЕНИЕ ПРОСТО ТАК ОТПРАВЛЕННЫХ СООБЩЕНИЙ
            @bot.message_handler(content_types=['text'])
            def reakcia_na_no_name_sms_from_user(message):
                print('''\n--—-----------------------------------------''')
                name = str(message.from_user.username) + "(" +str(message.from_user.id) +", " + str(message.chat.id) +")"
                print(f"\nПОЛУЧИЛ СМС от {name} (del через 2 секунды):", message.text)
                sms = bot.reply_to(message, text="Пожалуйста, пользуйтесь кнопками!\n(сообщения будут удалены через 2)" )#+ str(x) + " секунды)")
                x = 2
                time.sleep(1)
                while x != 1:
                    x = x - 1
                    bot.edit_message_text(chat_id=message.chat.id, message_id=sms.id, text="Пожалуйста, пользуйтесь кнопками!\n(сообщения будут удалены через "+ str(x) + ")")
                    time.sleep(1)
                #print("FORWARDING SMS")
                #sms3 = bot.forward_message(6239177054, message.chat.id, message.message_id)
                #sms3 = bot.send_message(6239177054, text=message.text)
                
                if del_msg(message.chat.id, [sms.id, message.message_id]):
                    print(f" ——> УДАЛЕНЫ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}, {message.message_id}]")
                else:
                    print(f" ——> ERROR: НЕ ПОЛУЧИЛОСЬ УДАЛИТЬ НЕНУЖНЫЕ СООБЩЕНИЯ:  [{sms.id}, {message.message_id}]")

            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
            ############################################################################################################################
                

            def solve_test_by_indexes_of_tests(call):
                        #несколько нужных переменных
                answers_complete = False
                
                #print(fenix.array_of_num_tests_to_solve) # введенные пользователем номера решаемых тестов
                #print(fenix.list_of_preds) #список всех предметов с номером
                #print('num of pred', fenix.num_of_pred)# номер указаного предмета
                #print('pred ->', fenix.list_of_preds[fenix.num_of_pred][1])#имя указанного предмета
                #print(fenix.list_of_vsex_testov)#список всех возможных тестов указанного предмета, где 0 - порядок, 1 - процент, 2 - беспантовый номер, и 3 - имя теста
                #print('\n')
                #for i in fenix.array_of_num_tests_to_solve:
                #    print(i, ' - ', fenix.list_of_vsex_testov[int(i)-1][3]) # имя теста по его порядковому номеру(индекс+1)
                
                
                #num_testing = index_of_test_ot
                #do_kakogo_testa_vkluchitelno = index_of_test_do
                
                array_of_num_tests_to_solve = fenix.array_of_num_tests_to_solve
                list_of_preds = fenix.list_of_preds    
                
                num_pred_r = fenix.num_of_pred
                name_pred_r = fenix.list_of_preds[fenix.num_of_pred][1]
                
                list_of_vsex_testov = fenix.list_of_vsex_testov
                
                
                result_solved_test = []
                errored_solved_test = 0
                del result_solved_test[:] 
                
                #идем решать указанные тесты
                counter = 0
                MAIN_SMS = [0 for i in range(len(array_of_num_tests_to_solve))]                                                                                               #СЧЕТЧИК ИЗ (ИНДЕКС+1)
                while counter < len(array_of_num_tests_to_solve):
                    num_testing = int(array_of_num_tests_to_solve[counter]) - 1  #ИНДЕКС РЕШАЕМОГО ТЕСТА
                    name_of_test = list_of_vsex_testov[num_testing][3]
                    
                    time_first_start_test = datetime.datetime.now() #чтобы в дальнейшем его вычесть из ожидания 
                    
                    ################################################
                    #################-ВХОДИМ-#######################
                    a = fenix.enter_current_test(num_pred_r, num_testing)  
                    
                    print(f"len of aray = {len(array_of_num_tests_to_solve)}")
                    print(f"MAIN SMS: {MAIN_SMS}")
                    
                    if MAIN_SMS[counter] == 0:
                        MAIN_SMS[counter] = bot.send_message(call.message.chat.id, 
                        text=f"🟡 {num_testing+1} тест \"{name_of_test}\"\n(1/6): Захожу на тест...")
                        fenix.array_to_del.append(MAIN_SMS[counter].id)
                    else:
                        MAIN_SMS[counter] = bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"🟡 {num_testing+1} тест \"{name_of_test}\"\n(1/6): Захожу на тест еще раз...")
                    
                    
                    soup = BeautifulSoup(a.text, 'html.parser')
                    proverka = False
                    
                    
                    ###################################################################
                    #0 - НУЖНА ЕЩЕ ОДНА ПРОВЕРКА - А ЗАШЛИ ЛИ МЫ ВООБЩЕ БЛЯТЬ НА НЕГО??
                    ###################################################################


                    # 1 проверка на Исчерпанный суточный лимит выполнения теста (или существует указанный тест вообще) 
                    b1 = soup.select('script[src^="/eport/WebResource.axd"] ~ script[type="text/javascript"]')
                    for i in range(len(b1)): 
                        if "Исчерпан суточный лимит выполнения теста" in b1[i].text:
                            print(f'\n--------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>"Исчерпан суточный лимит", тест {num_testing+1} по предмету')# \"{name_pred_r}\" (либо его не существует)!!!')
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"❌ {num_testing+1} тест \"{name_of_test}\"\n(-/-): Исчерпан суточный лимит для теста!")
                            #if (num_testing+1) <= do_kakogo_testa_vkluchitelno: 
                            #    print(f'{datetime.datetime.now().strftime("%H:%M:%S")}:——>Пробую решить следующий тест ({num_testing+2})...')
                            counter += 1
                            errored_solved_test += 1
                            answers_complete = False
                            proverka = True
                            break


                    # 2 проверка на уже прорешанный ранее тест с результатом меньше 70 %
                    b2 = soup.select('label[id="ctl00_MainContent_ASPxLabel10"]')
                    for i in range(len(b2)): 
                        if "Просмотр ответов заданий возможен только при выполнении не менее 70% теста" in b2[i].text:
                            print(f'\n--------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>"Просмотр ответов заданий возможен только при выполнении не менее 70%", тест {num_testing+1}, завершаю его!')
                            print(f'{datetime.datetime.now().strftime("%H:%M:%S")}:——>Пробую еще раз решить тест {num_testing+1}...')
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"❌ {num_testing+1} тест \"{name_of_test}\"\n(-/-): Тест уже решили менее чем на 70%")
                            
                            answers_complete = False                       
                            proverka = True
                            fenix.close_test_70_error()
                            break
                    

                    # 3 проверка на решенный ранее более чем на 70+ тест
                    b3 = soup.select('label[id="ctl00_MainContent_ASPxLabel8"]')
                    for i in range(len(b3)): 
                        if "Всего правильных ответов" in b3[i].text:
                            print(f'\n--------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>Тест {num_testing+1} уже был ранее прорешан на 70%+, завершаю его!')
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"✅ {num_testing+1} тест \"{name_of_test}\"\n(+/+): Уже был ранее прорешан на 70%+, завершаю его!")
                            
                            #if (num_testing+1) <= do_kakogo_testa_vkluchitelno: 
                            #   print(f'{datetime.datetime.now().strftime("%H:%M:%S")}:——>Пробую решить следующий тест ({num_testing+2})...')
                            counter += 1
                            answers_complete = False                      
                            proverka = True

                            b4 = soup.select('div[id="ctl00_MainContent_Panel1"] > label')
                            name_of_test = (b4[0].text).strip()
                            c = soup.select('label[id="ctl00_MainContent_ASPxLabel8"]')
                            num_non_smisl_of_test = (str(c[0].text)[20:]).strip()

                            result_solved_test.append([name_of_test, num_non_smisl_of_test, "70+"])

                            fenix.close_test(num_pred_r, num_testing)
                            break
                    
                    #Если проверка прошла успешно, то решаем данный тест
                    if proverka == True:
                        continue    
                    elif proverka == False:
                        
                        soup = BeautifulSoup(a.text, 'html.parser')
                        name_of_test = "Error_name" 
                        num_non_smisl_of_test = "Error_num_non_smisl_of_test"
                        try:
                            #name_of_pred = name_pred_r

                            b = soup.select('div[id="ctl00_MainContent_Panel1"] > label')
                            name_of_test = (b[0].text).strip()
                            
                        except Exception as e:
                            name_of_test ="Error_name" 

                            print(f"Не получилось узнать название теста: {e}\n\n")
                            print(a.text)
                            print("\n\n")
                        try:
                            c = soup.select('label[id="ctl00_MainContent_ASPxLabel8"]')
                            num_non_smisl_of_test = (str(c[0].text)[20:]).strip()
                        except Exception as e:
                            num_non_smisl_of_test = "Error_num_non_smisl_of_test"

                            print(f"Не получилось узнать номер теста : {e}\n\n")
                            print(a.text)
                            print("\n\n")
                        
                        
                        time_start_test = datetime.datetime.now()
                        print(f"\n--------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:Захожу на тест {num_testing+1} \"{str(name_of_test)[4:]}\" ({num_non_smisl_of_test})")
                        
                        
                        if answers_complete == False:
                            print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>1.ПРОБЕГАЮСЬ ПО ВОПРОСАМ...")
                            time.sleep(1)
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"🟡 {num_testing+1} тест \"{name_of_test}\"\n(2/6): Пробегаюсь по вопросам...")
                            
                            time_before = datetime.datetime.now()

                            if fenix.check_all_first_cases_and_verify():
                                pass

                            time_after = datetime.datetime.now()
                            time_elapsed = str(time_after-time_before)
                            for i in range(len(time_elapsed)):
                                if time_elapsed[i] == ".":
                                    time_elapsed = time_elapsed[i-2:i]
                                    if time_elapsed[0] == "0":
                                        time_elapsed = time_elapsed[1]
                                    break
                            print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Все вопросы протыканы! Заняло {(time_elapsed)} секунд")
                            
                            #Пятерочка
                            print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>2.ПРОРЕШИВАЮ ОТВЕТЫ ПЯТЕРОЧКИ ПО ТЕСТУ {num_testing + 1}:")
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"🟡 {num_testing+1} тест \"{name_of_test}\"\n(3/6): Прорешиваю ответы пятерочки...")
                            crytical_error = fenix.answer_all_questions()


                            #если зашли на пятерку раньше чем прорешали вопрос
                            if crytical_error == True:
                                print(f'\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>"!!! КРИТИЧЕСКАЯ ОШИБКА ВЫПОЛНЕНИЯ ТЕСТА, ЗАШЛИ НА ПЯТЕРКУ РАНЬШЕ ЧЕМ РЕШИЛИ ТЕСТ')
                                print(f'{datetime.datetime.now().strftime("%H:%M:%S")}:——>Пробую еще раз решить тест {num_testing+1}...')
                                answers_complete = False                       
                                continue

                            print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>3.ВСЕ ОТВЕТЫ УСПЕШНО ЗАПИСАНЫ")        
                            answers_complete=True
                        else:
                            print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:—————>3.ВНИМАНИЕ, ТЕСТ УЖЕ ПРОРЕШАН, НЕ ПРОРЕШИВАЮ ЕГО ЕЩЕ РАЗ!!!")

                        answers_complete=True

                        #ошибки
                        num_of_mistakes = random.randint(int(fenix.num_of_mistakes_ot), int(fenix.num_of_mistakes_do))
                        array_error = [['0', '0', '0', '0', '0'], ['U', 'U', 'U', 'U', 'U']]
                        print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Делаю ошибки — {num_of_mistakes}...")
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"🟡 {num_testing+1} тест \"{name_of_test}\"\n(4/6): Делаю ошибки - {num_of_mistakes}...")
                        fenix.select_question(1)
                        for i in range(num_of_mistakes):
                            fenix.check_some_case_and_next(array_error)



                        #готовися ждать
                        #time_first_start_test                                                                                        #start
                        time_end_of_start_test = datetime.datetime.now()                                                              #end
                        time_down = time_end_of_start_test-time_first_start_test                                                      #прошедшее время
                        time_to_wait = datetime.timedelta(seconds=(random.randint(int(fenix.time_to_wait_ot), int(fenix.time_to_wait_do))))     #указываем время в секундах которое надо было изначально подждать
                        if time_to_wait > time_down:
                            time_to_wait -= time_down                                                                                 #отнимаем от него уже прошедшее время

                            hours = int(str(time_to_wait).split(':')[0])
                            minutes = int(str(time_to_wait).split(':')[1])
                            seconds = int(str(time_to_wait).split(':')[2].split('.')[0])


                            time_to_wait = datetime.timedelta(seconds=seconds, minutes=minutes, hours=hours)
                            the_end = time_end_of_start_test + time_to_wait
                            #print(time_to_wait)


                            time_to_wait = seconds + minutes*60 + hours*3600 #КОТОРОЕ РЕАЛЬНО НУЖНО ЖДАТЬ

                            time_to_wait_min_for_print = f"{time_to_wait//60} минут {time_to_wait % 60} секунд"
                            print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Буду ждать {time_to_wait_min_for_print} до {the_end.strftime("%H:%M:%S")}...")
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"🟡 {num_testing+1} тест \"{name_of_test}\"\n(5/6): Буду ждать {time_to_wait_min_for_print} до {the_end.strftime("%H:%M:%S")}...")                
                            try:
                                for i in range(time_to_wait):
                                    time.sleep(1)
                            except KeyboardInterrupt:
                                print("Хорошо! Перестаю")

                            print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Время вышло! Заканчиваю тестирование...")
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"🟡 {num_testing+1} тест \"{name_of_test}\"\n(5/6): Время вышло! Заканчиваю тестирование...")            
                        
                        if fenix.close_test(num_pred_r=num_pred_r, num_testing=num_testing):
                            print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Тест закрыт успешно!")
                        
                        procent_solved = "Error" 

                        def get_result(num_pred_r, name_of_test, num_of_mist=0):
                            try:
                                if num_of_mist <=5:
                                    num_of_mist += 1
                                    #time.sleep(6)
                                    results_array = fenix.check_all_results_of_tests_by_num_of_pred(num_of_pred=num_pred_r)
                                    for j in range(len(results_array)-1): #j += 1
                                        j += 1
                                        if str(results_array[j][0].text).strip() in str(name_of_test):
                                            procent_solved = str(results_array[j][1].text).strip()
                                            #print(f"---------------> \"{procent_solved}\"")
                                            if procent_solved == "0":
                                                #значит тест не завершился еще
                                                print(f"Внимание, с {num_of_mist}/5 раза тест не завершился, пробую еще раз...")
                                                fenix.close_test(num_pred_r, num_testing)
                                                return get_result(num_pred_r, name_of_test, num_of_mist=num_of_mist)
                                            else:
                                                return procent_solved
                                        print("Error123, try again")
                                        return False 
                                    

                                    print("\n!!!!!!!!!чтото пошло не так при загрузке резов теста, возвращаю hui")
                                    return "hui"
                                else:
                                    return "Error123454575656345#"          
                            except Exception :
                                print("Error456, try again") 
                                return False
                        
                        procent_solved = get_result(num_pred_r, name_of_test) 

                            
                        print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>4.Тест {num_testing+1} \"{str(name_of_test)[4:]}\" завершён на {procent_solved}% (должно быть {round(((30-num_of_mistakes)/30)*100, 2)}%)")
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=MAIN_SMS[counter].id, text=f"✅ {num_testing+1} тест \"{name_of_test}\"\n(6/6): завершён на {procent_solved}% (должно быть {round(((30-num_of_mistakes)/30)*100, 2)}%)")
                        
                        answers_complete = False
                        counter += 1
                        result_solved_test.append([str(name_of_test)[4:], num_non_smisl_of_test, procent_solved])

                        try:
                            for i in range(10):
                                time.sleep(1)
                        except KeyboardInterrupt:
                            print("Хорошо! Перестаю")

                

                
                ##################################################################
                ########################---RESULT---##############################
                ##################################################################
                if len(result_solved_test) != 0:
                    print(f"\n--------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>Все указанные тесты прорешаны:")
                    itog_print = "Прорешано тестов:\n"
                    for i in range(len(result_solved_test)):
                        res = f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>✅{i+1}. {result_solved_test[i][0]} ({result_solved_test[i][1]}) — на {result_solved_test[i][2]}%"
                        print(res)
                        itog_print = itog_print + f"✅ {i+1}. {result_solved_test[i][0]} ({result_solved_test[i][1]}) — на {result_solved_test[i][2]}" + "\n"
                    itog_print += f"Итого ошибок: {errored_solved_test}"
                    print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:——>Итого ошибок: {errored_solved_test}")
                else:
                    print("\n--------------------------------------------------\nE—————————>6.Ни один тест не был прорешан :(")
                    print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:——>Итого ошибок: {errored_solved_test}")
                print("\n\n")

                time.sleep(1.5)
                del_msg(call.message.chat.id, fenix.array_to_del)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=array_message[call.message.chat.id][0], 
                    text=f"""Итоговый результат:\n{itog_print}""", reply_markup=make_keyboard([["Вернуться в меню", "-1"]]))  
                del result_solved_test[:]
            
            
            
            
            
            
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################
            ######################################################################################################################################      
            
            try:
                print('\n-------------------------------------------------- \nЗапускаю бота! Общайтесь с ним через свой любимый Telegram!\n!!!Чтобы прервать его работу нажмите Ctrl+C либо на интерактивную кнопку в самом боте')
                num_of_error = 1
                num_of_error_at_all = 100
                while True:
                    if QUIT_BOT == False:
                        try:
                            bot.polling(timeout=50, skip_pending=True)#, none_stop=True)#, restart_on_change=True)
                            print("hzhzhhzhzhhzhzhzzzhzhzhzhhh")
                            num_of_error = 1
                        except requests.exceptions.ConnectionError as E:
                            if num_of_error <= num_of_error_at_all:
                                #print(f"\n!!!Проблема с интернетом 1, пробую еще раз через 2 секунды ({num_of_error}/{num_of_error_at_all})...")
                                print(f"\n!!!Проблема с интернетом 1 ({str(E)}), пробую еще раз через 3 секунды ({num_of_error}/{num_of_error_at_all})...")
                                num_of_error += 1
                                time.sleep(3)
                            else:
                                print("\n--------------------------------------------------\nНе получается переподключиться, выхожу!!\n")
                                QUIT_BOT = True
                                bot.stop_bot()
                                break
                                #quit()
                        except KeyboardInterrupt:
                            print("\n--------------------------------------------------\nБот остановлен!\n")
                            #QUIT_BOT = True
                            bot.stop_bot()
                            print("Понял, ВЫКЛЮЧАЮСЬ!")
                            break
                            #quit()
                        except Exception as E:
                            if "Unauthorized" in str(E):
                                print("\nВ ТОКЕНЕ ОШИБКА! Попробуйте изменить его...")
                                break    
                            else:
                                print(f"!!!!!!!!!!!!!!!\n—> 2 КРИТИЧЕСКАЯ! ОШИБКА! КОТОРУЮ! Я! ВИЖУ! ВПЕРВЫЕ!, СООБЩИ! ОБ! ЭТОМ! АДМИНУ!!!!!!!!!!!!, текст ошибки: {str(E)}")
                                QUIT_BOT = True
                                quit()
                        except Exception as E:
                            if num_of_error <= num_of_error_at_all:
                                #print(f"\n!!!Проблема с чем-то, пробую еще раз через 2 секунды ({num_of_error}/{num_of_error_at_all})...")
                                print(f"\n!!!Проблема с чем-то ({str(E)}), пробую еще раз через 3 секунды ({num_of_error}/{num_of_error_at_all})...")
                                num_of_error += 1
                                time.sleep(3)
                            else:
                                print("\n--------------------------------------------------\nНе получается переподключиться, выхожу!!\n")
                                QUIT_BOT = True
                                bot.stop_bot()
                                break
                                #quit()
                    else:
                        print(f"QUIT_BOT == True, выхожу..")
                        bot.stop_bot()
                        sys.exit(0)
                        quit()
                        

                #print("\n--------------------------------------------------\nБот остановлен!\n")
            except ValueError:
                print("2 В ТОКЕНЕ ОШИБКА! Попробуйте изменить его...")
                continue
            except KeyboardInterrupt:
                print("\n--------------------------------------------------\nБот остановлен!\n")
                try:
                    QUIT_BOT = True
                    bot.stop_bot()
                except Exception:
                    pass
                print("Понял, ВЫКЛЮЧАЮСЬ!")
                continue
            except Exception as E:
                if "Unauthorized" in str(E):
                    print("В ТОКЕНЕ ОШИБКА! Попробуйте изменить его...")
                    continue   
                else:
                    print(f"!!!!!!!!!!!!!!!\n—> 2 КРИТИЧЕСКАЯ! ОШИБКА! КОТОРУЮ! Я! ВИЖУ! ВПЕРВЫЕ!, СООБЩИ! ОБ! ЭТОМ! АДМИНУ!!!!!!!!!!!!, текст ошибки: {str(E)}")
                    continue
        except KeyboardInterrupt:
            print("\n--------------------------------------------------\nБот остановлен!\n")
            try:
                QUIT_BOT = True
                bot.stop_bot()
            except Exception:
                pass
            continue
        except Exception as E:
            if "Unauthorized" in str(E):
                print("В ТОКЕНЕ ОШИБКА! Попробуйте изменить его...")
                continue  
            else:
                print(f"!!!!!!!!!!!!!!!\n—> 3 КРИТИЧЕСКАЯ! ОШИБКА! КОТОРУЮ! Я! ВИЖУ! ВПЕРВЫЕ!, СООБЩИ! ОБ! ЭТОМ! АДМИНУ!!!!!!!!!!!!, текст ошибки: {str(E)}")
                try:
                    QUIT_BOT = True
                    bot.stop_bot()
                except Exception:
                    pass
                continue
