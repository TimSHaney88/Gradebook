from Student import Student
'''class Student
    def _init_(self, score[], name, id):
        self._score = score
        self._name = name
        self._id = id

    defGetScores(self):'''
stud1=Student("Bob",898)
lst = []      #should be gone
average = 0
summ = 0
number = '1'
choice = '1'
count = 1
length = 0
number1 =1
score = '0'
score1= 1
menu = True

while menu == True:
    count += 1
    print ("Gradebook")
    print ("1. view grades")
    print ("2. add more scores")
    print ("3. percent in class")
    print ("4. exit")
    choice = (input("Choose a selection between 1 - 4: "))
    if choice < '1' or choice >= '5':
        print("Invalid input.  Please enter a number between 1 and 4. ")
        continue

    if choice == '1':
        #stud1.getGrade()
        length = len(lst)
        if length == 0:
            length = len(lst)
            print("No data")
        else:

            print(lst)
            print(summ)
            length = len(lst)
            print(length)
            average = summ//length
            print(average)

            if average >= 90:
                print("Student grade is A ")

            elif average >= 80:
                print("Student grade is B ")

            elif average >= 70:
                print("Student grade is C ")

            elif average >= 60:
                print("Student grade is D ")

            else:
                print("The grade is an F ")


    elif choice == '2':
        scoresNumMenu = True
        while scoresNumMenu == True:
            number = (input("How many scores?: "))
            if number.isdigit():
                print(number.isdigit())
                number1 = int(number)

                if number1 >= 1 and number1 <= 20:
                    number1 = int(number)
                    scoresNumMenu = False

                else:
                    print("Please enter a number between 1 and 20")

            else:
                print("letter input. Please enter a number between 1 and 20")


        scoresValMenu = True
        while scoresValMenu == True:
            for i in range(number1):
                score = (input("Enter a score: "))
                if score.isdigit():
                    score1 = int(score)
                    if score1 >= 0 and score1 <= 105:
                        lst.append(score1)
                        summ += score1
                        print(lst)

                    else:
                        print("Please enter a number between 0 and 1020:")
                        scoreCase = True
                        while scoreCase == True:
                            score = (input("Enter a score: "))
                            if score.isdigit():
                                score1 = int(score)
                                if score1 >= 0 and score1 <= 105:
                                    lst.append(score1)
                                    summ += score1
                                    print(lst)
                                    scoreCase = False
                                else:
                                    print("Invalid Input")
                            else:
                                print("Invalid Input")


                else:
                    print("letter.  Please enter a number between 0 and 105:")
                    scoreCase1 = True
                    while scoreCase1 == True:
                        score = (input("Enter a score: "))
                        if score.isdigit():
                            score1 = int(score)
                            if score1 >= 0 and score1 <= 105:
                                lst.append(score1)
                                summ += score1
                                print(lst)
                                scoreCase1 = False
                            else:
                                print("Invalid Input")
                        else:
                            print("Invalid Input")

            scoresValMenu = False

    elif choice == '3':

        #stud1.getAverage()
        length = len(lst)
        if length == 0:
            print("No data")
        else:
            length = len(lst)
            average = summ // length
            print("Average is ", average, "%")

    elif choice == '4':

        print("Goodbye!")
        menu = False




def main():
    stud1=Student("Bob",898)
    print("Name:", stud1.getName())
    print("hah")
main()








