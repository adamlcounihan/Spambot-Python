import pyautogui, time


def start():
    choice = input("Paste from the text-file or clipboard (t/c)")
    choice = choice.casefold()
    

    #spam paste from text file
    if choice == "t":
        print("")
        confirm = input("Are you sure? (y/n)")
        confirm = confirm.casefold()
        
        if confirm == "y":
            time.sleep(5)
            file = open("spambot.txt", 'r')
            for word in file:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
            file.close()
        else:
            start()


    #spam paste from clipboard
    elif choice == "c":
        print("")
        confirm = input("Are you sure? (y/n)")
        confirm = confirm.casefold()
        
        if confirm == "y" :
            print_num = int(input("How many times should the clipboard be printed?"))
            print("Time delay of 8 seconds.....")
            time.sleep(8)
            for n in range(print_num):
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.25)
                pyautogui.press('enter')
        else:
            start()


    #invalid input
    else:
        print("Invalid option")
        start()



start()
