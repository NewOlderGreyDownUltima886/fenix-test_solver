import subprocess, sys, os

#check and install updates
if len(sys.argv) > 1:
  if sys.argv[1] == "1":
    print("Для Windows-платформы обновления не предпологаются!")
  else:
    subprocess.call(["python", "updater.py"])
else:
  subprocess.call(["python", "updater.py"])


#start launcher
if len(sys.argv) > 1:
    if sys.argv[1] == "1":
        subprocess.call(["python", "launcher.py", "1"])
else:
    subprocess.call(["python", "launcher.py"])

print("\nПрощайте!")
