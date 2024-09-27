import os

if __name__ == '__main__':
    print("Welcome to robo created by Sumit")
    while True:
        x = input('Enter what you want me to speak: ')
        if x.lower() == "q":
            os.system("powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye bye friend')\"")
            break
         os.system(command)
.