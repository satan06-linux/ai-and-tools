import random
import datetime
from bs4 import BeautifulSoup
import pyttsx3   
import wikipedia
import speech_recognition as sr 
import psutil  
import pyautogui
import webbrowser
import requests
import pyjokes 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from requests import get
import operator
import subprocess
import time
import ctypes
import PyPDF2



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour< 12:
        a = "Good morning boss", "Good morning sir", "Hello boss Good Morning", "O, Good morning sir", "O, good morning boss", "Wow! Welcome back boss sir"
        speak(random.choice(a))
    elif hour>= 12 and hour< 18:
        b = "Good Afternoon boss", "Good Afternoon sir", "Hello boss Good Afternoon", "O, Good Afternoon sir", "O, good Afternoon boss", "Wow! Welcome back boss sir"   
        speak(random.choice(b))
    elif hour>= 18 and hour< 20:
        c = "Good Evening boss", "Good Evening sir", "Hello boss Good Evening", "O, Good Evening sir", "O, good Evening boss", "Wow! Welcome back boss sir"
        speak(random.choice(c))

    elif hour>=20 and hour<0:
        d = "Good Night boss Have a good dream"

wishMe()
wel = "So, how can i help you sir!", "How can i help", "Give me a command Sir", "Online and ready sir", "What can i do for you", "Please give me a command Sir"
speak(random.choice(wel)) 



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)
        speak("Try to say again")
        return "None"
    return query

if __name__ == '__main__':
    while True:
        query  = takeCommand().lower()

        if "jarvis"in query or "hey" in query :
            speak("yes sir")
        
        if 'wikipedia' in query:
            speak("Searching on wiki")
            try:
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                
                speak("so, wikipedia says")
                speak(results)
                
            except:
                speak("Not available on wikipedia")
         
        if 'stop' in query or 'over' in query or 'bye' in query or 'quit' in query or 'see you' in query or 'go' in query:
            f = "bye sir", "ok bye sir", "see you again sir", "bye bye", "As your wish sir", "Waiting for Activation sir", "As your wish, but I dont want to go sir!"
            speak(random.choice(f))
            
            break
        elif 'open firefox' in query or 'search on firefox' in query or 'type on firefox' in query:
            speak("what should i search?")
            h = takeCommand().lower()
            webbrowser.open(f"https://www.bing.com/search?q={h}")
            results = wikipedia.summary(query, sentences = 2)
            speak(results)
            from automation import firefoxAuto
            firefoxAuto(query)
            

        elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            speak(random.choice(dg))
            x = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
            from automation import youtubeAuto
            youtubeAuto(query)
            
         
            
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.bing.com/search?q={query}")
            speak("As your wish sir")


        elif 'joke' in query:
            speak(pyjokes.get_joke())          

        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system sir?")
            ch = takeCommand()
            if "yes" in ch:
                
                os.system("shutdown /s /t 1")
            else:
                speak("ok sir")
        elif "play music" in query:
            speak("tell me the song name!")
            p = takeCommand()
            webbrowser.open(f"https://gaana.com//search?q={p}")

        elif "play" in query:
            query = query.replace("play", "")
            speak("Ok sir opening your desired song!")
            webbrowser.open(f"https://gaana.com//search?q={query}")    
        elif 'jarvis introduce yourself' in query :
            speak("Wait, i am introducing myself. My name is Jarvi, I am an Assistant made by python progarmming, i can do many works like playing music, opening progarms, opening youtube, searching on web and many more")
        elif "who am i" in query:
            jh = "if you are speaking then, definately you are a human", "You are boss", "You are a human", "I cant identify peoples with their vocies, may be you are boss or anybody with relation of boss"
            speak(random.choice(jh))
        elif 'hello' in query:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gethering information, how can i help?", "Online and ready"
            speak(random.choice(gf))

        elif "open web whatsapp" in query:
            webbrowser.open(f"https://web.whatsapp.com/search?")
            speak("opening web whatsapp")

        elif "open mail" in query:
            webbrowser.open(f"https://mail.google.com/mail/search?")
            speak("opening mail")
            
        elif "open amazon" in query:
            webbrowser.open(f"https://www.amazon.in/?")
            speak("opening amazon")

        elif "open c language" in query:
            webbrowser.open(f"https://www.programiz.com/c-programming/online-compiler//?")
            speak("opening c language for practicising ")

        elif "open hackerrank" in query :
            webbrowser.open(f"https://www.hackerrank.com/dashboard/?")
            speak("opening hackerank")

        elif "open geeksforgeeks" in query :
            webbrowser.open(f"https://www.geeksforgeeks.org/c-programming-examples//?")
            speak("opening geeksforgeeks examples")
        
        elif "logout" in query :
           
            if "yes" in query :
                os.system("shutdown -l")
                speak("logging out ")

            else :
                print("okay sir not logging out")


        elif "disk usage" in query :
            disk_usage = psutil.disk_usage('/')
            print(f"Disk Usage: {disk_usage.percent}%")
            time.sleep(1)

        elif "facts of the day" in query or "facts" in query :
            webbrowser.open(f"https://bladenonline.com/10-fun-facts-of-the-day/?")
            print("opening todays facts")

        elif "calculate" in query :
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready to calculate")
                print("listening ....")
                
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string= r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        "+":operator.add,
                        "-":operator.sub,
                        "x":operator.mul,
                        "divided" : operator._truediv_,
                        }[op]
                    
                    
                def eval_binary_expr(op1, op2, oper):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))



        elif "open calculator" in query :
            print("are you sure")

            if "yes" in query :
                num1 = int(input("enter a number")) 
                num2 = int(input("enter a number"))

                action = str(input("choose action : addition, substraction, multiplication, division, ->"))

                print("the result is", end="") 

                if action == "addition" :
                    print("num1+num2")


                elif action == "substraction" :
                    print("num1-num2")

                elif action == "multiplication" :
                    print("num1*num2")

                elif action == "division" :
                    print(num1/num2)


            else :
                print("closing calculator")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print("time{strTime}")

        elif "date" in query:
            datetime.datetime.date()

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")


        elif "volume down" in query :
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip adress is {ip}")


        elif "close the tab" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('w') 
            pyautogui.keyUp('ctrl')

        elif "open new tab" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('t')
            pyautogui.keyUp('ctrl')

        elif "open new tab" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('n')
            pyautogui.keyUp('ctrl')

        elif "show history" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('h')
            pyautogui.keyUp('ctrl')

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif"temperature" in query:
           search = "temperature in telangana"
           url = f"http://www.google.com/search?q={search}"
           r = requests.get(url)
           data = BeautifulSoup(r.text,"html.parser")
           temp = data.find("div",class_="BNeawe").text
           speak(f"current {search} is {temp}")

        elif "open website" in query:
            speak("ok sir , opening.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = "https://www." + web1 + ".com"
            webbrowser.open(web2)
            speak("opened website sir!")  
        
        elif "take a screenshot" in query:
            speak("okay sir where should i place the screenshot ")
            name =takeCommand().lower()
            speak("pls wait sir take a screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot uploaded")   
        
        else :
            print("could not take a screenshot")
################################### notepad automated ###################################################

def notepad() :
    speak("tell in query .")
    speak("i am ready note")

    writes = takeCommand().lower()

    time = datetime.datetime.now().strftime("%H:%M:%S")

    filename = str(time) + "-note.txt"
    with open(filename, "w") as file :
        file.qrite(writes)

    path_1 = "enter the path of the notepad file" + str(filename)

    path_2 = "enter the second path of the notepad file"
    

    os.rename(path_1, path_2)
    os.startfile(path_2)


def closenotepad() :
    os.startfile("Task kill/ F/ im notepad.exe")
    breakpoint

######################## cpu usage checker ##########################3

def cpu_usage_checker(interval=1):
    while True:
        # Get the CPU usage percentage
        cpu_percent = psutil.cpu_percent(interval=interval)
        speak(f"CPU Usage: {cpu_percent}%")
        time.sleep(3) 
        
if __name__ == "__main__":

    speak("Starting CPU usage checker. Press Ctrl+C to stop.")

    try:
        cpu_usage_checker()
    
    except KeyboardInterrupt:
        speak("CPU usage checker stopped.")


######################## battery status ########################
def battery_status_checker():
    battery = psutil.sensors_battery()
    
    if battery is None:
        print("No battery information available.")
        return

    percent = battery.percent
    is_plugged = battery.power_plugged
    time_left = battery.secsleft

    print(f"Battery Percentage: {percent}%")
    print("Charging Status: ", "Plugged In" if is_plugged else "Not Plugged In")

    if time_left == psutil.POWER_TIME_UNLIMITED:
        print("Battery status: Charging (time left: unlimited)")
    elif time_left == psutil.POWER_TIME_UNKNOWN:
        print("Battery status: Unable to determine time left")
    else:
        hours, seconds = divmod(time_left, 3600)
        minutes, seconds = divmod(seconds, 60)
        print(f"Time Left: {hours} hours and {minutes} minutes")

if __name__ == "__main__":
    print("Battery status checker:")
    battery_status_checker()

######################### password generator ####################################

def generate_password(length: int) : 

    length = takeCommand().lower()
    length = int(length)
    if length is None or length < 1:
        raise ValueError("Length must be a positive integer")

    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    passwd_types = upper_case + lower_case + numbers

    password = ""

    for _ in range(length):
        password += random.choice(passwd_types)

    return password  
  

if __name__ == "__main__":  


    pass_str = generate_password(len)  

    print("A randomly generated Password is:", pass_str)  

############################# memory utilization ############################

def memory_utilization_checker():
    while True:
        # Get the memory usage of the current process
        process = psutil.Process()
        mem_info = process.memory_info()
        
        # Get the virtual memory usage of the system
        virtual_memory = psutil.virtual_memory()
        
        print(f"--- Memory Utilization ---")
        print(f"Process Memory Usage: {mem_info.rss / (1024 ** 2):.2f} MB")  # Resident Set Size
        print(f"Virtual Memory Total: {virtual_memory.total / (1024 ** 2):.2f} MB")
        print(f"Virtual Memory Used: {virtual_memory.used / (1024 ** 2):.2f} MB")
        print(f"Virtual Memory Available: {virtual_memory.available / (1024 ** 2):.2f} MB")
        print(f"Memory Usage Percentage: {virtual_memory.percent}%")
        print("--------------------------")
        
        time.sleep(3)  # Wait for the specified interval before checking again

if __name__ == "__main__":
    print("Starting memory utilization checker. Press Ctrl+C to stop.")
    try:
        memory_utilization_checker()  
    except KeyboardInterrupt:
        print("\nMemory utilization checker stopped.")

############################### cpu timer #################################
def cpu_time_checker():
    process = psutil.Process()
    while True:

        cpu_time_process = process.cpu_times()

        cpu_time_system = psutil.cpu_times()
        
        print(f"--- CPU Time ---")
        print(f"Process CPU Time: user={cpu_time_process.user:.2f} sec, system={cpu_time_process.system:.2f} sec")
        print(f"System CPU Time: user={cpu_time_system.user:.2f} sec, system={cpu_time_system.system:.2f} sec")
        print(f"System Idle Time: {cpu_time_system.idle:.2f} sec")
        print("------------------")
        
        time.sleep(3) 
if __name__ == "__main__":
    print("Starting CPU time checker. Press Ctrl+C to stop.")
    try:
        cpu_time_checker()  
    except KeyboardInterrupt:
        print("\nCPU time checker stopped.")


####################################### cpu count ######################################

def cpu_count_checker():
    while True:

        logical_cpus = psutil.cpu_count(logical=True)
        

        physical_cpus = psutil.cpu_count(logical=False)
        
        print(f"--- CPU Count ---")
        print(f"Logical CPU Count: {logical_cpus}")
        print(f"Physical CPU Count: {physical_cpus}")
        print("------------------")
        
        time.sleep(3) 
if __name__ == "__main__":
    print("Starting CPU count checker. Press Ctrl+C to stop.")
    try:
        cpu_count_checker() 
    except KeyboardInterrupt:
        print("\nCPU count checker stopped.")


############################################# open and close cmd ##############################
cmd_process = None

def open_cmd():
    global cmd_process
    try:
        # Open Command Prompt and store the process
        cmd_process = subprocess.Popen('cmd.exe')
        print("Command Prompt opened.")
    except Exception as e:
        print(f"An error occurred: {e}")

def close_cmd():
    global cmd_process
    if cmd_process is not None:
        try:
            # Terminate the Command Prompt process
            cmd_process.terminate()  # Gracefully terminate
            cmd_process.wait()       # Wait for the process to terminate
            print("Command Prompt closed.")
            cmd_process = None  # Reset the cmd_process variable
        except Exception as e:
            print(f"An error occurred while closing cmd: {e}")
    else:
        print("No Command Prompt is currently open.")

if __name__ == "__main__":
    print("Welcome to Jarvis! Type 'open cmd' to open the Command Prompt, 'close cmd' to close it.")
    
    while True:
        command = input("You: ").strip().lower()
        
        if command == "open cmd":
            open_cmd()
        elif command == "close cmd":
            close_cmd()
        elif command == "exit":
            print("Exiting Jarvis. Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")


########################### reader ##################################

def reader(filename, read_from_which_page_number=0, startfile=True):

    if startfile == True:
        os.startfile(filename)

        book = open(filename, "rb")

        pdf_reader = PyPDF2.pdfFileReader(book)

        pages = pdf_reader.getNumPages()
        print("number of pages = ", pages)

        page = pdf_reader.getPage(read_from_which_page_number)

        text = page.extract_text()

        book.close()

        return text()
    
reader()


################################ windows update######################
def restart_system(time_delay):
    print("Restarting the system ...")

    os.system(f"shutdown /r /t {time_delay}")


def lock_screen():
    ctypes.wind1l.user32.LockWorkStation()


def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls() 
            server.login(sender_email, sender_password)  
            server.send_message(msg) 

        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to Jarvis! Type 'send email' to send an email or 'exit' to quit.")
    
    while True:
        command = input("You: ").strip().lower()
        
        if command == "send email":
            sender_email = input("Enter your email: ")
            sender_password = input("Enter your password: ")
            recipient_email = input("Enter recipient's email: ")
            subject = input("Enter the subject: ")
            body = input("Enter the email body: ")
            
            send_email(sender_email, sender_password, recipient_email, subject, body)
        
        elif command == "exit":
            print("Exiting Jarvis. Goodbye!")
            break
        
        else:
            print("Unknown command. Please try again.")

