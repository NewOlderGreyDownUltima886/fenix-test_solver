import subprocess, sys
import time
i = 1

#print("Выберите версию:\n1. Терминал (старая версия)\n2. Телеграм бот (новая нестабильная версия)")
chose = 0
try:
    while True:
        print('\n--------------------------------------------------------')
        chose = input("Выберите версию:\n1. Терминал (старая версия)\n2. Телеграм бот (новинка)\nВыбор (цифра 1 или 2): ")
        try:
            chose = int(chose)
        except Exception:
          print("Попробуйте еще раз!")
          continue
        if (chose == 1) or (chose == 2):
            break
        else:
            print("Попробуйте еще раз!")
            continue
except:
    print("Попробуйте еще раз!")
while True:
    if i > 1:
        print(f"\n--------------------------------------------------------\nПерезапускаю fenix {i} раз")
        #print("Автоматически перезапускаю fenix...")
    time.sleep(1)
    if chose == 1:
        subprocess.call(["python", "core_test_solver_terminal_edition.py"])
    elif chose ==2:
        #print("Пока недоступно, извините!")
        subprocess.call(["python", "core_test_solver_TgBot_edition.py"])
    i += 1


"""
def del_msg(chat_id, msg_id_array):  #msg_id - array
  time.sleep(0.2)
  try:
    if len(msg_id_array) != 0:
      print("\n----------------------------\nПОЛУЧЕН ЗАПРОС НА УДАЛЕНИЕ:", msg_id_array)
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
      
      try:
        for i in range(len(msg_id_array)):
          #print("работаю с", msg_id_array[i])
          try:
            bot.delete_message(chat_id, str(msg_id_array[i]))
            print("Успешно удалено смс в телеграмме", msg_id_array[i] )
          except Exception as e:
            print('Не получилось удалить смс в телеграмме', msg_id_array[i], e)
        print("------> УДАЛЕНИЕ ПРОШЛО БЕЗ ОШИБОК, ОЧИЩАЮ МАССИВ")
        msg_id_array.clear()
      
      except Exception as e:
        print("    ERROR 2: (ошибка удаления смс)", e, " ВХОЖУ ЕЩЕ РАЗ В СЕБЯ ДЛЯ ПОПЫТКИ ЕЩЕ РАЗ!!!!!!!!!!!!!!!")
        del_msg(chat_id, msg_id_array)
      
"""
