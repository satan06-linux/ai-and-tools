import takecommand 
import pyautogui
import query
import time
import webbrowser
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


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


def open_github():
    # The URL of GitHub
    github_url = "https://github.com"
    
    # Open the URL in the default web browser
    webbrowser.open(github_url)

# Call the function to open GitHub
open_github()

if __name__ == "__main__":
    open_github()

    if "command" == "login":
        print(f"Enter the username and password")
        username = input("Username:")
        password = input("Password:")
        print(f"is the username {username} and password{password} correct?")

        if "yes" in query or "it is correct" in query or "true" in query or "correct" in query or "sure it is" in query:
            print(f"logging in github with username{username}")
            #login in github with username and password

        else:
            print(f"pls enter the correct username and password")

        if "search in github" in query:
            pyautogui.press("/")
            pyautogui.press("/")
            pyautogui.press("/")
            pyautogui.press("/")
            query = takeCommand().lower()
            pyautogui.typewrite("query")
            pyautogui.typewrite("query")
            pyautogui.press("enter")
            pyautogui.press("enter")

        else:
            print(f"what would you like to do in github sir?")

        if "what is my username" in query:
            print(f"your username is {username}")

        else:
            print("sir what should i do")

        if "what can i do in github" in query or "what shall we do in github" in query or "what is github used for" in query or " what are the things we can do in github" in query:
            print(f"we can do the following things in github sir:")
            
            print(f"1. Create a new repository")
            print(f"2. Clone a repository")
            print(f"3. Fork a repository")
            print(f"4. Star a repository")
            print(f"5. Watch a repository")
            print(f"6. Create an issue")
            print(f"7. Create a pull request")
            print(f"8. Create a new branch")
            print(f"9. Merge a branch")
            print(f"10. Delete a branch")
            print(f"11. Delete a repository")
            print(f"12. Create a new file")
            print(f"13. Delete a file")
            print(f"14. Rename a file")
            print(f"15. Commit changes")
            print(f"16. Push changes")

            print(f"17. Pull changes")
            print(f"18. Merge changes")
            print(f"19. Create a new tag")

            if "focus on th search bar" in query:
                print(f"okay sir focusing on the search bar")
                #s is to short cut for opening search box of the user to find the file
                pyautogui.press("s") 
                pyautogui.press("s")
                pyautogui.press("s")
                pyautogui.press("s")
                pyautogui.press("s")
                pyautogui.press("s")

                
                print("what would like to open in the user files sir")
                query = takeCommand().lower()
                pyautogui.write("query")
                pyautogui.write("query")
                pyautogui.write("query")
                pyautogui.write("query")
                pyautogui.write("query")
                pyautogui.write("query")
                pyautogui.write("query")
                pyautogui.write("query")

# now we for clicking enter we can use the below function then it will open the file in the user's files
                pyautogui.press("enter")
                pyautogui.press("enter")
                pyautogui.press("enter")
                pyautogui.press("enter")
                pyautogui.press("enter")
                pyautogui.press("enter")
            
            if " go to notification" in query or "open notification " in query :
                print(f"okay sir opening notification")
                pyautogui.hotkey("G", "N")
                pyautogui.hotkey("G", "N")
                pyautogui.hotkey("G", "N")
                pyautogui.hotkey("G", "N")
                pyautogui.hotkey("G", "N")
                pyautogui.hotkey("G", "N")
                pyautogui.hotkey("G", "N")
                pyautogui.hotkey("G", "N")

            elif "open the code tab" in query or"ope code tab" in query or "code tab" in query:
                print(f"okay sir opening code tab in github pls wait....")
                pyautogui.hotkey("G", "C")
                pyautogui.hotkey("G", "C")
                pyautogui.hotkey("G", "C")
                pyautogui.hotkey("G", "C")
                pyautogui.hotkey("G", "C")
                pyautogui.hotkey("G", "C")
                pyautogui.hotkey("G", "C")
                pyautogui.hotkey("G", "C")

            elif "open the issue tab" in query or "open issue tab" in query or "issue tab" in query:
                print(f"okay sir opening issue tab in github pls wait....")
                pyautogui.hotkey("G", "I")
                pyautogui.hotkey("G", "I")
                pyautogui.hotkey("G", "I")
                pyautogui.hotkey("G", "I")
                pyautogui.hotkey("G", "I")
                print(f"what should i write in issue tab pls say sir")
                command = takeCommand().lower()
                pyautogui.typewrite('command')


            elif "open the pull request tab" in query or "open pull request tab" in query or "pull request tab" in query or "request tab" in query:
                print(f"okay sir opening pull request tab in github pls wait....")
                pyautogui.hotkey("G", "P")
                pyautogui.hotkey("G", "P")
                pyautogui.hotkey("G", "P")
                pyautogui.hotkey("G", "P")
                pyautogui.hotkey("G", "P")
                pyautogui.hotkey("G", "P")

            elif " open project tab" in query or "project tab" in query or "open project lab" in query:
                print(f"okay sir opening project tab in github pls wait....")
                pyautogui.hotkey("G", "B")
                pyautogui.hotkey("G", "B")
                pyautogui.hotkey("G", "B")
                pyautogui.hotkey("G", "B")
                pyautogui.hotkey("G", "B")
                pyautogui.hotkey("G", "B")
                pyautogui.hotkey("G", "B")
                pyautogui.hotkey("G", "B")

            elif "open wiki tab" in query or "wiki tab" in query :
                print(f"okay sir opening the wiki tab in github pls wait ....")
                pyautogui.hotkey("G", "W")
                pyautogui.hotkey("G", "W")
                pyautogui.hotkey("G", "W")
                pyautogui.hotkey("G", "W")
                pyautogui.hotkey("G", "W")
                pyautogui.hotkey("G", "W")
                pyautogui.hotkey("G", "W")
                pyautogui.hotkey("G", "W")
            
#################### SOURCE CODE EDITING (GITHUB) ####################
            
            elif "searching in file editor" in query or "file editor" in query:
                print(f"okay sir searching in file editor pls wait....")
                pyautogui.hotkey("ctrl", "F")
                pyautogui.hotkey("ctrl", "F")
                pyautogui.hotkey("ctrl", "F")
                pyautogui.hotkey("ctrl", "F")
                pyautogui.hotkey("ctrl", "F")
                pyautogui.hotkey("ctrl", "F")
                print(f"pls say what we should find in file editor sir ")
                command = takeCommand().lower()
                pyautogui.typewrite('command')

            elif "jump to line" in query or "jump " in query:
                print(f"okay sir jumping to line pls wait....")
                pyautogui.hotkey("alt", "G")
                pyautogui.hotkey("alt", "G")
                pyautogui.hotkey("alt", "G")
                pyautogui.hotkey("alt", "G")
                pyautogui.hotkey("alt", "G")
                print(f"pls say the line we should jump sir ")
                command = takeCommand().lower()
                pyautogui.typewrite('command')
                 
            elif "replace all" in query:
                print(f"okay sir replacing all pls wait....") 
                pyautogui.hotkey("ctrl", "shift, ", "R")
                pyautogui.hotkey("ctrl", "shift, ", "R")
                pyautogui.hotkey("ctrl", "shift, ", "R")
                pyautogui.hotkey("ctrl", "shift, ", "R")
                pyautogui.hotkey("ctrl", "shift, ", "R")
                pyautogui.hotkey("ctrl", "shift, ", "R")

            elif "undo" in query or "undo the code" in query:
                print(f"okay sir undoing the code pls wait....")
                pyautogui.hotkey("ctrl", "Z")
                pyautogui.hotkey("ctrl", "Z")
                pyautogui.hotkey("ctrl", "Z")
                pyautogui.hotkey("ctrl", "Z")
                pyautogui.hotkey("ctrl", "Z")
                pyautogui.hotkey("ctrl", "Z")
            
            elif "Redo" in query or "Redo the code" in query:
                print(f"okay sir redoing the codes in the github pls wait ....")
                pyautogui.hotkey("ctrl", "Y")
                pyautogui.hotkey("ctrl", "Y")
                pyautogui.hotkey("ctrl", "Y")
                pyautogui.hotkey("ctrl", "Y")
                pyautogui.hotkey("ctrl", "Y")
                pyautogui.hotkey("ctrl", "Y")

################# source code browsing(GITHUB) ####################

            elif "file finder" in query or "activate the file finder" in query or "activte finders" in query:
                print(f"okay sir activating the file finders in process pls wait .....")
                pyautogui.press("T")
                pyautogui.press("T")
                pyautogui.press("T")
                pyautogui.press("T")
                pyautogui.press("T")

                print(f"what should i find pls say key word")
                command = takeCommand().lower()
                pyautogui.typewrite('command')

            elif "jump to the line in our code" in query or "jump to the line" in query:
                print(f"okay sir jumping too the line pls say which line you want to jump")
                pyautogui.press("L")
                pyautogui.press("L")
                pyautogui.press("L")
                pyautogui.press("L")
                pyautogui.press("L")
                pyautogui.press("L")
                pyautogui.press("L")


            elif "show comment" in query or "comment" in query or " hide comments" in query or "hide" in query:
                print(f"okay sir pls wait .....") 

                pyautogui.press("I")
                pyautogui.press("I")
                pyautogui.press("I")
                pyautogui.press("I")
                pyautogui.press("I")

            elif "opn blame view" in query or "blame view" in query or "activate blame view" in query:
                print(f"okay sir activating the blame view pls wait ....")
                pyautogui.press("B")
                pyautogui.press("B")
                pyautogui.press("B")
                pyautogui.press("B")
                pyautogui.press("B")
                pyautogui.press("B")
                pyautogui.press("B")

            elif "create an issue" in query or "there is a issue" in query:
                print("okay sir creting an issue pls what is the issues") 
                pyautogui.press("C")
                pyautogui.press("C")
                pyautogui.press("C")
                pyautogui.press("C")
                pyautogui.press("C")
                pyautogui.press("C")
                command = takeCommand().lower()
                pyautogui.typewrite(command)
                pyautogui.press('enter')

            elif "filter" in query or "edit labels" in query or "okay filters" in query or "okay edit labels" in query:
                print(f"okay sir filterning results pls wait")
                pyautogui.press('L')
                pyautogui.press('L')
                pyautogui.press('L')
                print(f"isit filtered the results sir")

                if "yes" in query:
                    print(f"okay sir is there anything you want sir")
                    print("i will be waiting for nest command")

                else:
                    print(f"okay sir pls wait i will be filtering it again") 
                    pyautogui.press('L')
                    pyautogui.press('L')
                    pyautogui.press('L')

            elif "cancel the move in progress" in query or "cancel it" in query or "cancel the progress" in query:
                print(f" cancelling th emoves in the progress ")
                pyautogui.press('ESC')
                pyautogui.press('ESC')
                pyautogui.press('ESC')
                pyautogui.press('ESC')

            elif "move coloumn to the right" in query or "move to the right column" in query or "right column" in query:
                print(f"moving to the right coloumn pls wait ...")
                pyautogui.press('L')
                pyautogui.press('L')
                pyautogui.press('L')

            elif "move card" in query or "move it" in query:
                print(f"moving the card ..")
                pyautogui.press('k')
                pyautogui.press('k')
                pyautogui.press('k')


            elif "mark as read" in query or "mark it" in query or "read it" in query:
                pyautogui.press('Y')
                pyautogui.press('Y')
                pyautogui.press('Y')
                pyautogui.press('Y')
                print(f"marked it as read sir ")

