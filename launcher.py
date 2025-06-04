import subprocess, sys, os

i = 1
chose = 0


while True:
    try:
        while True:
            chose = input("""           
////////////////////////////////////////////////
// ________  ________  __    __  __  __    __ //
//|        \\|        \\|  \\  |  \\|  \\|  \\  |  \\//
//| $$$$$$$$| $$$$$$$$| $$\\ | $$ \\$$| $$  | $$//
//| $$__    | $$__    | $$$\\| $$|  \\ \\$$\\/  $$//
//| $$  \\   | $$  \\   | $$$$\\ $$| $$  >$$  $$ //
//| $$$$$   | $$$$$   | $$\\$$ $$| $$ /  $$$$\\ //
//| $$      | $$_____ | $$ \\$$$$| $$|  $$ \\$$\\//
//| $$      | $$     \\| $$  \\$$$| $$| $$  | $$//
// \\$$       \\$$$$$$$$ \\$$   \\$$ \\$$ \\$$   \\$$//
////////////////////////////////////////////////

--------------------------------------------------
ГЛАВНОЕ МЕНЮ:
1. Консольная версия (классическая)
2. Telegram бот (новинка)
3. Очистить экран
0. Выйти из программы
                          
—>Ваш выбор: """)
            try:
                chose = int(chose)
            except Exception:
              print("Попробуйте еще раз!")
              continue
            if (chose == 1) or (chose == 2) or (chose == 3) or (chose == 0):
                break
            else:
                print("Попробуйте еще раз!")
                continue
    except:
        print("Попробуйте еще раз!")
    
    try:
      if chose == 1:
          if len(sys.argv) > 1:
              if sys.argv[1] == "1":
                subprocess.call(["python", "core_test_solver_terminal_edition.py", "1"])
          else:
            subprocess.call(["python", "core_test_solver_terminal_edition.py"])
      elif chose == 2:
          if len(sys.argv) > 1:
              if sys.argv[1] == "1":
                subprocess.call(["python", "core_test_solver_TgBot_edition.py", "1"])
          else:
            subprocess.call(["python", "core_test_solver_TgBot_edition.py"])
      elif chose == 0:
          quit()
      elif chose == 3:
          if len(sys.argv) > 1:
              if sys.argv[1] == "1":
                os.system('cls')
          else:
              os.system('clear')
    except KeyboardInterrupt:
      print("pohui")
    i += 1
