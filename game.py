"""
FIT1056 Software Development Phase
Student name: Yong Wen Jian
Student ID: 33561583
Group: MA_FRI_1600_G2
"""


import os

class Game:
    baseFile = os.path.dirname(os.path.realpath('__file__'))
    quizFile = os.path.join(baseFile,'database\quizzes.txt')

    def attemptQuizzes(self):
        readFile = open(self.quizFile, "r", encoding="utf8")
        lines = list(readFile)
        questions = []
        initialCodes = []
        answers = []
        codeAnswers = []

        for line in lines:
            (question, initialCode, answer, codeAnswer) = line.split(",")
            questions.append(question)
            initialCodes.append(initialCode)
            answers.append(answer)
            codeAnswers.append(codeAnswer)

        for i in range(len(questions)):
            while True:
                print(questions[i])
                givenCode = initialCodes[i].strip().split(';')
                for k in range(len(givenCode)):
                    givenCode[k] = "\n".join(givenCode[k].split('~~'))
                print('Initial Code:\n' + givenCode[0])
                print("Type in your code to complete the question.\nType in (without quotes):\n'--delete--' to remove the last line\n'--clear--' to clear all lines\n'--finish--' to submit the code\n'--stop--' to see the answer\n")
                userInputs = []
                submitted = False
                while True:
                    userInput = input()
                    if userInput == '--delete--':
                        try:
                            userInputs.pop()
                            print("\033[A\033[A") # Clears a line
                            print("\033[A\033[A") # Clears a line
                        except IndexError:
                            print("No previous code has been typed.")

                    elif userInput == '--clear--':
                        userInputs = []
                        print("------------------------------Restart Code From Here------------------------------\n")

                    elif userInput == '--finish--':
                        submitted = True
                        break

                    elif userInput == '--stop--':
                        break

                    else:
                        userInputs.append(userInput)
                
                if submitted:
                    passed = True
                    for j in range(len(givenCode)):
                        try:
                            codeList = [givenCode] + userInputs
                            code = "\n".join(codeList)
                            if str(exec(code)) != answers[j]: # exec method executes methods from string
                                passed = False
                                print("Code is incorrect.")
                                break
                        except:
                            passed = False
                            print("Code is incorrect.")
                            break
                    if passed:
                        print("Code passed!")
                        break
                
                else:
                    print("The coded answer is:\n" + "\n".join(codeAnswers[i].split("~~")))
                    break

        readFile.close()
        print("All questions finished, returning to menu.")
    
    def create_quiz(self):
        while True:
            qnsInput = input("Please enter the question to be asked:\n")
            if qnsInput == "":
                print("Question must not be empty.")
            elif "," in qnsInput:
                print("All inputs are not able to support commas(,) please retype the question.")
            else:
                break
        
        testCases = []
        eduInputs = []
        print("Type in your code to complete the initial code(s).\nType in (without quotes):\n'--delete--' to remove the last line\n'--clear--' to clear all lines\n'--next--' to move on to the next initial code test case\n'--finish--' to add this code to the initial code test case and finish\n")
        while True:
                eduInput = input()
                if eduInput == '--delete--':
                    try:
                        eduInputs.pop()
                        print("\033[A\033[A") # Clears a line
                    except IndexError:
                        print("No previous code has been typed.")

                elif eduInput == '--clear--':
                    eduInputs = []
                    print("------------------------------Restart Code From Here------------------------------\n")

                elif eduInput == '--next--':
                    testCases.append("~~".join(eduInputs))
                    eduInputs = []
                    print("------------------------------Code Next Test Case From Here------------------------------\n")

                elif eduInput == '--finish--':
                    testCases.append("~~".join(eduInputs))
                    break

                else:
                    eduInputs.append(eduInput)

        ansInput = []
        for i in range(len(testCases)):
            ansInput.append(input("Type in the returned item for this test case:\n " + "\n".join(testCases[i]).split("~~")))

        codedAns = []
        print("Type in your code to complete the initial code(s).\nType in (without quotes):\n'--delete--' to remove the last line\n'--clear--' to clear all lines\n'--finish--' to set the coded answer\n")
        while True:
                codedInput = input()
                if codedInput == '--delete--':
                    try:
                        codedAns.pop()
                        print("\033[A\033[A") # Clears a line
                        print("\033[A\033[A")
                    except IndexError:
                        print("No previous code has been typed.")

                elif codedInput == '--clear--':
                    codedAns = []
                    print("------------------------------Restart Code From Here------------------------------\n")

                elif codedInput == '--finish--':
                    break

                else:
                    codedAns.append(codedInput)

        writeFile = open(self.quizFile, "a", encoding="utf8")
        writeLine = [qnsInput, ";".join(testCases), ";".join(ansInput), "~~".join(codedAns)]
        writeFile.write("\n" + ",".join(writeLine))
        writeFile.close()
        print("Question added, returning to menu.")

    def remove_quiz(self):
        readFile = open(self.quizFile, "r", encoding="utf8")
        lines = list(readFile)
        readFile.close()

        questions = []
        initialCodes = []
        answers = []
        codeAnswers = []

        for line in lines:
            (question, initialCode, answer, codeAnswer) = line.strip("\n").split(",")
            questions.append[question]
            initialCodes.append[initialCode]
            answers.append[answer]
            codeAnswers.append[codeAnswer]

        for i in range(len(questions)):
            codedAns = '\n'.join(codeAnswer[i].split('~~'))
            print(f"[{i+1}]\nQuestion: {questions[i]}\nAnswer: {codedAns}\n\n")
        
        while True:
            try:
                removeInput = int(float(input("Pick an option to remove by number (Pick 0 to return without removing): \n")))
                if removeInput > len(questions) or removeInput < 0:
                    print("Invalid selection.")
                elif removeInput == 0:
                    break
                else:
                    questions.pop(removeInput-1)
                    initialCodes.pop(removeInput-1)
                    answers.pop(removeInput-1)
                    codeAnswers.pop(removeInput-1)
                    break
            except ValueError:
                print("Invalid option.")

        overwriteList = []
        for i in range(len(questions)):
            overwriteList.append[f"{questions[i]},{initialCodes[i]},{answers[i]},{codeAnswers[i]}"]

        overwriteFile = open(self.quizFile, "w", encoding="utf8")
        overwriteFile.write("\n".join(overwriteList))