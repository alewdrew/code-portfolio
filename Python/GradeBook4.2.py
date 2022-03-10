import numpy as np

class GradeBook:
    """A class to set up object oriented gradebook program"""
    def __init__(self):
        self.myName = ""
        self.assignList = []
        self.numAssigment = 0
        self.messsage = ""
        self.messageTwo = ""
        self.examList = []
        self.numExam = 0
        self.part = 0
        self.finalexam = 0
        self.assignAvg = 0
        self.examAvg = 0
        self.finalGrade = 0
    #initializing variables to store
    def getInput(self):
        self.myName = input("Please input your name using letters only: ")
        self.numAssignment = int(input("\nPlease input the number of assignments there are: "))
        for num in range(self.numAssignment):
            self.message = int(input(f"\tGrade for assignment {num + 1}: "))
            self.assignList.append(self.message)

        self.numExam = int(input("\nPlease input the number of exams there are: "))
        for value in range(self.numExam):
            self.messageTwo = int(input(f"\tGrade for exam {value + 1}: "))
            self.examList.append(self.messageTwo)

        self.part = int(input("\nPlease input your participation grade: "))
        self.finalExam = int(input("\nPlease enter an estimation for your final exam grade: "))
        self.finalExam = float(self.finalExam)
    def calculateLetterGrade(self):
        self.assignAvg = float(np.mean(self.assignList))
        self.examAvg = float(np.mean(self.examList))
        self.finalGrade = (0.30 * self.examAvg + 0.25 * self.finalExam + 0.25 * self.part + 0.40 * self.assignAvg)

        if self.finalGrade <= 60:
            print("\nYou are failing the course. Please come for help.")
        elif 60 <= self.finalGrade <= 69:
            print("\nYou earned a D, {self.myName.title()}, come for help if you need it.")
        elif 70 <= self.finalGrade <= 79:
            print(f"\nYou earned a C, {self.myName.title()}, perhaps a bit more work?")
        elif 80 <= self.finalGrade <= 89:
            print(f"\nGood work, {self.myName.title()}, you earned a B.")
        elif 90 <= self.finalGrade:
            print(f"\nCongratulations, {self.myName.title()}, you eanred an A!")
         
        print(f"{self.myName.title()}")
        print("(Values are rounded to 2 decimal places.)")
        print(f"\n\tFinal Grade: {np.round(self.finalGrade, 2)}")
        print(f"\n\tAssignment Average: {np.round(self.assignAvg, 2)}")
        print(f"\n\tExam Average: {np.round(self.examAvg, 2)}")
    #function CalculateLetterGrade created, handles the calculations for assignment average, exam average, and the final grade
    #as well as output statements based on if elif conditions
def main():
        #instantiate GradeBook object
    gb = GradeBook()    #invoke methods
    gb.getInput()
    gb.calculateLetterGrade()#invoke the main function/method in the traditional way (this is new information)

if __name__ == "__main__":
    main()

    
