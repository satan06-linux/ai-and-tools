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
    if 0 <= hour < 12:
        greetings = [
            "Good morning boss", "Good morning sir", "Hello boss Good Morning",
            "O, Good morning sir", "O, good morning boss", "Wow! Welcome back boss sir"
        ]
    elif 12 <= hour < 18:
        greetings = [
            "Good Afternoon boss", "Good Afternoon sir", "Hello boss Good Afternoon",
            "O, Good Afternoon sir", "O, good Afternoon boss", "Wow! Welcome back boss sir"
        ]
    elif 18 <= hour < 20:
        greetings = [
            "Good Evening boss", "Good Evening sir", "Hello boss Good Evening",
            "O, Good Evening sir", "O, good Evening boss", "Wow! Welcome back boss sir"
        ]
    else:
        greetings = ["Good Night boss Have a good dream"]
    speak(random.choice(greetings))


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(f"Error: {e}")
        speak("Try to say again")
        return "None"
    return query.lower()


def search_wikipedia(query):
    speak("Searching on Wikipedia")
    try:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("So, Wikipedia says")
        speak(results)
    except Exception:
        speak("Not available on Wikipedia")


def open_website(site_name):
    site_name = site_name.replace("open", "").replace("website", "").replace("jarvis", "").strip()
    if not site_name.startswith("http"):
        site_name = "https://www." + site_name + ".com"
    webbrowser.open(site_name)
    speak("Opened website sir!")


def take_screenshot(name):
    speak("Please wait sir, taking a screenshot")
    time.sleep(2)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("Screenshot saved")


def generate_password():
    speak("Please tell me the length of the password")
    length_str = takeCommand()
    try:
        length = int(length_str)
        if length < 1:
            raise ValueError
    except ValueError:
        speak("Length must be a positive integer")
        return None

    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    passwd_types = upper_case + lower_case + numbers

    password = "".join(random.choice(passwd_types) for _ in range(length))
    return password


def cpu_usage_checker(interval=1):
    while True:
        cpu_percent = psutil.cpu_percent(interval=interval)
        speak(f"CPU Usage: {cpu_percent} percent")
        time.sleep(3)


def battery_status_checker():
    battery = psutil.sensors_battery()
    if battery is None:
        speak("No battery information available.")
        return

    percent = battery.percent
    is_plugged = battery.power_plugged
    time_left = battery.secsleft

    speak(f"Battery Percentage: {percent} percent")
    speak("Charging Status: Plugged In" if is_plugged else "Not Plugged In")

    if time_left == psutil.POWER_TIME_UNLIMITED:
        speak("Battery status: Charging with unlimited time left")
    elif time_left == psutil.POWER_TIME_UNKNOWN:
        speak("Battery status: Unable to determine time left")
    else:
        hours, remainder = divmod(time_left, 3600)
        minutes, _ = divmod(remainder, 60)
        speak(f"Time Left: {hours} hours and {minutes} minutes")


def memory_utilization_checker():
    while True:
        process = psutil.Process()
        mem_info = process.memory_info()
        virtual_memory = psutil.virtual_memory()

        print(f"--- Memory Utilization ---")
        print(f"Process Memory Usage: {mem_info.rss / (1024 ** 2):.2f} MB")
        print(f"Virtual Memory Total: {virtual_memory.total / (1024 ** 2):.2f} MB")
        print(f"Virtual Memory Used: {virtual_memory.used / (1024 ** 2):.2f} MB")
        print(f"Virtual Memory Available: {virtual_memory.available / (1024 ** 2):.2f} MB")
        print(f"Memory Usage Percentage: {virtual_memory.percent}%")
        print("--------------------------")

        time.sleep(3)


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


def cpu_count_checker():
    while True:
        logical_cpus = psutil.cpu_count(logical=True)
        physical_cpus = psutil.cpu_count(logical=False)

        print(f"--- CPU Count ---")
        print(f"Logical CPU Count: {logical_cpus}")
        print(f"Physical CPU Count: {physical_cpus}")
        print("------------------")

        time.sleep(3)


cmd_process = None


def open_cmd():
    global cmd_process
    try:
        cmd_process = subprocess.Popen('cmd.exe')
        print("Command Prompt opened.")
    except Exception as e:
        print(f"An error occurred: {e}")


def close_cmd():
    global cmd_process
    if cmd_process is not None:
        try:
            cmd_process.terminate()
            cmd_process.wait()
            print("Command Prompt closed.")
            cmd_process = None
        except Exception as e:
            print(f"An error occurred while closing cmd: {e}")
    else:
        print("No Command Prompt is currently open.")


def reader(filename, read_from_page=0, startfile=True):
    if startfile:
        os.startfile(filename)

    with open(filename, "rb") as book:
        pdf_reader = PyPDF2.PdfFileReader(book)
        pages = pdf_reader.numPages
        print(f"Number of pages = {pages}")

        if read_from_page >= pages:
            speak("Page number exceeds total pages.")
            return ""

        page = pdf_reader.getPage(read_from_page)
        text = page.extract_text()
        return text


def restart_system(time_delay):
    speak("Restarting the system")
    os.system(f"shutdown /r /t {time_delay}")


def lock_screen():
    ctypes.windll.user32.LockWorkStation()


def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        speak("Email sent successfully!")
    except Exception as e:
        speak(f"An error occurred: {e}")


def main():
    wishMe()
    welcome_msgs = [
        "So, how can I help you sir!", "How can I help?", "Give me a command Sir",
        "Online and ready sir", "What can I do for you?", "Please give me a command Sir"
    ]
    speak(random.choice(welcome_msgs))

    while True:
        query = takeCommand()

        if query == "none":
            continue

        if "jarvis" in query or "hey" in query:
            speak("Yes sir")

        if 'wikipedia' in query:
            search_wikipedia(query)

        elif any(word in query for word in ['stop', 'over', 'bye', 'quit', 'see you', 'go']):
            farewell_msgs = [
                "Bye sir", "Ok bye sir", "See you again sir", "Bye bye",
                "As your wish sir", "Waiting forActivation sir", "As your wish, but I don't want to go sir!"
            ]
            speak(random.choice(farewell_msgs))
            break

        elif 'open firefox' in query or 'search on firefox' in query or 'type on firefox' in query:
            speak("What should I search?")
            h = takeCommand()
            if h != "none":
                webbrowser.open(f"https://www.bing.com/search?q={h}")
                speak("Search completed on Firefox.")

        elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            speak("What should I search on YouTube?")
            x = takeCommand()
            if x != "none":
                webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
                speak("Opened YouTube search results.")

        elif 'search' in query:
            query = query.replace("search", "").strip()
            webbrowser.open(f"https://www.bing.com/search?q={query}")
            speak("As your wish sir")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system sir?")
            ch = takeCommand()
            if "yes" in ch:
                speak("Shutting down the system.")
                os.system("shutdown /s /t 1")
            else:
                speak("Ok sir")

        elif "play music" in query or "play" in query:
            speak("Tell me the song name!")
            p = takeCommand()
            if p != "none":
                webbrowser.open(f"https://gaana.com/search?q={p}")
                speak("Playing your desired song!")

        elif 'jarvis introduce yourself' in query:
            speak("Wait, I am introducing myself. My name is Jarvis. I am an assistant made by Python programming. I can do many tasks like playing music, opening programs, opening YouTube, searching on the web, and many more.")

        elif "who am i" in query:
            responses = [
                "If you are speaking then, definitely you are a human",
                "You are boss", "You are a human",
                "I can't identify people by their voices, maybe you are boss or somebody related to boss"
            ]
            speak(random.choice(responses))

        elif 'hello' in query:
            greetings = [
                "O hello sir", "Hi sir", "I am here for your help sir!",
                "Hello sir", "I was surfing the web and gathering information, how can I help?",
                "Online and ready"
            ]
            speak(random.choice(greetings))

        elif "open web whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("Opening web WhatsApp")

        elif "open mail" in query:
            webbrowser.open("https://mail.google.com/mail/")
            speak("Opening mail")

        elif "open amazon" in query:
            webbrowser.open("https://www.amazon.in/")
            speak("Opening Amazon")

        elif "open c language" in query:
            webbrowser.open("https://www.programiz.com/c-programming/online-compiler/")
            speak("Opening C language for practicing")

        elif "open hackerrank" in query:
            webbrowser.open("https://www.hackerrank.com/dashboard/")
            speak("Opening HackerRank")

        elif "open geeksforgeeks" in query:
            webbrowser.open("https://www.geeksforgeeks.org/c-programming-examples/")
            speak("Opening GeeksforGeeks examples")

        elif "logout" in query:
            speak("Are you sure you want to logout?")
            confirm = takeCommand()
            if "yes" in confirm:
                os.system("shutdown -l")
                speak("Logging out")
            else:
                speak("Okay sir, not logging out")

        elif "disk usage" in query:
            disk_usage = psutil.disk_usage('/')
            speak(f"Disk Usage: {disk_usage.percent} percent")

        elif "facts of the day" in query or "facts" in query:
            webbrowser.open("https://bladenonline.com/10-fun-facts-of-the-day/")
            speak("Opening today's facts")

        elif "calculate" in query:
            speak("Ready to calculate. Please say your expression like '5 plus 3'")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                my_string = r.recognize_google(audio)
                print(f"Calculating: {my_string}")
                def get_operator_fn(op):
                    return {
                        "+": operator.add,
                        "plus": operator.add,
                        "-": operator.sub,
                        "minus": operator.sub,
                        "x": operator.mul,
                        "times": operator.mul,
                        "divided": operator.truediv,
                        "by": operator.truediv
                    }[op]

                def eval_binary_expr(op1, op2, oper):
                    op1, op2 = float(op1), float(op2)
                    return get_operator_fn(oper)(op1, op2)

                tokens = my_string.split()
                if len(tokens) == 3:
                    op1, oper, op2 = tokens
                    result = eval_binary_expr(op1, op2, oper)
                    speak(f"Your result is {result}")
                else:
                    speak("Sorry, I could not understand the expression.")
            except Exception as e:
                speak("Sorry, I could not calculate that.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "date" in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {strDate}")

        elif "volume up" in query:
            for _ in range(8):
                pyautogui.press("volumeup")
            speak("Volume increased")

        elif "volume down" in query:
            for _ in range(8):
                pyautogui.press("volumedown")
            speak("Volume decreased")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "close the tab" in query:
            pyautogui.hotkey('ctrl', 'w')
            speak("Closed the current tab")

        elif "open new tab" in query:
            pyautogui.hotkey('ctrl', 't')
            speak("Opened a new tab")

        elif "open new window" in query:
            pyautogui.hotkey('ctrl', 'n')
            speak("Opened a new window")

        elif "show history" in query:
            pyautogui.hotkey('ctrl', 'h')
            speak("Showing history")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("Switched window")

        elif "temperature" in query:
            search = "temperature in telangana"
            url = f"http://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")

        elif "open website" in query:
            open_website(query)

        elif "take a screenshot" in query:
            speak("Okay sir, what should I name the screenshot?")
            name = takeCommand()
            if name != "none":
                take_screenshot(name)
            else:
                speak("Screenshot cancelled")

        elif "generate password" in query:
            password = generate_password()
            if password:
                speak(f"Generated password is {password}")
                print(f"Generated password: {password}")

        elif "open cmd" in query:
            open_cmd()

        elif "close cmd" in query:
            close_cmd()

        elif "send email" in query:
            speak("Please enter your email credentials and recipient details in the console.")
            sender_email = input("Enter your email: ")
            sender_password = input("Enter your password: ")
            recipient_email = input("Enter recipient's email: ")
            subject = input("Enter the subject: ")
            body = input("Enter the email body: ")
            send_email(sender_email, sender_password, recipient_email, subject, body)

        else:
            speak("Sorry sir, I did not understand that command.")


if __name__ == "__main__":
    main()
