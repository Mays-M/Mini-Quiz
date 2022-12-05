class user_add_questions():
    mylist_RightOption=[]
    def adduser_questions(self):
                print("you are allowed to add  only one question")
                user_question=input("Enter your question: ")
                OptionA=input("Enter Option A: ")
                OptionB=input("Enter Option B: ")
                OptionC=input("Enter Option C: ")
                Rightoption=input("Enter the Right OPtion for your question: ")
                self.mylist_RightOption.append(Rightoption)# save the option in the list
                #open the file to read the question added by user
                with open(r"C:\Users\Omistaja\Desktop\JAMK\basics-of-programming\myproject\quiz_questions.txt",'a') as add_questions :
                   add_questions.write("\n")
                   add_questions.write("User questions: ")
                   add_questions.write(user_question)
                   add_questions.write("\n")
                   add_questions.write("A.")
                   add_questions.write(OptionA)
                   add_questions.write("\n")
                   add_questions.write("B.")
                   add_questions.write(OptionB)
                   add_questions.write("\n")
                   add_questions.write("C.")
                   add_questions.write(OptionC)
                   add_questions.write("\n")
                   print("Your question added: ",user_question)
    def getuser_questions(self): # a function to save the Right option for the user question 
        return self.mylist_RightOption
    
        