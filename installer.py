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

apache=input("IS APACHE2 SERVER IS INSTALLED IN YOUR SYSTEM? [Y/n] : ")
if apache=="n" or apache=="N":
          os.system("sudo apt-get install apache2")
else:
     print("HURRAY....")

path=os.getcwd()
with open("febrev.sh","w+") as fr:
      fr.write(f"python3 {path}/febrev-venom.py")
os.system(f"cp {path}/febrev.sh /bin/febrev1")
os.system("chmod +x /bin/febrev.sh")
print("")
print("NOW YOU CAN RUN FEBREV-VENOM FROM ANYWERE BY TYPING   >> ./febrev.sh")




print("STARTING FEBREV VENOM......#######################")
os.system("chmod +x *")
os.system("sudo python3 febrev-venom.py")
