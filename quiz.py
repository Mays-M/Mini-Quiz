from User_questions import *
def play_quiz():  
    mylist_user_question=[] # empty list to add the user  question
    count=0
    print("======================Welcome TO Quiz=======================",end="\n")
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question1:
        q1=question1.readlines()[0:4] #read specific lines fromthe file
        print(*q1)
        answer1=input("enter your choice : ") # to select the option 
        if answer1=='A' or answer1=='a' :# compare the option
            count+=1   #increase the count 1
    #readquestion2
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question2:
        q2=question2.readlines()[4:9]
        print(*q2)
        answer2=input("enter your choice : ")
        if answer2=='B'or answer2== 'b'  :
            count+=1
    #read question3
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question3:
        q3=question3.readlines()[9:14]
        print(*q3)   
        answer3=input("enter your choice : ")
        if answer3=='C' or answer3=='c' :
            count+=1
    #read question4
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question4:
        q4=question4.readlines()[14:19]
        print(*q4)
        answer4=input("enter your choice : ")
        if answer4=='C' or answer4=='c' :
           count+=1
    #read question5
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question5:
        q5=question5.readlines()[19:24]
        print(*q5)
        answer5=input("enter your choice : ")
        if answer5=='B' or answer5=='b' :
            count+=1
    #read question6
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question6:
        q6=question6.readlines()[24:29]
        print(*q6)    
        answer6=input("enter your choice : ")
        if answer6=='A'or answer6=='a' :
           count+=1
    #read question7
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question7:
        q7=question7.readlines()[29:34]
        print(*q7)   
        answer7=input("enter your choice : ")
        if answer7=='B' or answer7=='b' :
            count+=1
    #read question8
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question8:
        q8=question8.readlines()[34:39]
        print(*q8)   
        answer8=input("enter your choice : ")
        if answer8=='C' or answer8=='c' :
           count+=1
    #read question9
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question9:
        q9=question9.readlines()[39:44]
        print(*q9)   
        answer9=input("enter your choice : ")
        if answer9=='A' or answer9=='a' :
           count+=1
    #read question10
    with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as question10:
        q10=question10.readlines()[44:49]
        print(*q10)    
        answer10=input("enter your choice : ")
        if answer10=='C' or answer10=='c' :
            count+=1
        with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'r') as user_qus:
            newQ=user_qus.readlines()[49:]
            print(*newQ)
            if (len(newQ)>0):
               new=user_qus.readlines()[49:]
               option_user_question=input("enter your choice : ")
               mylist_user_question.append(option_user_question) #add user option for the question add by the user to a list
               question_user=user_add_questions()  #fetch the fuction of the class that content a list of the Right option
               fetch_user_question=question_user.getuser_questions()
               if mylist_user_question == fetch_user_question: #compare the items inside the list of user input and the option is given
                   count+=1
            else:
                pass
 
        f=True
        fname=input("Enter your Name : ") #input the name of the user
        while f:
            age=input("Enter your age :") #age with condition of nummbers only
            try:
               age2=int(age)
               f=False
            except Exception:
                print("please add number to age column ")
                f=True
    
        print("Your Total points are :", count,"/10")   

        print("")