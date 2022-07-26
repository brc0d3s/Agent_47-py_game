import time
import random
print("Genetically engineered from conception...")
time.sleep(1.5)
print("To be the perfect killing machine...")
time.sleep(1.5)
print("He's the culmination of decades of research...")
time.sleep(2)
print("Endowed with unprecedented speed, stamina and intelligence...\n\n")
time.sleep(1)
print("KNOWN ONLY AS AGENT 47\n\n")
if input("Hello Agent 47 ready for a mission...\nType 'yes' to start\n")=="yes":
    print("Mission 1....\n")
    time.sleep(1.2)
print('You are in a lab they are researching on you\nYou see a worker He has some medical samples which are very useful\nSteal them and take it to HQ')
ataque=input("[1] Escape quietly \n[2] Attack the worker from behind\n")
if ataque=='1':
    time.sleep(1)
    print("You were caught by the Staff\n\n>>>Mission Failed<<<\n\n") 
    
if ataque=='2':
    time.sleep(1)
    ataque=input("Sucessful\n\n[3] Take the samples \n[4] Dispose the body\n")
    
if ataque=='3':
    time.sleep(1)
    ataque=input("Sucessful\n\n[5] Take the samples to HQ \n[6] Take the samples and change your appearence\n")  
if ataque=='4':
    print("Someone saw you Disposing the body\nAnd complained to the police\n\nMission Failed\n\n")
    
if ataque=='5':
    time.sleep(1)
    print("You were caught for stealing the samples by a staff\n\nMission Failed\n\n")
if ataque=='6':
    time.sleep(1)
    ataque=input("Sucessful\n\n[7] Take the samples and ride to HQ \n")

if ataque=='7':
    time.sleep(1)
    ataque=input("Sucessful\n\n[8] Use short way (reach faster)\n[9] Use long way\n")

if ataque=='8':
    time.sleep(1)
    print("You were struck in a traffic jam\n\nMission Failed\n\n")
if ataque=='9':
    time.sleep(1)
    print("Sucessful\n\n<<<< MISSION ACCOMPLISHED >>>>\n\n")
   