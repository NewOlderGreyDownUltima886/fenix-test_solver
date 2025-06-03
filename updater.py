import os, subprocess

print("Добро пожаловать в Fenix!!! Проверяю обновления...")
process = subprocess.Popen(['cd ~/fenix-test_solver'], stdout=subprocess.DEVNULL, text=True, shell=True)
process = subprocess.Popen(['git init'], stdout=subprocess.DEVNULL, text=True, shell=True)
process = subprocess.Popen(['git stash'], stdout=subprocess.DEVNULL, text=True, shell=True)
process = subprocess.Popen(['git pull'], stdout=subprocess.PIPE, text=True, shell=True)
for line in iter(process.stdout.readline, ''):
    if "Already up to date" in line:
        print("\n—>Обновления не найдены, у вас последняя версия!")
        break
    elif "Updating" in line:
        print("\n—>Обновления успешно установлены!")
        quit()

        
