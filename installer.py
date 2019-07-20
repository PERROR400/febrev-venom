import os

metasploit=input("IS METASPLOIT-FRAMEWORK ALREADY INSTALLED IN YOUR SYSTEM ? [Y/n] : ")
if metasploit=="n" or metasploit=="N":
            os.sytem("sudo apt-get install metasploit")
else:
     print("NICE ......!")

apksign=input("IS APKSIGNER ALREADY INSTALLED IN YOUR SYSTEM? [Y/n]? : ")
if apksign=="n" or apksign=="N":
           os.system("sudo apt-get install apksigner")
else: 
     print("NICE .....")
     

python3=input("IS PYTHON3 INSTALLED IN YOUR SYSTEM? [Y/n] : ")
if python3=="n" or python3=="N":
           os.system("sudo apt-get install python3")



print("STARTING FEBREV VENOM......#######################")
os.system("chmod +x *")
os.system("sudo python3 febrev-venom.py")
