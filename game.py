"""
FIT1056 Software Development Phase
Student name: Yong Wen Jian
Student ID: 33561583
Group: MA_FRI_1600_G2
"""


import os
from menu import Menu

class Game:
    """
    The Game class represents the CodeVenture quizzes to be made, deleted, or played.
    """
    
    baseFile = os.path.dirname(os.path.realpath('__file__'))
    """
    A string representing the directory to the current file
    """
    
    codeFile = os.path.join(baseFile,'database\code_quizzes.txt')
    """
    A string representing the coded quizzes data from the database folder
    """

    mcqFile = os.path.join(baseFile,'database\mcq_quizzes.txt')
    """
    A string representing the mcq quizzes data from the database folder
    """

    moduleFile = os.path.join(baseFile, 'database\modules.txt')
    """
    A string representing the modules data from the database folder
    """
    
    def pick_module(self) -> str:
        """
        Allows educator to pick a module to edit from.
        :return: A string representing the module name
        """
        readFile = open(self.moduleFile, "r", encoding="utf8")
        modules = list(readFile)
        readFile.close()
        
        for line in modules:
            line = line.strip("\n")

        return Menu.option_select(modules)
    

    def attempt_mcq_quizzes(self, key: str) -> list[int]:
        """
        The function for any students to attempt the quizzes found within the mcq quiz file data.
        :param key: Key for the module to be played
        :return: A list of integers representing the total questions and correct answers of the quiz.
        """
        readFile = open(self.mcqFile, "r", encoding="utf8")
        lines = list(readFile)
        readFile.close()
        keys = []
        questions = []
        selections = []
        answers = []

        for line in lines:
            (moduleKey, question, selection, answer) = line.strip("\n").split(",")
            keys.append(moduleKey)
            questions.append(question)
            selections.append(selection)
            answers.append(answer)

        cleared = 0
        total = 0

        incrementer = 0
        for i in range(len(questions)):
            if key == keys[i]:
                allOptions = selections[i].split(";")

                incrementer += 1
                print(f"\n================================ Question {incrementer} ================================")
                print(questions[i])
                print("================================ Select One ================================")
                ch = 'A' # Note: ord('A') is 65
                for options in allOptions:
                    print(f"{ch}. {options}")
                    ch = chr(ord(ch) + 1)
                while True:
                    chosenInput = input("\n").upper()
                    try:
                        index = ord(chosenInput) - 65
                        if index < 0 or (index) > (len(allOptions) - 1):
                            print("Input is invalid, please select a valid option.")
                        else:
                            break
                    except TypeError:
                        print("Input is invalid, please select a valid option.")
                
                correct = answers[i] == allOptions[index]
                if correct:
                    print("\nAnswer is correct! Moving to the next question...")
                    cleared += 1
                    total += 1
                else:
                    print(f"\nAnswer is incorrect.\nCorrect answer: {answers[i]}\nMoving to next question...")
                    total += 1

        return [total, cleared]

        
    def attempt_code_quizzes(self, key: str) -> list[int]:
        """
        The function for any students to attempt the quizzes found within the coding quiz file data.
        :param key: Key for the module to be played
        :return: A list of integers representing the total questions and correct answers of the quiz
        """
        # Reading quiz file, seperating each section into their own list
        readFile = open(self.codeFile, "r", encoding="utf8")
        lines = list(readFile)
        readFile.close()
        keys = []
        questions = []
        initialCodes = []
        answers = []
        codeAnswers = []

        for line in lines:
            (moduleKey, question, initialCode, answer, codeAnswer) = line.split(",")
            keys.append(moduleKey)
            questions.append(question)
            initialCodes.append(initialCode)
            answers.append(answer)
            codeAnswers.append(codeAnswer)

        cleared = 0
        total = 0

        incrementer = 0
        # Prompting each question one by one
        for i in range(len(questions)):
            if key == keys[i]:
                incrementer += 1
                while True:
                    # Question prompt
                    print(f"\n================================ Question {incrementer} ================================")
                    print("\n" + questions[i]) 

                    # Provide one initial code to work on
                    givenCode = initialCodes[i].strip().split(';')
                    givenAnswers = answers[i].strip().split(';')
                    for k in range(len(givenCode)):
                        givenCode[k] = "\n    ".join(givenCode[k].split('~~'))
                    print('===== Initial Code =====\n    ' + givenCode[0])

                    # Prompting user for input
                    print("\n===== Type in your code to complete the question. =====\nType (without quotes):\n'--delete--' to remove the last line\n'--clear--' to clear all lines\n'--finish--' to submit the code\n'--stop--' to see the answer\n=======================================================\n")
                    userInputs = []
                    submitted = False
                    while True:
                        userInput = input()

                        # Checking for special options
                        if userInput == '--delete--':
                            try:
                                userInputs.pop()
                                print("\033[A\033[A") # Clears a line
                                print("\033[A\033[A")
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
                    
                    # Check if user has given up
                    if submitted:
                        passed = True
                        
                        print("\n\n====== Going through test cases =====")
                        # Check answers using user inputted code for each test case
                        for j in range(len(givenCode)):
                            print(f"\nTest {j + 1}")
                            try:
                                codeList = [givenCode[j]] + userInputs
                                code = "\n    ".join(codeList)
                                code = "def newFunc():\n    " + code + "\nresult = newFunc()"
                                local = locals()
                                exec(code, globals(), local)
                                result = local["result"]
                                print(f"Result: {result}")
                                print(f"Answer: {givenAnswers[j]}")
                                if str(result) != givenAnswers[j]: # exec method executes methods from string
                                    passed = False
                                    print("\nCode is incorrect; Test cases unmatched.")
                                    break
                            except:
                                passed = False
                                print("\nCode is incorrect; Error during execution of code.")
                                break
                        if passed:
                            print("\nCode passed!")
                            cleared += 1
                            total += 1
                            break
                    
                    # Executes when student gives up
                    else:
                        print("The coded answer is:\n" + "\n".join(codeAnswers[i].split("~~")))
                        total += 1
                        break
        
        # Executes after all questions have been done 
        print("All questions finished, returning to menu.\n")
        return [total, cleared]
    
    