import os
import pickle
import time
from getpass import getpass
from quiz import *
from User_questions import *
filename="notebook.dat"
note=[]
def quiz():
    t=True
    n=True
    while t:
        print("================WELCOME TO QUIZ MASTER=================")
        print("---------------------------------------------------")
        print("(1) play Quiz")
        print("(2) Add Quiz questions")
        print("(3)Greate an Account ")
        print("(4) Login Panel")
        print("(5)Logout Panel")
        print("(6)See instructions on how to play Quiz")
        print("(7)Exit")
        print("(8)Add Note")
        print("(9)Read Notes")
        select=input("PLEASE! ENTER YOUR CHOICE :")
        if(select=='1'): #check user option1
            play_quiz() #call the function to enter the quize 
            t=True
        elif(select=='2'):
            p=user_add_questions() #call the class inside a attribute
            p.adduser_questions() # call fuction inside the class 

        elif(select=='3'): # option to add a ccount to the user 
            mylist=[]
            print("==========GREATE ACCOUNT==========")
            fname=input("Enter your USERNAME: ")
            PASSWD=getpass() #function to add secuire password
            mylist.append(fname) #add name of the user to list and password
            mylist.append(PASSWD) #add password
            print("Account Created successfuly!")
            t=True
        elif(select=='4'):#log in 
            n=True
            try:
                while n:
                    fname=input("USERNAME: ")
                    PASSWD = getpass()
                    if fname  in mylist and PASSWD in mylist :
                        print("You have successfuly Logged in")
                        n=False
                        
                    else:
                       print("Wrong username or password, please try again")
                       n=True
                    
            except Exception:
                print("No valid Login")
            t=True
        elif(select=='5'): #log out 
            print("You have been logged out successfully")
            t=True
        elif(select=='6'): #instractions
            print("========================INSTRACTIONS==========================")
            print("1.Each round consist of 10 questions ,you must prees A,B,C or a,b,c\nYour final score will be given at the end.")
            print("2.Each questions consists  of 1-point. There's no negative point for wrong answers.")
            print("3.You can create an account from Account creation panel.")
            print("4.You can login using the LOGIN PANEL .Currently,the program can only login and not do anything more.")
            t=True
        elif(select=='7'): #Exit
            print("THANK YOU AND GOOD BYE")
            t=False
        elif(select=='8'): # write note with add the time 
            print("========NOTE PANEL=========")
            noteitem=input("Write a new note: ")
            noteitem=noteitem + ':::'
            noteitem +=time.strftime('%x')
            note.append(noteitem)
            
            t=True
        elif(select=='9'): #read the saved notes
            print("==========READ NOTES==========")
            print("The list has ",len(note),"notes.")
            for i in note:
                print(i)
            t=True

        else:
            t=True

def main():
    quiz()

if __name__ == "__main__":
    main()
        


        

    
