#Добро пожаловать в исходный код!
#Любознательность - наше всё!!!

#1. возвращен requests (+)
#2. есть проверка на ошибки, но не весь пользовательский ввод проверяется достаточно
#3. есть гит (+)
#4. нет парсера ввода номеров тестов
#5. нет тг бота
#6. нет защиты от временного дисконекта (+)
#7. дима пошел нахер (+++)

import os, subprocess
import requests
import time, random, datetime, timedelta, string
from bs4 import BeautifulSoup
from urllib.parse import quote
import prikoli


#Функции для работы с сессией
headers1 = prikoli.headers1
SessionId=""
def get_new_session_id():
    a = requests.get("http://eport.fesmu.ru/eport/eport/Default.aspx", headers=headers1)
    try:
        set_cookies = str(a.headers["Set-Cookie"]).strip()
        if "ASP.NET_SessionId" in set_cookies:
            set_cookies = set_cookies[(set_cookies.find("ASP.NET_SessionId") + 18):(set_cookies.find(';'))]
            return set_cookies
    except KeyError:
        print("Попробуйте с включенным интернетом!")
        quit()
def set_new_session_id():
    global SessionId
    SessionId = get_new_session_id()
    if SessionId != "":
        return True
    else:
        return False
def get_cookies():
    global SessionId
    cookies1 = {
    "_ym_d":"1746367815",
    "_ym_uid":"174636781563597601",
    "_ym_isad":"2",
    "_ym_visorc":"w",
    "ASP.NET_SessionId":SessionId,
}
    return cookies1


#Главная функция аутентификации
gay_words = prikoli.gay_words
def make_a_request(url, data, silens=True, streaming=False, num_of_error=0, auth=False, get_request=False):
    num_of_error=num_of_error
    try:
        if get_request == True:
            time.sleep(1)
            a = requests.get(url, headers=headers1, cookies=get_cookies(), stream=streaming)            #ДЛя GET-запросов
        else:
            time.sleep(1)       
            a = requests.post(url, data=data, headers=headers1, cookies=get_cookies(), stream=streaming) #Для POST-запросов
    except Exception as E:
        print(f'''\n----------------------------ERROR-------------------------------------------''')
        for x in range(len(gay_words)):
            if str(gay_words[x]) in str(E):
                num_of_error += 1
                num_of_error_vsego = 50
                if num_of_error <= num_of_error_vsego:
                    print(f"ПЛОХОЕ ИНТЕРЕНЕТ СОЕДИНЕНИЕ!!! Пробую ещё раз через 10 секунд({num_of_error}/{num_of_error_vsego})...\nGay Word: {gay_words[x]}")
                    time.sleep(10)
                    return make_a_request(url, data, silens, streaming, num_of_error=num_of_error)
                else:
                    print(f"НЕ ПОЛУЧАЕТСЯ АВТОРИЗОВАТЬСЯ, проверьте подключение к интернету!!!\n—————>Выхожу...")
                    quit()  #return False
        print(f"НЕИЗВЕСТНАЯ ФАТАЛЬНАЯ ОШИБКА, \nописание: {E}\n—————>Выхожу...")
        quit() #return False


    def test_na_diskonekt_izza_istekshey_sessii(a):
        soup = BeautifulSoup(a.text, 'html.parser')
        
        b1 = soup.select('h1[id="ctl00_MainContent_Label1"]')
        for i in range(len(b1)):
            if "На портале могут работать только зарегистрированные пользователи" in b1[i].text:
                print("!!!СРАБОТАЛ ДИСКОННЕКТ, ПЕРЕПОДКЛЮЧАЮСЬ")
                return False
            
        b2 = soup.select('script[type="text/javascript"]')
        for i in range(len(b2)):
            if "необходима авторизация" in b2[i].text:
                print("!!!СРАБОТАЛ ДИСКОННЕКТ, ПЕРЕПОДКЛЮЧАЮСЬ")
                return False
        return True

    if test_na_diskonekt_izza_istekshey_sessii(a):
        if silens==False:
            print("\n\n\n-----------------------------------------------------------------------------------------------1")
            print(a.status_code)
            print("-----------------------------------------------------------------------------------------------2")
            print(a.text)
        return a
    else:
        print(f'''\n----------------------------ERROR-------------------------------------------''')
        if auth == True:
            print("Error, неправильный логин или пароль!!!\n—————>Выхожу...")
            quit() #return False
        else:
            #print(f"НУЖНА АВТОРИЗАЦИЯ ДЛЯ ДЛЯ РАБОТЫ ПО ССЫЛКЕ: {url}!!! Пробую перезайти в аккаунт и продолжить работу...\n")
            #if auth():
            #    make_a_request(url, data, silens, streaming)
            #else: 
            num_of_error+=1
            num_of_error_vsego = 10
            if num_of_error <= num_of_error_vsego:
                print(f"\nСДОХЛА СЕССИЯ {get_login()}:{get_pass()}!!! Пробую ещё раз через 10 секунд ({num_of_error}/{num_of_error_vsego})")
                time.sleep(10)
                auth(silence=True) 
                return make_a_request(url, data, silens, streaming, num_of_error=num_of_error)
            else:
                print("Не получается авторизоваться, проверьте подключение к интернету!!!\n—————>Выхожу...")
                quit() #return False


#Парочка функций для работы с файлами и выводом
def user_input(str1):
    res = input(str1)
    if res == "admin":
        admin()
        return False
    else:
        return res
def set_login_pass(login1, pass1):
    with open("pass_file", "w+") as file:
        file.write(f"{login1}\n{pass1}")
    return True 
def get_login():
    try:
        with open("pass_file", "r") as file:
            arr = file.readlines()
            return arr[0].strip()
    except FileNotFoundError:
        return False
def get_pass():
    try:
        with open("pass_file", "r") as file:
            arr = file.readlines()
            return arr[1].strip()
    except FileNotFoundError:
        return False




#Авторизация
#POST /eport/eport/Default.aspx
# возвращает тру\фолс
def auth(login1="", password1="", silence=False):
    if set_new_session_id():
        if silence == False:
            print(f"Session ID({SessionId}) установлен, пытаюсь войти...")
        if (login1 == "") and (password1 == ""):
            login1 = get_login()
            password1 = get_pass()
            if (login1 == False) or (password1 == False):
                print("ERROR, НЕ СУЩЕСТВУЕТ ФАЙЛА С ЛОГИНОМ И ПАРОЛЕМ!!!\n—————>Выхожу...")
                quit()
        else:
            print(f"Пробую зайти в аккаунт {login1}:{password1}...\n")
        data_auth = f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKLTM5Mjc2OTQzMQ9kFgJmD2QWAgIDD2QWAgIBD2QWAgIFDw8WAh4EVGV4dAXQAtCX0LAg0YHRg9GC0LrQuCDRg9C90LjQutCw0LvRjNC90YvRhSDQsNCy0YLQvtGA0LjQt9C40YDQvtCy0LDQvdC90YvRhSDQv9C%2B0LvRjNC30L7QstCw0YLQtdC70LXQuSDQvdCwINC%2F0L7RgNGC0LDQu9C1OiA3NzAgIDxiciAvPtCh0YDQtdC00L3QtdC1INCy0YDQtdC80Y8g0LLRi9C%2F0L7Qu9C90LXQvdC40Y8gMSDQt9Cw0LTQsNC90LjRjyDQv9C%2B0YHQu9C10LTQvdC40YUgNTAg0YDQtdC30YPQu9GM0YLQsNGC0LjQstC90YvRhSDRgtC10YHRgtC%2B0LIgMTQg0YHQtdC60YPQvdC0PGJyLyA%2B0KHQtdC50YfQsNGBINC%2F0L7QtNC60LvRjtGH0LXQvdC40Lkg0Log0L%2FQvtGA0YLQsNC70YM6IDYzMWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMWYnd7fFZyValq0x%2B30B7kDIWqfTBgE1HUa5%2Fne5VLQz&__VIEWSTATEGENERATOR=73D4C735&__EVENTVALIDATION=%2FwEdAANykW%2Fz6ZjgBrPJhiB0FU0SUN0eEH6RAZcaSKVdt8S4X7osef1mutGT26WuFCdWwFZsovP8KXv0BZyweEkBDqJpWQ1Mw3YxYEw8xGAX44%2FbtA%3D%3D&ctl00%24MainContent%24UserText={login1}&ctl00%24MainContent%24PassText={password1}&ctl00%24MainContent%24ASPxButton1=&DXScript=1_42%2C1_75%2C2_27"
        
        #print(data_auth)
        #data_auth = data_auth.encode('utf-8')
        requst1 = make_a_request("http://eport.fesmu.ru/eport/eport/Default.aspx", data_auth, auth=True)#, start=True)
        soup = BeautifulSoup(requst1.text, 'html.parser')
        b = soup.select('span[id="ctl00_MainContent_Label1"]')
        if len(b) > 0:
            if "Здравствуйте" in b[0].text:
                #print("\n---------------------------------------------------------------")
                if silence == False:
                    print(f'\n{str(b[0].text)[:-33]}!')
                return True
            else:
                print(f"ERROR AUTH (1) < error: {b}")
                return False
        print("Ошибка, не получилось войти в аккаунт, попробуйте еще раз!!!")
        return False
    else:
        print("Проверьте подключение к интернету")
        quit()

#Войти в тест с известным num_pred и num_test
#POST /eport/eport/studtst1.aspx HTTP/1.1
def enter_current_test(num_of_pred=0, num_of_test=0):
    num_of_pred = str(num_of_pred)
    num_of_test = str(num_of_test)
    data_enter_current_test=f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUIOTk1NDMwOTQPZBYCZg9kFgICAw9kFgJmD2QWAgIJD2QWBAIDD2QWAmYPZBYCZg9kFgJmD2QWAgIBDxQrAAUPFgIeD0RhdGFTb3VyY2VCb3VuZGdkZGQ8KwAHAQYPZBAWAgIBAgIWAhQrAAEWAh4PQ29sVmlzaWJsZUluZGV4ZhQrAAEWAh8BAgFkFgBkAgcPZBYCZg9kFgJmD2QWAmYPZBYCAgEPFCsABWRkZDwrAAcBBg9kEBYCZgIBFgIUKwABFgIfAWYUKwABFgIfAQIBZBYAZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjcFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjm6%2BEbUEKpaxmSv00E%2B%2FJiuKcZ%2BYI%2BIkpp3rzk2vaUFAA%3D%3D&__VIEWSTATEGENERATOR=847F47AD&__EVENTVALIDATION=%2FwEdAAeH8wh4QiiJKgOuKnFFkPWbI7ZJDWlRgaefdPW8BTEVtXw%2BikVKJJfrT0ndBbXKBTA39nUTQDb0GEkh6LDT5SpRsAIaIhbklmBqr8w%2BPxD292wBCiQy8HT9gxcspUtWdqpbDCDdUSb6jcSCho5zpwlSvNMTFvzkvoYxtvqO8J0ljItyMFkzxVGQu2RBvSrJ7No%3D&ctl00%24MainContent%24hfPred={num_of_pred}&ctl00%24MainContent%24hfTest={num_of_test}&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2DeletedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2InsertedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel1%24ASPxListBox2=System.Data.DataRowView&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3DeletedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3InsertedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel2%24ASPxListBox3=System.Data.DataRowView&ctl00%24MainContent%24ASPxButton1=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C1_41%2C2_36"
    a  = make_a_request("http://eport.fesmu.ru/eport/eport/studtst1.aspx", data_enter_current_test)
    return a

#Выбрать тест из списка и войти в него
#POST /eport/eport/startstu.aspx HTTP/1.1  - 1 
#POST /eport/eport/studtst1.aspx HTTP/1.1  - 2
def chose_some_test_from_list():
    result = []
    del result[:]

    #Подгружаем список предметов
    data_chose_some_test_from_list1 ="------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ToolkitScriptManager1_HiddenField\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__EVENTTARGET\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__EVENTARGUMENT\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__VIEWSTATE\"\x0d\x0a\x0d\x0a/wEPDwUKMTE4NDI1MjM5MQ9kFgJmD2QWAgIDD2QWAmYPFgIeB2VuY3R5cGUFE211bHRpcGFydC9mb3JtLWRhdGEWBgIPD2QWDAIBDw8WAh4EVGV4dAWCAdCX0LTRgNCw0LLRgdGC0LLRg9C50YLQtSAg0KHQotCQ0J3QmNCh0JvQkNCSINCh0KLQkNCd0JjQodCb0JDQktCe0JLQmNCnLCDQstGL0LHQtdGA0LjRgtC1INC90YPQttC90YvQuSDRgNCw0LfQtNC10Lsg0YDQsNCx0L7RgtGLOiBkZAILDw8WAh8BBRw8dGFibGUgY2xhc3M9J21lc3MnPjwvdGFibGU+ZGQCDQ8PFgIfAQXaCTx0YWJsZSBjbGFzcz0nbWVzcyc+PHRyPjx0ZD48YSBocmVmPSdSZWFkTXNnLmFzcHg/aWQ9MjEwMDA2Jz7QlNCXINC6INGC0LXQvNC1IDEzLCAi0J/QsNC70LvQuNCw0YIuINC/0L7QvNC+0YnRjCIsINC30LDRh9C10YIsIDQg0YHQtdC80LXRgdGC0YAuPC9hPjwvdGQ+PHRkPjA0LjA1LjIwMjUgMTU6MDc8L3RkPjx0ZD48aW1nIHNyYz0ncGZpbGUuZ2lmJyBhbHQ9J9CY0LzQtdC10YLRgdGPINCy0LvQvtC20LXQvdC90YvQuSDRhNCw0LnQuycvPjwvdGQ+PHRkPiA8L3RkPjwvdHI+PHRyPjx0ZD48YSBocmVmPSdSZWFkTXNnLmFzcHg/aWQ9MjA5NjUxJz7QniDRgtC10LvQtdCz0YDQsNC8LdC60LDQvdCw0LvQtTwvYT48L3RkPjx0ZD4yOC4wNC4yMDI1IDE1OjA2PC90ZD48dGQ+PC90ZD48dGQ+PHNwYW4gc3R5bGU9ImNvbG9yOiAjMDA4ODAwIj4o0J/RgNC+0YHQvNC+0YLRgCAzMC4wNC4yMDI1IDEyOjAyKTwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD48YSBocmVmPSdSZWFkTXNnLmFzcHg/aWQ9MjA5NDk0Jz7QlNC+0LzQsNGI0L3QtdC1INC30LDQtNCw0L3QuNC1INC00LvRjyDQn9CXIOKEliAxMiwg0KHQlDwvYT48L3RkPjx0ZD4yNS4wNC4yMDI1IDE3OjU5PC90ZD48dGQ+PGltZyBzcmM9J3BmaWxlLmdpZicgYWx0PSfQmNC80LXQtdGC0YHRjyDQstC70L7QttC10L3QvdGL0Lkg0YTQsNC50LsnLz48L3RkPjx0ZD4gPC90ZD48L3RyPjx0cj48dGQ+PGEgaHJlZj0nUmVhZE1zZy5hc3B4P2lkPTIwODY4MSc+0JPQn9C10YDQtdC90L7RgSDQvtGC0YDQsNCx0LDRgtGL0LLQsNC90LjRjyDQt9Cw0L3Rj9GC0LjRjy48L2E+PC90ZD48dGQ+MDguMDQuMjAyNSAxNDo0NDwvdGQ+PHRkPjwvdGQ+PHRkPjxzcGFuIHN0eWxlPSJjb2xvcjogIzAwODgwMCI+KNCf0YDQvtGB0LzQvtGC0YAgMTAuMDQuMjAyNSAyMzoxMSk8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+PGEgaHJlZj0nUmVhZE1zZy5hc3B4P2lkPTIwODYyNCc+0JTQvtC80LDRiNC90LXQtSDQt9Cw0LTQsNC90LjQtSDQtNC70Y8g0J/QlyDihJYxMSwg0KHQlC4gMiDQuiwg0JvQpDwvYT48L3RkPjx0ZD4wNy4wNC4yMDI1IDE2OjE3PC90ZD48dGQ+PGltZyBzcmM9J3BmaWxlLmdpZicgYWx0PSfQmNC80LXQtdGC0YHRjyDQstC70L7QttC10L3QvdGL0Lkg0YTQsNC50LsnLz48L3RkPjx0ZD48c3BhbiBzdHlsZT0iY29sb3I6ICMwMDg4MDAiPijQn9GA0L7RgdC80L7RgtGAIDExLjA0LjIwMjUgMTI6NTgpPC9zcGFuPjwvdGQ+PC90cj48L3RhYmxlPmRkAg8PFCsABg8WAh8BBSPQn9GA0LXQtNGL0LTRg9GJ0LjQuSDRgdC10LzQtdGB0YLRgGRkZGRkPCsABgEAFgIeEVNwcml0ZUNzc0ZpbGVQYXRoBSR+L0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAhEPPCsABQEADxYCHgVWYWx1ZQUBM2RkAhUPDxYCHwEFigLQn9GA0Lgg0L3QtdC+0LHRhdC+0LTQuNC80L7RgdGC0Lgg0YDQsNCx0L7RgtGLINGBINGC0LXRgdGC0LDQvNC4INC40LvQuCDQt9Cw0LTQsNGH0LDQvNC4INC/0YDQtdC00YvQtNGD0YnQuNGFINGB0LXQvNC10YHRgtGA0L7QsiAtINCy0LLQtdC00LjRgtC1INC90YPQttC90YvQuSDRgdC10LzQtdGB0YLRgCwg0LrQu9C40LrQvdC40YLQtSDRjdGC0YMg0LrQvdC+0L/QutGDLCDQt9Cw0YLQtdC8INCy0YvQsdC10YDQuNGC0LUg0L3Rg9C20L3Ri9C5INGA0LDQt9C00LXQu2RkAhEPPCsABQEADxYCHwMFATRkZAITD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWBAILDxQrAAUPFgIeD0RhdGFTb3VyY2VCb3VuZGdkZGQ8KwAHAQYPZBAWAWYWARQrAAEWAh4PQ29sVmlzaWJsZUluZGV4ZmQWAGQCDQ9kFgJmD2QWAmYPZBYCZg9kFgICAQ8UKwAFZGRkPCsABwEGD2QQFgFmFgEUKwABFgIfBWZkFgBkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYSBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTgFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjExBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTMFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b243BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMQUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjIFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b240BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE2BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjAFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xNAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjYFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24zBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTcFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xOQUjY3RsMDAkTWFpbkNvbnRlbnQkQVNQeFBvcHVwQ29udHJvbDEFMGN0bDAwJE1haW5Db250ZW50JEFTUHhQb3B1cENvbnRyb2wxJEFTUHhCdXR0b24xMtz5qfbiMbMeISAR/QvG06v5dpRCChvKqSK05ZSRup7m\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__VIEWSTATEGENERATOR\"\x0d\x0a\x0d\x0a556E0939\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"__EVENTVALIDATION\"\x0d\x0a\x0d\x0a/wEdAAsLNa6a+9G22QqI86rItVBI05GkTiFJ5RGCGZo4MFlAWmJX/zM4Fq62BChlnvEOcV3H/Y6Ii2DoqGxCrv3qHaubI7ZJDWlRgaefdPW8BTEVtfksz20s2aJuEs5x2iFvUXC/Cz5d6MynVZDCnI40CgFMDJH1HO5EJDXub4y4Eu52UlPcgdOU1mpwY+veTx5eZwxMbGvsjNRUDd20juN1ZU1pJbOyFoUUWZYCdLvCz9c8nk/PEZpnaVcCpNnaj/+3aAnk78Bg6t2TRTu0+rVkX32c\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hftxdescr\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hftyp\"\x0d\x0a\x0d\x0a0\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hftxt\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hfPred\"\x0d\x0a\x0d\x0a-1\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hfPrep\"\x0d\x0a\x0d\x0a-1\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$hfSem\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxTextBox2\"\x0d\x0a\x0d\x0a3\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxButton5\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxTextBox3\"\x0d\x0a\x0d\x0a4\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1WS\"\x0d\x0a\x0d\x0a0:0:-1:50:-10000:0:955px:500px:1\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$ASPxTextBox1\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$ASPxMemo1\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxListBox1DeletedItems\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxListBox1InsertedItems\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxListBox1CustomCallback\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$ASPxListBox1\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxCallbackPanel_ASPxListBox3DeletedItems\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxCallbackPanel_ASPxListBox3InsertedItems\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00_MainContent_ASPxPopupControl1_ASPxCallbackPanel_ASPxListBox3CustomCallback\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$ASPxCallbackPanel$ASPxListBox3\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"ctl00$MainContent$ASPxPopupControl1$FileUpload1\"; filename=\"\"\x0d\x0aContent-Type: application/octet-stream\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB\x0d\x0aContent-Disposition: form-data; name=\"DXScript\"\x0d\x0a\x0d\x0a1_42,1_75,2_27,2_34,2_41,1_68,1_65,2_36,1_41,2_40\x0d\x0a------WebKitFormBoundarynaBB3GGbJd0GJGGB--\x0d\x0a"
    a = make_a_request("http://eport.fesmu.ru/eport/eport/startstu.aspx", data_chose_some_test_from_list1)
    soup = BeautifulSoup(a.text, 'html.parser')
    pred_list = soup.select('table[id="ctl00_MainContent_ASPxPopupControl1_ASPxListBox1_LBT"] > tr > td ')
    #Выводим его и спрашиваем предмет
    print("\n---------------------------------------------------------------\nДоступные вам тесты:")
    for i in range(len(pred_list)):
        num = str(i+1)
        space = ""
        if i < 9: space += " "
        print(f"\t{num}.{space} {pred_list[i].text}") 
    print("\t0.  Вернуться в меню") 
    try:
        num_of_pred = int(user_input("\nВыберите предмет из списка: ")) - 1
    except ValueError:
        print("hui1")
        return False
    if num_of_pred == -1:
        return -1
    if (num_of_pred > (len(pred_list)-1)) or (num_of_pred < 0):
        print("hui2")
        return False
    
    
    #Подгружаем список тестов
    data_chose_some_test_from_list2 = f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUIOTk1NDMwOTQPZBYCZg9kFgICAw9kFgJmD2QWAgIJD2QWBAIDD2QWAmYPZBYCZg9kFgJmD2QWAgIBDxQrAAUPFgIeD0RhdGFTb3VyY2VCb3VuZGdkZGQ8KwAHAQYPZBAWAgIBAgIWAhQrAAEWAh4PQ29sVmlzaWJsZUluZGV4ZhQrAAEWAh8BAgFkFgBkAgcPZBYCZg9kFgJmD2QWAmYPZBYCAgEPFCsABWRkZDwrAAcBBg9kEBYCZgIBFgIUKwABFgIfAWYUKwABFgIfAQIBZBYAZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjcFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjm6%2BEbUEKpaxmSv00E%2B%2FJiuKcZ%2BYI%2BIkpp3rzk2vaUFAA%3D%3D&__VIEWSTATEGENERATOR=847F47AD&__EVENTVALIDATION=%2FwEdAAeH8wh4QiiJKgOuKnFFkPWbI7ZJDWlRgaefdPW8BTEVtXw%2BikVKJJfrT0ndBbXKBTA39nUTQDb0GEkh6LDT5SpRsAIaIhbklmBqr8w%2BPxD292wBCiQy8HT9gxcspUtWdqpbDCDdUSb6jcSCho5zpwlSvNMTFvzkvoYxtvqO8J0ljItyMFkzxVGQu2RBvSrJ7No%3D&ctl00%24MainContent%24hfPred={num_of_pred}&ctl00%24MainContent%24hfTest=100&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2DeletedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2InsertedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel1%24ASPxListBox2=System.Data.DataRowView&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3DeletedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3InsertedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel2%24ASPxListBox3=System.Data.DataRowView&ctl00%24MainContent%24ASPxButton1=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C1_41%2C2_36"
    a2 = make_a_request("http://eport.fesmu.ru/eport/eport/studtst1.aspx", data_chose_some_test_from_list2)
    soup = BeautifulSoup(a2.text, 'html.parser')
    test_num_list = soup.select('table[id="ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3_LBT"] > tr > td[class="dxeListBoxItem_Aqua dxeFTM"]')
    test_name_list = soup.select('table[id="ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3_LBT"] > tr > td[class="dxeListBoxItem_Aqua dxeLTM"]')
    
    new_list_of_persent = [[0 for i in range(len(test_name_list))], [0 for i in range(len(test_name_list))]]
     
    #нужно сравнить имена всех тестов поочереди с имеющимися списком большой кучи уже решенных и выбрать тот где больше процент 
    results_array = check_all_results_of_tests_by_num_of_pred(num_of_pred=num_of_pred)
    for i in range(len(test_name_list)):
        for j in range(len(results_array)-1): #j += 1
            j += 1
            if str(results_array[j][0].text).strip() in str(test_name_list[i].text).strip():
                #print(f"SOVPADENIE NAIDENO: {str(results_array[j][0].text).strip()}  —>  {str(test_name_list[i].text).strip()}")
                if int(str(results_array[j][1].text).strip()) >= new_list_of_persent[0][i]: 
                    new_list_of_persent[0][i] = int(str(results_array[j][1].text).strip())
                    new_list_of_persent[1][i] = str(results_array[j][0].text).strip()

    
    #Выводим его и спрашиваем с какого по какой тест
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
        print(f"\t{num}.{space} ({persent}) {num_test} | {name_test}")
    
    print("\t0.  Вернуться в меню")
    try:
        num_of_test = int(user_input("\nC какого теста начать (по счёту): ")) - 1
        if num_of_test == -1:
            return -1
        if (num_of_test > (len(test_name_list)-1)) or (num_of_test < 0):
            print("hui3")
            return False
        do_kakogo_testa_vkluchitelno = int(user_input("До какого теста решать включительно: ")) - 1 #до какого теста  (начиная с нуля)
        if (do_kakogo_testa_vkluchitelno > (len(test_name_list)-1)) or (do_kakogo_testa_vkluchitelno < 0) or (do_kakogo_testa_vkluchitelno < num_of_test):
            print("hui4")
            return False
    except ValueError:
        print("hui5")
        return False
    
    
    
    
    
    name_of_pred = str(pred_list[num_of_pred].text).rstrip()
    result = [num_of_pred, num_of_test, do_kakogo_testa_vkluchitelno, str(pred_list[num_of_pred].text).strip(), [(test_num_list[i].text).strip() for i in range(len(test_num_list))], [(test_name_list[i].text).strip() for i in range(len(test_name_list))]]
    return result


#Выбрать вопрос
#POST /eport/eport/studtst2.aspx HTTP/1.1
def select_question(num_of_question="1"):
    data_select_question=f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTUwNzg4NDI2OQ9kFgJmD2QWAgIDD2QWAgIBD2QWAgIDD2QWQgIBDzwrAAQBAA8WAh4FVmFsdWUFUygyKSDQo9GF0L7QtCDQt9CwINCx0L7Qu9GM0L3Ri9C80Lgg0LIg0L%2FQtdGA0LjQvtC%2F0LXRgNCw0YLQuNCy0L3QvtC8INC%2F0LXRgNC40L7QtNC1ZGQCCQ88KwAEAQAPFgIfAAUr0JjQtNC10L3RgtC40YTQuNC60LDRgtC%2B0YAg0YLQtdGB0YLQsCAxMzczNWRkAgsPFCsABA8WAh8ABSvQktCw0Ygg0LvQuNC80LjRgiDQstGA0LXQvNC10L3QuCAxOCDQvNC40L0uZDwrAAwBABYEHglGb3JlQ29sb3IKTx4EXyFTQgIEZGRkAg8PFCsABmRkZGQ8KwAHAQAWBB4LQ3NzRmlsZVBhdGgFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHgpDc3NQb3N0Zml4BQRBcXVhPCsABgEAFgIeEVNwcml0ZUNzc0ZpbGVQYXRoBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAhEPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAITDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCFQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAhcPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIZDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCGw8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAh0PFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIfDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCIQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAiMPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIlDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCJw8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAikPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIrDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCLQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAi8PFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAIxDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCMw8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAjUPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAI3DxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCOQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAjsPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAI9DxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCPw8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAkEPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAJDDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQCRQ8UKwAGZGRkZDwrAAcBABYEHwMFIH4vQXBwX1RoZW1lcy9BcXVhL3swfS9zdHlsZXMuY3NzHwQFBEFxdWE8KwAGAQAWAh8FBSF%2BL0FwcF9UaGVtZXMvQXF1YS9BU1B4QnV0dG9uLnNraW5kAkcPFCsABmRkZGQ8KwAHAQAWBB8DBSB%2BL0FwcF9UaGVtZXMvQXF1YS97MH0vc3R5bGVzLmNzcx8EBQRBcXVhPCsABgEAFgIfBQUhfi9BcHBfVGhlbWVzL0FxdWEvQVNQeEJ1dHRvbi5za2luZAJJDxQrAAZkZGRkPCsABwEAFgQfAwUgfi9BcHBfVGhlbWVzL0FxdWEvezB9L3N0eWxlcy5jc3MfBAUEQXF1YTwrAAYBABYCHwUFIX4vQXBwX1RoZW1lcy9BcXVhL0FTUHhCdXR0b24uc2tpbmQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFiEFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24wNAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjAyBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMDMFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMgUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjMFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b240BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNQUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjYFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b243BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjkFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xMAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjExBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTIFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xMwUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE0BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTUFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xNgUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE3BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTgFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xOQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjIwBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjEFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yMgUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjIzBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjQFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjI2BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjcFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yOAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjI5BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMzDtYe90Z6nu2QDSkLRvblOV03MTQ%2BTm0ytfqvbm%2BoOJjg%3D%3D&__VIEWSTATEGENERATOR=4F4B5F1E&ctl00%24MainContent%24ASPxButton{num_of_question}=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40"
    a = make_a_request("http://eport.fesmu.ru/eport/eport/studtst2.aspx", data_select_question)
    return a
#Тыкнуть первый и к следующему
#POST /eport/eport/studtst3.aspx HTTP/1.1
def check_first_and_next():
    data_check_first_and_next = "ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTI5MTM5NzM3Nw9kFgJmD2QWAgIDD2QWAmYPZBYCAg8PZBYSAgEPPCsABAEADxYCHgVWYWx1ZQUYKDIpINCf0L7Qt9C90LDQvdC40LUgLSAzZGQCBw88KwAEAQAPFgIfAAUQ0JfQsNC00LDQvdC40LUgMWRkAgkPFCsABA8WAh8ABSvQktCw0Ygg0LvQuNC80LjRgiDQstGA0LXQvNC10L3QuCAxOSDQvNC40L0uZDwrAAwBABYEHglGb3JlQ29sb3IKTx4EXyFTQgIEZGRkAgsPDxYCHgRUZXh0BXombmJzcDvQrdC80L%2FQuNGA0LjRh9C10YHQutC40LUg0LzQtdGC0L7QtNGLINC90LDRg9GH0L3QvtCz0L4g0LjRgdGB0LvQtdC00L7QstCw0L3QuNGPINC40YHQutC70Y7Rh9Cw0Y7RgjombmJzcDsmbmJzcDsgPGJyPmRkAg8PDxYCHwMFHiZuYnNwOzEuINC90LDQsdC70Y7QtNC10L3QuNC1O2RkAhMPDxYCHwMFICZuYnNwOzIuINGN0LrRgdC%2F0LXRgNC40LzQtdC90YI7ZGQCFw8PFgIfAwUhJm5ic3A7My4g0YTQvtGA0LzQsNC70LjQt9Cw0YbQuNGOZGQCGw8PFgIfAwUcJm5ic3A7NC4g0YHRgNCw0LLQvdC10L3QuNC1LmRkAh8PDxYCHwMFGyZuYnNwOzUuINC40LfQvNC10YDQtdC90LjQtWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjA0%2Bk22ByzKq5L7zouSrrJbMziS20QR38bdXSKqlADvvqw%3D&__VIEWSTATEGENERATOR=A8B80323&__EVENTVALIDATION=%2FwEdAAc%2FlZpllc25PN%2BYPogZdEuvCa17vhDUriBurXCsNy590WMU%2Ff8RYiHeDshdCQG6KXsl%2BbxYKsnWKi1oDF%2BSPbsJHS3vs9PY66cqRnl9zzvdQgrZ%2B0y1djOQFJQdjlbLnVhP%2FHXZRS6bBCR%2FaTH01z%2B9bOik%2B0yMqvUzm3kYLHgnd9IAIvs1oV7es8UR7FcUYQ4%3D&ctl00%24MainContent%24hfo1=1&ctl00%24MainContent%24hfo2=0&ctl00%24MainContent%24hfo3=0&ctl00%24MainContent%24hfo4=0&ctl00%24MainContent%24hfo5=0&ctl00%24MainContent%24hf1=0&ctl00%24MainContent%24ASPxButton5=&ctl00%24MainContent%24ASPxCheckBox1=C&ctl00%24MainContent%24ASPxCheckBox2=U&ctl00%24MainContent%24ASPxCheckBox3=U&ctl00%24MainContent%24ASPxCheckBox4=U&ctl00%24MainContent%24ASPxCheckBox5=U&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C2_30"
    a = make_a_request("http://eport.fesmu.ru/eport/eport/studtst3.aspx", data_check_first_and_next, streaming=False)
    return a
#Тыкнуть первый и к следующему
#POST /eport/eport/studtst3.aspx HTTP/1.1
def check_some_case_and_next(array1):
    data_check_some_case_and_next = f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTI5MTM5NzM3Nw9kFgJmD2QWAgIDD2QWAmYPZBYCAg8PZBYSAgEPPCsABAEADxYCHgVWYWx1ZQUYKDIpINCf0L7Qt9C90LDQvdC40LUgLSAzZGQCBw88KwAEAQAPFgIfAAUQ0JfQsNC00LDQvdC40LUgMWRkAgkPFCsABA8WAh8ABSvQktCw0Ygg0LvQuNC80LjRgiDQstGA0LXQvNC10L3QuCAxOSDQvNC40L0uZDwrAAwBABYEHglGb3JlQ29sb3IKTx4EXyFTQgIEZGRkAgsPDxYCHgRUZXh0BXombmJzcDvQrdC80L%2FQuNGA0LjRh9C10YHQutC40LUg0LzQtdGC0L7QtNGLINC90LDRg9GH0L3QvtCz0L4g0LjRgdGB0LvQtdC00L7QstCw0L3QuNGPINC40YHQutC70Y7Rh9Cw0Y7RgjombmJzcDsmbmJzcDsgPGJyPmRkAg8PDxYCHwMFHiZuYnNwOzEuINC90LDQsdC70Y7QtNC10L3QuNC1O2RkAhMPDxYCHwMFICZuYnNwOzIuINGN0LrRgdC%2F0LXRgNC40LzQtdC90YI7ZGQCFw8PFgIfAwUhJm5ic3A7My4g0YTQvtGA0LzQsNC70LjQt9Cw0YbQuNGOZGQCGw8PFgIfAwUcJm5ic3A7NC4g0YHRgNCw0LLQvdC10L3QuNC1LmRkAh8PDxYCHwMFGyZuYnNwOzUuINC40LfQvNC10YDQtdC90LjQtWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjA0%2Bk22ByzKq5L7zouSrrJbMziS20QR38bdXSKqlADvvqw%3D&__VIEWSTATEGENERATOR=A8B80323&__EVENTVALIDATION=%2FwEdAAc%2FlZpllc25PN%2BYPogZdEuvCa17vhDUriBurXCsNy590WMU%2Ff8RYiHeDshdCQG6KXsl%2BbxYKsnWKi1oDF%2BSPbsJHS3vs9PY66cqRnl9zzvdQgrZ%2B0y1djOQFJQdjlbLnVhP%2FHXZRS6bBCR%2FaTH01z%2B9bOik%2B0yMqvUzm3kYLHgnd9IAIvs1oV7es8UR7FcUYQ4%3D&ctl00%24MainContent%24hfo1={array1[0][0]}&ctl00%24MainContent%24hfo2={array1[0][1]}&ctl00%24MainContent%24hfo3={array1[0][2]}&ctl00%24MainContent%24hfo4={array1[0][3]}&ctl00%24MainContent%24hfo5={array1[0][4]}&ctl00%24MainContent%24hf1=0&ctl00%24MainContent%24ASPxButton5=&ctl00%24MainContent%24ASPxCheckBox1={array1[1][0]}&ctl00%24MainContent%24ASPxCheckBox2={array1[1][1]}&ctl00%24MainContent%24ASPxCheckBox3={array1[1][2]}&ctl00%24MainContent%24ASPxCheckBox4={array1[1][3]}&ctl00%24MainContent%24ASPxCheckBox5={array1[1][4]}&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C2_30"
    make_a_request("http://eport.fesmu.ru/eport/eport/studtst3.aspx", data_check_some_case_and_next)
    return array1[0]
    #print(":", data_check_some_case_and_next)

#Тыкнуть первый и в меню
#POST /eport/eport/studtst3.aspx HTTP/1.1
def check_first_and_return_main_menu():
    data_check_first_and_return_main_menu = "ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTI5MTM5NzM3Nw9kFgJmD2QWAgIDD2QWAmYPZBYCAg8PZBYSAgEPPCsABAEADxYCHgVWYWx1ZQVTKDIpINCj0YXQvtC0INC30LAg0LHQvtC70YzQvdGL0LzQuCDQsiDQv9C10YDQuNC%2B0L%2FQtdGA0LDRgtC40LLQvdC%2B0Lwg0L%2FQtdGA0LjQvtC00LVkZAIHDzwrAAQBAA8WAh8ABRHQl9Cw0LTQsNC90LjQtSAyMmRkAgkPFCsABA8WAh8ABSrQktCw0Ygg0LvQuNC80LjRgiDQstGA0LXQvNC10L3QuCA0INC80LjQvS5kPCsADAEAFgQeCUZvcmVDb2xvcgorHgRfIVNCAgRkZGQCCw8PFgIeBFRleHQFWdCc0LXRgNGLINC%2F0YDQuCDQt9Cw0LTQtdGA0LbQutC1INC80L7Rh9C10LjRgdC%2F0YPRgdC60LDQvdC40Y8g0L%2FQvtGB0LvQtSDQvtC%2F0LXRgNCw0YbQuNC4ZGQCDw8PFgIfAwVNMS4g0J%2FRgNC40LzQtdC90LXQvdC40LUg0L%2FRg9C30YvRgNGPINGB0L4g0LvRjNC00L7QvCDQvdCwINC90LjQtyDQttC40LLQvtGC0LBkZAITDw8WAh8DBSwyLiDQvdCw0LfQvdCw0YfQtdC90LjQtSDQvNC%2B0YfQtdCz0L7QvdC90YvRhWRkAhcPDxYCHwMFTzMuINCy0L3Rg9GC0YDQuNCy0LXQvdC90L7QtSDQstCy0LXQtNC10L3QuNC1IDUlINGA0LDRgdGC0LLQvtGA0LAg0LPQu9GO0LrQvtC30YtkZAIbDw8WAh8DBWM0LiDQv9GA0LjQvNC10L3QtdC90LjQtSDRgtC10L%2FQu9C%2B0Lkg0LPRgNC10LvQutC4INC90LAg0L7QsdC70LDRgdGC0Ywg0LzQvtGH0LXQstC%2B0LPQviDQv9GD0LfRi9GA0Y9kZAIfDw8WAh8DBQFfZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgIFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b241BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMDQE5T9V7VMreWdfpku7yNIDDWy4F0wCwHlTSIdKybDHIQ%3D%3D&__VIEWSTATEGENERATOR=A8B80323&__EVENTVALIDATION=%2FwEdAAfDRLP7NE8mELLiT2ZK%2FjipCa17vhDUriBurXCsNy590WMU%2Ff8RYiHeDshdCQG6KXsl%2BbxYKsnWKi1oDF%2BSPbsJHS3vs9PY66cqRnl9zzvdQgrZ%2B0y1djOQFJQdjlbLnVhP%2FHXZRS6bBCR%2FaTH01z%2B9zErVTJvNAHMQny1oGGVfJe3IXe%2FaUiAq3S3lPvQuuas%3D&ctl00%24MainContent%24hfo1=1&ctl00%24MainContent%24hfo2=0&ctl00%24MainContent%24hfo3=0&ctl00%24MainContent%24hfo4=0&ctl00%24MainContent%24hfo5=0&ctl00%24MainContent%24hf1=0&ctl00%24MainContent%24ASPxButton04=&ctl00%24MainContent%24ASPxCheckBox1=C&ctl00%24MainContent%24ASPxCheckBox2=U&ctl00%24MainContent%24ASPxCheckBox3=U&ctl00%24MainContent%24ASPxCheckBox4=U&ctl00%24MainContent%24ASPxCheckBox5=U&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C2_30"
    a = make_a_request("http://eport.fesmu.ru/eport/eport/studtst3.aspx", data_check_first_and_return_main_menu)
    return a





# ЗАЙТИ НА ПЯТЕРКУ
#GET /eport/eport/studtst5.aspx HTTP/1.1
def go_to_check_answer5():
    a = make_a_request("http://eport.fesmu.ru/eport/eport/studtst5.aspx", "", get_request=True)

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
def answer_all_questions():
    select_question("1")    
    for i in range(30):
        space = ""
        if (i+1) < 10: space = " "
        

        var1 = go_to_check_answer5()
        
        if var1 == False:
            return True

        new_list = check_some_case_and_next(var1)
        
        print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Вопрос {i+1}{space}: {new_list}")
                            
    return False

#check_results_of_tests_by_num_of_pred
#POST /eport/eport/studtst1.aspx HTTP/1.1
def check_all_results_of_tests_by_num_of_pred(num_of_pred=0):
    data_check_results_of_tests_by_num_of_pred = f"ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUIOTk1NDMwOTQPZBYCZg9kFgICAw9kFgJmD2QWAgIJD2QWBAIDD2QWAmYPZBYCZg9kFgJmD2QWAgIBDxQrAAUPFgIeD0RhdGFTb3VyY2VCb3VuZGdkZGQ8KwAHAQYPZBAWAgIBAgIWAhQrAAEWAh4PQ29sVmlzaWJsZUluZGV4ZhQrAAEWAh8BAgFkFgBkAgcPZBYCZg9kFgJmD2QWAmYPZBYCAgEPFCsABWRkZDwrAAcBBg9kEBYCZgIBFgIUKwABFgIfAWYUKwABFgIfAQIBZBYAZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjcFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOAUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjm6%2BEbUEKpaxmSv00E%2B%2FJiuKcZ%2BYI%2BIkpp3rzk2vaUFAA%3D%3D&__VIEWSTATEGENERATOR=847F47AD&__EVENTVALIDATION=%2FwEdAAeH8wh4QiiJKgOuKnFFkPWbI7ZJDWlRgaefdPW8BTEVtXw%2BikVKJJfrT0ndBbXKBTA39nUTQDb0GEkh6LDT5SpRsAIaIhbklmBqr8w%2BPxD292wBCiQy8HT9gxcspUtWdqpbDCDdUSb6jcSCho5zpwlSvNMTFvzkvoYxtvqO8J0ljItyMFkzxVGQu2RBvSrJ7No%3D&ctl00%24MainContent%24hfPred={str(num_of_pred)}&ctl00%24MainContent%24hfTest=-1&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2DeletedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2InsertedItems=&ctl00_MainContent_ASPxCallbackPanel1_ASPxListBox2CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel1%24ASPxListBox2=System.Data.DataRowView&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3DeletedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3InsertedItems=&ctl00_MainContent_ASPxCallbackPanel2_ASPxListBox3CustomCallback=&ctl00%24MainContent%24ASPxCallbackPanel2%24ASPxListBox3=&ctl00%24MainContent%24ASPxButton9=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40%2C1_41%2C2_36"
    a = make_a_request("http://eport.fesmu.ru/eport/eport/studtst1.aspx", data_check_results_of_tests_by_num_of_pred)
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
def close_test():
    data_close_test = "ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTUwNzg4NDI2OQ9kFgJmD2QWAgIDD2QWAgIBD2QWAgIDD2QWQgIBDzwrAAQBAA8WAh4FVmFsdWUFKCgxKSDQoNGD0YHRgdC60LDRjyDRhNC40LvQvtGB0L7RhNC40Y8gLTFkZAIJDzwrAAQBAA8WAh8ABSvQmNC00LXQvdGC0LjRhNC40LrQsNGC0L7RgCDRgtC10YHRgtCwIDEyNDUwZGQCCw8UKwAEDxYCHwAFKtCS0LDRiCDQu9C40LzQuNGCINCy0YDQtdC80LXQvdC4IDIg0LzQuNC9LmQ8KwAMAQAWBB4JRm9yZUNvbG9yCqABHgRfIVNCAgRkZGQCDw8UKwAGZGRkZDwrAAcBABYEHgtDc3NGaWxlUGF0aAUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHgpDc3NQb3N0Zml4BQVHbGFzczwrAAYBABYCHhFTcHJpdGVDc3NGaWxlUGF0aAUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCEQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAhMPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIVDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCFw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAhkPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIbDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCHQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAh8PFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIhDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCIw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAiUPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAInDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCKQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAisPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAItDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCLw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAjEPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIzDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCNQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAjcPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAI5DxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCOw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAj0PFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAI%2FDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCQQ8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAkMPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAJFDxQrAAZkZGRkPCsABwEAFgQfAwUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwQFBUdsYXNzPCsABgEAFgIfBQUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCRw8UKwAGZGRkZDwrAAcBABYEHwMFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8EBQVHbGFzczwrAAYBABYCHwUFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAkkPFCsABmRkZGQ8KwAHAQAWBB8DBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBAUFR2xhc3M8KwAGAQAWAh8FBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WIQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjA0BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMDIFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24wMwUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjEFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yBR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMwUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjQFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b241BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uNgUdY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjcFHWN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b244BR1jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uOQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjEwBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTEFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xMgUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjEzBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTQFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xNQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE2BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMTcFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24xOAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjE5BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjAFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yMQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjIyBR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjMFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yNAUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjI1BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjYFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24yNwUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjI4BR5jdGwwMCRNYWluQ29udGVudCRBU1B4QnV0dG9uMjkFHmN0bDAwJE1haW5Db250ZW50JEFTUHhCdXR0b24zMGNg%2Btc0Yd%2B%2BfMAWH2wgXducRETufa9xvvwxgDjN4cZ%2F&__VIEWSTATEGENERATOR=4F4B5F1E&ctl00%24MainContent%24ASPxButton03=&DXScript=1_42%2C1_75%2C2_27%2C2_34%2C2_40"
    a = make_a_request("http://eport.fesmu.ru/eport/eport/studtst2.aspx", data_close_test)
    return a


#Завершить тест при меньше 70 % ошибке
#POST /eport/eport/studtst4.aspx HTTP/1.1
def close_test_70_error():
    data_close_test = "ctl00_MainContent_ToolkitScriptManager1_HiddenField=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKMTQ4OTc2MzU4MA9kFgJmD2QWAgIDD2QWAgIBD2QWAgIDD2QWRgIBDzwrAAQBAA8WAh4FVmFsdWUFKCgxKSDQoNGD0YHRgdC60LDRjyDRhNC40LvQvtGB0L7RhNC40Y8gLTFkZAIFDw8WAh4EVGV4dGVkZAIHDw8WBh8BZR4JRm9yZUNvbG9yCpEBHgRfIVNCAgRkZAITDzwrAAQBAA8WAh8ABQEgZGQCFQ8UKwAEDxYCHwAFiQHQn9GA0L7RgdC80L7RgtGAINC%2B0YLQstC10YLQvtCyINC30LDQtNCw0L3QuNC5INCy0L7Qt9C80L7QttC10L0g0YLQvtC70YzQutC%2BINC%2F0YDQuCDQstGL0L%2FQvtC70L3QtdC90LjQuCDQvdC1INC80LXQvdC10LUgNzAlINGC0LXRgdGC0LAuIGQ8KwAMAQAWBh8CCpEBHglGb250X1NpemUoKiJTeXN0ZW0uV2ViLlVJLldlYkNvbnRyb2xzLkZvbnRVbml0BDI1cHQfAwKECGRkZAIXDxQrAAYPFgIeB1Zpc2libGVoZGRkZDwrAAcBABYEHgtDc3NGaWxlUGF0aAUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MeCkNzc1Bvc3RmaXgFB1JlZFdpbmU8KwAGAQAWAh4RU3ByaXRlQ3NzRmlsZVBhdGgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCGQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAhsPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBwUFR2xhc3M8KwAGAQAWAh8IBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIdDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCHw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAiEPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAIjDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwcFBUdsYXNzPCsABgEAFgIfCAUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCJQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAicPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAIpDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCKw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAi0PFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBwUFR2xhc3M8KwAGAQAWAh8IBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAIvDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUhfi9BcHBfVGhlbWVzL0dsYXNzL3swfS9zdHlsZXMuY3NzHwcFBUdsYXNzPCsABgEAFgIfCAUifi9BcHBfVGhlbWVzL0dsYXNzL0FTUHhCdXR0b24uc2tpbmQCMQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAjMPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAI1DxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCNw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAjkPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAI7DxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCPQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAj8PFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSF%2BL0FwcF9UaGVtZXMvR2xhc3MvezB9L3N0eWxlcy5jc3MfBwUFR2xhc3M8KwAGAQAWAh8IBSJ%2BL0FwcF9UaGVtZXMvR2xhc3MvQVNQeEJ1dHRvbi5za2luZAJBDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCQw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFIX4vQXBwX1RoZW1lcy9HbGFzcy97MH0vc3R5bGVzLmNzcx8HBQVHbGFzczwrAAYBABYCHwgFIn4vQXBwX1RoZW1lcy9HbGFzcy9BU1B4QnV0dG9uLnNraW5kAkUPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAJHDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCSQ8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAksPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZAJNDxQrAAYPFgIfBWhkZGRkPCsABwEAFgQfBgUjfi9BcHBfVGhlbWVzL1JlZFdpbmUvezB9L3N0eWxlcy5jc3MfBwUHUmVkV2luZTwrAAYBABYCHwgFJH4vQXBwX1RoZW1lcy9SZWRXaW5lL0FTUHhCdXR0b24uc2tpbmQCTw8UKwAGDxYCHwVoZGRkZDwrAAcBABYEHwYFI34vQXBwX1RoZW1lcy9SZWRXaW5lL3swfS9zdHlsZXMuY3NzHwcFB1JlZFdpbmU8KwAGAQAWAh8IBSR%2BL0FwcF9UaGVtZXMvUmVkV2luZS9BU1B4QnV0dG9uLnNraW5kAlEPFCsABg8WAh8FaGRkZGQ8KwAHAQAWBB8GBSN%2BL0FwcF9UaGVtZXMvUmVkV2luZS97MH0vc3R5bGVzLmNzcx8HBQdSZWRXaW5lPCsABgEAFgIfCAUkfi9BcHBfVGhlbWVzL1JlZFdpbmUvQVNQeEJ1dHRvbi5za2luZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUeY3RsMDAkTWFpbkNvbnRlbnQkQVNQeEJ1dHRvbjAz1nJ55AxZ4GtGPuU7FLyU46WjfL997Ctb045KzUnZOCI%3D&__VIEWSTATEGENERATOR=6D81C9BC&ctl00%24MainContent%24ASPxButton03="
    a = make_a_request("http://eport.fesmu.ru/eport/eport/studtst4.aspx", data_close_test)
    return a 

def try_to_check_all():
    select_question("1")
    for i in range(30):
        check_first_and_next()



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_all_first_cases_and_verify(num_of_error=0):
    num_of_error += 1
    num_of_error_vsego = 5
    if num_of_error <=5:
        try_to_check_all()

        res = check_first_and_return_main_menu()
        soub = BeautifulSoup(res.text, 'html.parser')
        a = soub.select('table[class="btntest"] > tr > td > table > tr > td[id^="ctl00_MainContent_ASPxButton"]')
        if len(a) == 30:
            for i, item in enumerate(a):
                #if 'class="dxbButton_Glass"' in str(item):
                #    print(f'{i} - прорешан')
                if 'class="dxbButton_Aqua"' in str(item):
                    print(f'Внимание!, {i+1} - не прорешан, пробую еще раз ({num_of_error}/{num_of_error_vsego})...')
                    return check_all_first_cases_and_verify(num_of_error=num_of_error)
                #else:
                #    print(f'{i} - error')
        else:
            print(f'Внимание!, что-то пошло не так, пробую еще раз ({num_of_error}/{num_of_error_vsego})...')
            return check_all_first_cases_and_verify(num_of_error=num_of_error)
        return True
    else:
        print("Не получается, извините, завершаю работу программы")
        quit()



def admin():
    while True:
        print("""
    0 - auth
    1 - enter_current_test
    2 - select_question   
    3 - check_first_and_next
    4 - check_first_and_return_main_menu
    6 - close_test
    7 - close_test_70_error
    8 - check_some_case_and_next(go_to_check_answer5())
    9 - go_to_check_answer5()
    10 - chose_some_test_from_list
    11 - cls
    12 - exit admin 
    
    15 - check_all_results_of_tests_by_num_of_pred(num_of_pred=10)
    """)
        choice = str(user_input("\n———>Do: "))

        if choice == "0":
            login = user_input("Login: ")
            password = user_input("Passd: ")
            auth(login, password)
        elif choice == "1":
            try:
                pred = int(user_input("\n——————>What a predmet: "))
                test = int(user_input("\n——————>What a test:    "))
                enter_current_test(pred-1, test-1)
            except Exception as e:
                print(f"\n————————————> error: {e}")
        elif choice == "2":
            try:
                choice2 = str(user_input("\n——————>What a question: "))
                select_question(choice2)
            except Exception as e:
                print("\n————————————> error")
        elif choice == "3":
            check_first_and_next()
        elif choice == "4":
            check_first_and_return_main_menu()
        elif choice == "5":
            go_to_check_answer5()
        elif choice == "6":
            close_test()
        elif choice == "7":
            close_test_70_error()
        
        elif choice == "8":
            var1 = go_to_check_answer5()
            if var1 == False:
                print("критическая ошибка")
            else: 
                print("Ввожу полученные данные на сайт и перехожу к следующему вопросу...")
                check_some_case_and_next(var1)
        elif choice == "9":
            var1 = go_to_check_answer5()
            if var1 == False:
                print("критическая ошибка")
            else: print(var1)
        elif choice == "11":
            os.system("cls")

        elif choice == "10":
            print(chose_some_test_from_list())
        elif choice == "12":
            break
        elif choice == "15":
            list = check_all_results_of_tests_by_num_of_pred()
            #print(list)
            for i in range(len(list)):
                print(list[i])
        else:
            print("Не распознал")
            continue
    

auth_bool = False
def main():
    auth_bool = False
    num_of_mistakes_ot = 1
    num_of_mistakes_do = 4
    time_to_wait_ot = 420
    time_to_wait_do = 660

    ################################проверка на апдейт и установка
    print("Добро пожаловать!!! Проверяю обновления...")
    process = subprocess.Popen(['cd ~/fenix-test_solver'], stdout=subprocess.DEVNULL, text=True, shell=True)
    process = subprocess.Popen(['git init'], stdout=subprocess.DEVNULL, text=True, shell=True)
    process = subprocess.Popen(['git stash'], stdout=subprocess.DEVNULL, text=True, shell=True)
    process = subprocess.Popen(['git pull'], stdout=subprocess.PIPE, text=True, shell=True)
    for line in iter(process.stdout.readline, ''):
        if "Already up to date" in line:
            print("\nОбновления не найдены, у вас последняя версия!(нестабильная)\n")
            break
        elif "Updating" in line:
            print("\nОбновление установлено успешно, перезапусти меня!!!\n(введи \"test\")\n")
            quit()
    ##############################################################
    
    while True:

        print("""
---------------------------------------------------------------
Выберите действие:
1. Решить тесты
2. Изменить параметы — ошибки и время
3. Изменить данные аккаунта
4. Очистить экран
0. Выйти
""")
        chose = input("Действие: ")
        if chose == "1":
            if get_login() and get_pass():
                if auth():
                    auth_bool = True
                else:
                    print("Кажется в данных ошибка! Попробуйте изменить логин или пароль")
            else:
                print("Кажется вы здесь впервые! Введите свои данные:")
                login = input("Логин: ")
                passw = input("Пароль: ")
                set_login_pass(login1=quote(login), pass1=quote(passw))
                print("Спасибо! Записал в файл...")
                if auth():
                    auth_bool = True
                else:
                    print("Кажется в данных ошибка! Попробуйте изменить логин или пароль")
                #continue
        elif chose == "3":
            if get_login() and get_pass():
                print(f"Ваши данные: {get_login()}:{get_pass()}")
            print("\nВведите новые данные (0 — вернуться в меню)")
            login = input("Логин: ")
            if login == "0": continue
            passw = input("Пароль: ")
            if passw == "0": continue
            set_login_pass(login1=quote(login), pass1=quote(passw))
            print("Спасибо! Записал в файл...")
            continue
        elif chose == "4":
            os.system('clear')
        elif chose == "0":
            print("\nПрощайте! Для повторного запуска введите команду \"test\" или откройте новую вкладку!")
            quit()

        elif chose == "2":
            print(f"""
1. Количество ошибок (установлено от {num_of_mistakes_ot} до {num_of_mistakes_do})
2. Сколько ждать времени чтобы завершить тест(установлено от {time_to_wait_ot} до {time_to_wait_do} секунд)
3. Исправить ошибку молодости (error)
0. Вернуться в меню
""")
            chose2 = input("Действие: ")
            if chose2 == "1":
                try:
                    a1 = int(input("Со скольки: "))
                    a2 = int(input("До скольки: "))     
                    num_of_mistakes_ot = a1
                    num_of_mistakes_do = a2
                    print(f"Установлено рандомное колиество ошибок от {num_of_mistakes_ot} до {num_of_mistakes_do}")
                except ValueError:
                    print("Вы допустили ошибку!")
    
            if chose2 == "2":
                try:
                    a1 = int(input("Со скольки: "))
                    a2 = int(input("До скольки: "))    
                    time_to_wait_ot = a1
                    time_to_wait_do = a2
                    print(f"Установлено рандомное время до завершения теста от {time_to_wait_ot} до {int(time_to_wait_do)} секунд")
                except ValueError:
                    print("Вы допустили ошибку! Попробуйте еще раз")
    
            if chose2 == "3":
                a = input("Как зовут ошибку: ")
                if (a == "Дима") or (a == "дима"):
                    print(prikoli.dima)
                elif (a == "Стас") or (a == "стас"):
                    print(prikoli.admin)
                elif (a == "Алена") or (a == "алена") or (a == "Алёна") or (a == "алёна"):
                    print(prikoli.alena)
                elif (a == "Эля") or (a == "эля") or (a == "Элина") or (a == "элина"):
                    print(prikoli.elia)
                else:
                    print("У вас еще всё более чем отлично!, попробуйте кого-нибудь другого исправить...")
        if auth_bool == True:
            to_exit = False
            while True:

                #допытываем от пользователя номер предмета и тесты
                try:
                    list_of_preds_and_tests = chose_some_test_from_list()
                except ValueError:
                    print("\nБудьте внимательнее! Пробуем ещё раз...")
                    continue
                
                if list_of_preds_and_tests == -1:
                    to_exit = True
                    break
                if list_of_preds_and_tests == False:
                    print("\nБудьте внимательнее! Пробуем ещё раз...")
                    continue
                try:
                    num_pred_r = list_of_preds_and_tests[0]
                    num_testing_r = list_of_preds_and_tests[1]
                    do_kakogo_testa_vkluchitelno_r = list_of_preds_and_tests[2]
                    
                    name_pred_r = list_of_preds_and_tests[3]               #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    list_of_num_test_r = list_of_preds_and_tests[4]
                    list_of_name_test_r = list_of_preds_and_tests[5]
                    
                    del list_of_preds_and_tests[:]
                except Exception as e:
                    print("\nБудьте внимательнее! Пробуем ещё раз...")
                    continue
                #и удостоверяемся в правильности введенной информации
                vsego_testov = int(do_kakogo_testa_vkluchitelno_r) - int(num_testing_r) + 1
                world_test = ""
                if vsego_testov == 1:
                    world_test = "тест"
                elif (vsego_testov >=2) and (vsego_testov <=4):
                    world_test = "теста"
                else:
                    world_test = "тестов"
                a = user_input(f"Решаю {vsego_testov} {world_test} по предмету \"{name_pred_r}\" — с {num_testing_r+1} по {do_kakogo_testa_vkluchitelno_r+1} включительно, правильно?\n(y/n): ")
                if ("y" in a): break
                elif ("Y" in a): break
                elif ("н" in a): break
                elif ("Н" in a): break
                else: print("Хорошо, пробуем ещё раз...")

            if to_exit:
                print("Возвращаюсь...")
                continue
            #несколько нужных переменных
            answers_complete = False
            num_of_error = 0
            time_start_test = 0

            num_testing = num_testing_r
            do_kakogo_testa_vkluchitelno = do_kakogo_testa_vkluchitelno_r

            result_solved_test = []
            errored_solved_test = 0
            del result_solved_test[:]
            
            #идем решать указанные тесты
            while num_testing <= do_kakogo_testa_vkluchitelno:
                a = enter_current_test(num_pred_r, num_testing)  #входим
                soup = BeautifulSoup(a.text, 'html.parser')
                proverka = False
                
                # 1 проверка на Исчерпанный суточный лимит выполнения теста (или существует указанный тест вообще) 
                b1 = soup.select('script[src^="/eport/WebResource.axd"] ~ script[type="text/javascript"]')
                for i in range(len(b1)): 
                    if "Исчерпан суточный лимит выполнения теста" in b1[i].text:
                        print(f'\n---------------------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>"Исчерпан суточный лимит", тест {num_testing+1} по предмету \"{name_pred_r}\" (либо его не существует)!!!')
                        if (num_testing+1) <= do_kakogo_testa_vkluchitelno: 
                            print(f'{datetime.datetime.now().strftime("%H:%M:%S")}:——>Пробую решить следующий тест ({num_testing+2})...')
                        num_testing += 1
                        errored_solved_test += 1
                        answers_complete = False
                        proverka = True
                        break

                # 2 проверка на уже прорешанный ранее тест с результатом меньше 70 %
                b2 = soup.select('label[id="ctl00_MainContent_ASPxLabel10"]')
                for i in range(len(b2)): 
                    if "Просмотр ответов заданий возможен только при выполнении не менее 70% теста" in b2[i].text:
                        print(f'\n---------------------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>"Просмотр ответов заданий возможен только при выполнении не менее 70%", тест {num_testing+1} по предмету \"{name_pred_r}\", завершаю его!')
                        print(f'{datetime.datetime.now().strftime("%H:%M:%S")}:——>Пробую еще раз решить тест {num_testing+1}...')
                        answers_complete = False                       
                        proverka = True
                        close_test_70_error()
                        break
                
                # 3 проверка на решенный ранее более чем на 70+ тест
                b3 = soup.select('label[id="ctl00_MainContent_ASPxLabel8"]')
                for i in range(len(b3)): 
                    if "Всего правильных ответов" in b3[i].text:
                        print(f'\n---------------------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>Тест {num_testing+1} уже был ранее прорешан на 70%+ по предмету \"{name_pred_r}\", завершаю его!')
                        if (num_testing+1) <= do_kakogo_testa_vkluchitelno: 
                            print(f'{datetime.datetime.now().strftime("%H:%M:%S")}:——>Пробую решить следующий тест ({num_testing+2})...')
                        num_testing += 1
                        answers_complete = False                      
                        proverka = True

                        b4 = soup.select('div[id="ctl00_MainContent_Panel1"] > label')
                        name_of_test = (b4[0].text).strip()
                        name_of_pred = name_pred_r
                        c = soup.select('label[id="ctl00_MainContent_ASPxLabel8"]')
                        num_non_smisl_of_test = (str(c[0].text)[20:]).strip()

                        result_solved_test.append([name_pred_r, name_of_test, num_non_smisl_of_test, "70+"])

                        close_test()
                        break
                
                #Если проверка прошла успешно, то решаем данный тест
                if proverka == True:
                    continue    
                elif proverka == False:
                    soup = BeautifulSoup(a.text, 'html.parser')
                    b = soup.select('div[id="ctl00_MainContent_Panel1"] > label')
                    name_of_test = "Error_name" 
                    try:
                        name_of_test = (b[0].text).strip()
                    except Exception:
                        name_of_test ="Error_name" 
                        try:
                            if auth():
                                name_of_test = (b[0].text).strip()
                        except Exception:
                            pass
                    
                    name_of_pred = name_pred_r

                    c = soup.select('label[id="ctl00_MainContent_ASPxLabel8"]')
                    num_non_smisl_of_test = (str(c[0].text)[20:]).strip()
                    
                    time_start_test = datetime.datetime.now()
                    print(f"\n---------------------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:Захожу на тест {num_testing+1} \"{str(name_of_test)[4:]}\" ({num_non_smisl_of_test})")
                    
                    
                    if answers_complete == False:
                        print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>1.ПРОБЕГАЮСЬ ПО ВОПРОСАМ...")
                        
                        time_before = datetime.datetime.now()
        
                        if check_all_first_cases_and_verify():
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
                        crytical_error = answer_all_questions()


                        #Завершение
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
                    num_of_mistakes = random.randint(num_of_mistakes_ot, num_of_mistakes_do)
                    array_error = [['0', '0', '0', '0', '0'], ['U', 'U', 'U', 'U', 'U']]
                    print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Делаю ошибки — {num_of_mistakes}...")
                    select_question(1)
                    for i in range(num_of_mistakes):
                        check_some_case_and_next(array_error)



                    



                    #готовися ждать
                    time_to_wait = random.randint(time_to_wait_ot, time_to_wait_do) 
                    #time_to_wait = 1800
                    interval = datetime.timedelta(seconds=time_to_wait)
                    the_end = datetime.datetime.now() + interval
                    time_to_wait_min = f"{time_to_wait//60} минут {time_to_wait % 60} секунд"
                    print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Буду ждать {time_to_wait_min} до {the_end.strftime("%H:%M:%S")}...")
                    time.sleep(time_to_wait)
                    print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>Время вышло! Заканчиваю тестирование...")
                    
                    #auth(silence=True)
                    #time.sleep(5)
                    #конец
                    
                    
                    
                    res_exit = close_test()
                    
                    print(f"""
-----------------------------------------------------
{res_exit.text}
-----------------------------------------------------
""")
                    
                    
                    procent_solved = "Error" 

                    """def get_result(mist=0):
                        mist += 1
                        if mist <= 3:
                            try:    
                                results_array = check_all_results_of_tests_by_num_of_pred(num_of_pred=num_pred_r)
                                procent_solved = "ERROR"
                                for j in range(len(results_array)-1): #j += 1
                                    j += 1
                                    if str(results_array[j][0].text).strip() in str(name_of_test):
                                        procent_solved = str(results_array[j][1].text).strip()
                                        return procent_solved
                                    print("Error123, try again") 
                                    time.sleep(5)
                                    #auth(silence=True) 
                                    return get_result(mist=mist)            
                            except Exception :
                                print("Error123, try again") 
                                time.sleep(5)
                                #auth(silence=True) 
                                return get_result(mist=mist) 
                        else:
                            return "Error" """
                    
                    def get_result(num_pred_r, name_of_test, num_of_mist=0):
                        try:
                            if num_of_mist <=5:
                                num_of_mist += 1
                                time.sleep(6)
                                results_array = check_all_results_of_tests_by_num_of_pred(num_of_pred=num_pred_r)
                                for j in range(len(results_array)-1): #j += 1
                                    j += 1
                                    if str(results_array[j][0].text).strip() in str(name_of_test):
                                        procent_solved = str(results_array[j][1].text).strip()
                                        #print(f"---------------> \"{procent_solved}\"")
                                        if procent_solved == "0":
                                            #значит тест не завершился еще
                                            print(f"Внимание, с {num_of_mist}/5 раза тест не завершился, пробую еще раз...")
                                            close_test()
                                            return get_result(num_pred_r, name_of_test, num_of_mist=num_of_mist)
                                        else:
                                            return procent_solved
                                    print("Error123, try again")
                                    return False 
                            else:
                                return "Error123454575656345#"          
                        except Exception :
                            print("Error456, try again") 
                            return False
                    
                    procent_solved = get_result() 

                        
                            
                            
                            
                            #print(f"SOVPADENIE NAIDENO: {str(results_array[j][0].text).strip()}  —>  {str(test_name_list[i].text).strip()}")
                            #if int(str(results_array[j][1].text).strip()) >= new_list_of_persent[0][i]: 
                            #    new_list_of_persent[0][i] = int(str(results_array[j][1].text).strip())
                            #    new_list_of_persent[1][i] = str(results_array[j][0].text).strip()
                     
                    print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>4.Тест {num_testing+1} \"{str(name_of_test)[4:]}\" завершён на {procent_solved}% (должно быть {round(((30-num_of_mistakes)/30)*100, 2)}%)")

                    
                    answers_complete = False
                    num_testing += 1
                    num_of_error = 0
                    result_solved_test.append([name_of_pred, str(name_of_test)[4:], num_non_smisl_of_test, procent_solved])
                    
                    if num_testing > do_kakogo_testa_vkluchitelno:
                        pass
                    else:
                        print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——> Жду 10 секунд и приступаю к следующему...")
                        time.sleep(10)

            



            if len(result_solved_test) != 0:
                print(f"\n---------------------------------------------------------------\n{datetime.datetime.now().strftime("%H:%M:%S")}:—————>Все указанные тесты прорешаны:")
                for i in range(len(result_solved_test)):
                    print(f"{datetime.datetime.now().strftime("%H:%M:%S")}:——>{i+1}. {result_solved_test[i][0]} — {result_solved_test[i][1]} ({result_solved_test[i][2]}) — на {result_solved_test[i][3]}%")
                print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:——>Сколько не получилось прорешать указанных тестов: {errored_solved_test}")
            else:
                print("\n---------------------------------------------------------------\nE—————————>6.Ни один тест не был прорешан :(")
                print(f"\n{datetime.datetime.now().strftime("%H:%M:%S")}:——>Сколько не получилось прорешать указанных тестов: {errored_solved_test}")
            print("\n\n")
            del result_solved_test[:]



# дима лох
main()
