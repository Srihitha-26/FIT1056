import os
from menu import Menu

class ModuleHandler:
    """
    The ModuleHandler handles all creation and deletion of modules, and the quizzes within.
    """

    baseFile = os.path.dirname(os.path.realpath('__file__'))
    mcqData = os.path.join(baseFile,'database\mcq_quizzes.txt')
    codeData = os.path.join(baseFile,'database\code_quizzes.txt')
    moduleData = os.path.join(baseFile,'database\modules.txt')


    def create_module(self):
        """
        Allows educator to create modules
        :return: None
        """

        while True:
            moduleInput = input("Please enter module name to be created:\n")

            # Checking if the thing is blank or "cancel" (cancel cannot be the name of the module)
            if moduleInput is not None or moduleInput == '' and moduleInput != 'cancel':
                break
            else:
                print("The module must have a name (that is not 'cancel'), please try again.")

        # Appending the module name into module.txt
        writeFile = open(self.moduleData, "a", encoding="utf8")
        writeFile.write("\n" + moduleInput)
        writeFile.close()

    
    def remove_module(self, moduleKey: str):
        """
        Allows educator to remove unwanted modules and associated quizzes.
        :param moduleKey: A string representing the name of the module to be removed
        :return: None
        """
        # While True block to repeat if they put invalid inputs
        while True:
            # Basically to confirm that they want to delete everything
            confirmation = input("\nThis action will remove all associated quizzes along with the module, are you sure? (Y/N):\n").upper()
            if confirmation == "Y":
                while True:
                    # Re-confiming they do want to delete by making them type the module name
                    confirmation = input("\nPlease type in '" + moduleKey + "' to delete the module or 'cancel' to cancel the operation:\n")
                    if confirmation == moduleKey:
                        confirmed = True
                        break
                    elif confirmation == "cancel":
                        confirmed = False
                        break
                    else:
                        print("Invalid input, please try again.")
                break
            elif confirmation == "N":
                confirmed = False
                break

        if confirmed:

            # Removing from modules.txt
            readFile = open(self.moduleData, "r", encoding="utf8")
            modules = list(readFile)
            readFile.close()

            for line in modules:
                line = line.strip("\n")

            modules.pop(modules.index(moduleKey))
            overwriteFile = open(self.moduleData, "w", encoding="utf8")
            overwriteFile.write("\n".join(modules))
            overwriteFile.close()

            # Removing from code_quizzes.txt
            readFile = open(self.codeData, "r", encoding="utf8")
            lines = list(readFile)
            readFile.close()

            
            modules = []
            questions = []
            initialCodes = []
            answers = []
            codeAnswers = []

            for line in lines:
                (module, question, initialCode, answer, codeAnswer) = line.strip("\n").split(",")
                modules.append(module)
                questions.append(question)
                initialCodes.append(initialCode)
                answers.append(answer)
                codeAnswers.append(codeAnswer)

            for i in range(len(questions)):
                if module[i] == moduleKey:
                    modules.pop(i)
                    questions.pop(i)
                    initialCodes.pop(i)
                    answers.pop(i)
                    codeAnswers.pop(i)
            
            
            overwriteList = []
            for i in range(len(questions)):
                overwriteList.append(f"{modules[i]},{questions[i]},{initialCodes[i]},{answers[i]},{codeAnswers[i]}")
            overwriteFile = open(self.codeData, "w", encoding="utf8")
            overwriteFile.write("\n".join(overwriteList))
            overwriteFile.close()
            
            # Removing from mcq_quizzes.txt
            readFile = open(self.mcqData, "r", encoding="utf8")
            lines = list(readFile)
            readFile.close()

            modules = []
            questions = []
            selections = []
            answers = []

            for line in lines:
                (module, question, selection, answer) = line.strip("\n").split(",")
                modules.append(module)
                questions.append(question)
                selections.append(selection)
                answers.append(answer)

            for i in range(len(questions)):
                if module[i] == moduleKey:
                    modules.pop(i)
                    questions.pop(i)
                    selections.pop(i)
                    answers.pop(i)

            overwriteList = []
            for i in range(len(questions)):
                overwriteList.append(f"{modules[i]},{questions[i]},{selections[i]},{answers[i]}")
            overwriteFile = open(self.mcqData, "w", encoding="utf8")
            overwriteFile.write("\n".join(overwriteList))
            overwriteFile.close()
        
        else:
            print("\nDeletion cancelled, returning to menu...\n")

    def pick_module(self) -> str:
        """
        Allows educator to pick a module to edit from.
        :return: A string representing the module name
        """
        readFile = open(self.moduleData, "r", encoding="utf8")
        modules = list(readFile)
        readFile.close()
        
        for line in modules:
            line = line.strip("\n")

        return Menu.option_select(modules)
    
    def create_mcq_quiz(self, moduleKey: str):
        """
        Allows educator to create quizzes to be done by students.
        :return: None
        """
        while True:
            qnsInput = input("Please enter the question to be asked:\n")

            # Checking qnsInput
            if qnsInput is None or qnsInput == "":
                print("Question must not be empty.")
            elif "," in qnsInput:
                print("All inputs are not able to support commas(,) please retype the question.")
            else:
                break
        
        selectionList = []
        hasSelection = False
        while True:
            if hasSelection:
                print("Type in '--stop--' to submit all selections, or '--remove--' to remove the last selection.")
            selInput = input("Please enter a selection option:\n")
            # Checking selInput
            if selInput is None or selInput == "":
                print("Question must not be empty.")
            elif "," in selInput or ";" in selInput:
                print("Selections are not able to support commas(,) or semicolons(;) please retype the question.")
            elif selInput == '--remove--':
                if len(selectionList > 0):
                    selectionList.pop(-1)
                    if len(selectionList) == 0:
                        hasSelection = False
                else:
                    print("No selections to remove.")
                    
            elif selInput == '--stop--':
                break

            else:
                hasSelection = True
                selectionList.append(selInput)
        
        while True:
            ansInput = input("Please enter the answer to the question:\n")

            # Checking ansInput
            if ansInput is None or ansInput == "":
                print("Answer must not be empty.")
            elif "," in qnsInput:
                print("All inputs are not able to support commas(,) please retype the question.")
            elif ansInput not in selectionList:
                print(f"Selections: {selectionList}")
                print("The answer is not in the selection list, please try again.")
            else:
                break
        
        writeFile = open(self.mcqData, "a", encoding="utf8")
        writeLine = [moduleKey, qnsInput, ";".join(selectionList), ansInput]
        writeFile.write("\n" + ",".join(writeLine))
        writeFile.close()
        print("Question added, returning to menu...\n")
        

    def remove_mcq_quiz(self, moduleKey: str):
        """
        Allows educator to remove unwanted quizzes.
        :return: None
        """
        # Reading and seperating all questions to be given as options for removal
        readFile = open(self.mcqData, "r", encoding="utf8")
        lines = list(readFile)
        readFile.close()

        modules = []
        questions = []
        selections = []
        answers = []

        for line in lines:
            (module, question, selection, answer) = line.strip("\n").split(",")
            modules.append(module)
            questions.append(question)
            selections.append(selections)
            answers.append(answer)
        

        indexList = []
        incrementer = 1
        # Providing all options for question removal
        for i in range(len(questions)):
            if module[i] == moduleKey:
                indexList.append(i)
                print(f"[{incrementer}]\nQuestion: {questions[i]}\nAnswer: {answers[i]}\n\n")
                incrementer += 1
                
        # Prompting for option to remove
        while True:
            try:
                removeInput = int(float(input("Pick an option to remove by number (Pick 0 to return without removing): \n")))
                if removeInput > len(indexList) or removeInput < 0:
                    print("Invalid selection.") 
                elif removeInput == 0:
                    break
                else:
                    removeInput = indexList[removeInput - 1]
                    modules.pop(removeInput)
                    questions.pop(removeInput)
                    selections.pop(removeInput)
                    answers.pop(removeInput)
                    break
            except ValueError:
                print("Invalid option.") 

        # Overwriting list once the options are removed
        overwriteList = []
        for i in range(len(questions)):
            overwriteList.append(f"{modules[i]},{questions[i]},{selections[i]},{answers[i]}")

        overwriteFile = open(self.codeData, "w", encoding="utf8")
        overwriteFile.write("\n".join(overwriteList))
        overwriteFile.close()

    def create_code_quiz(self, moduleKey: str):
        """
        Allows educator to create quizzes to be done by students.
        :return: None
        """

        # While True block to repeat if invalid inputs have been made
        while True:
            qnsInput = input("Please enter the question to be asked:\n")

            # Checking qnsInput
            if qnsInput is None or qnsInput == "":
                print("Question must not be empty.")
            elif "," in qnsInput:
                print("All inputs are not able to support commas(,) please retype the question.")
            else:
                break

        # Test cases and initial code input
        testCases = []
        eduInputs = []

        print("Type in your code to complete the initial code(s).\nType in (without quotes):\n'--delete--' to remove the last line\n'--clear--' to clear all lines\n'--next--' to move on to the next initial code test case\n'--finish--' to add this code to the initial code test case and finish\n")
        while True:
                
                # Prompt for input
                eduInput = input()

                # Checking for special options
                if eduInput == '--delete--':
                    try:
                        eduInputs.pop()
                        print("\033[A\033[A")
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

        # Creating expected return value for each test case
        # If the test case is "a = 1\nb = 2", and the question is "Return the value of a+b" then the ansInput should be 3
        ansInput = []
        for i in range(len(testCases)):
            ansInput.append(input("Type in the returned item for this test case:\n " + "\n".join(testCases[i]).split("~~")))

        # Providing a piece of code that could be used to solve the question
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


        # Appends all question data into file
        writeFile = open(self.codeData, "a", encoding="utf8")
        writeLine = [moduleKey, qnsInput, ";".join(testCases), ";".join(ansInput), "~~".join(codedAns)]
        writeFile.write("\n" + ",".join(writeLine))
        writeFile.close()
        print("Question added, returning to menu.")

    
    def remove_code_quiz(self, moduleKey: str):
        """
        Allows educator to remove any unwanted quizzes
        :return: None
        """
        # Reading and seperating all questions to be given as options for removal
        readFile = open(self.codeData, "r", encoding="utf8")
        lines = list(readFile)
        readFile.close()

        modules = []
        questions = []
        initialCodes = []
        answers = []
        codeAnswers = []

        for line in lines:
            (module, question, initialCode, answer, codeAnswer) = line.strip("\n").split(",")
            modules.append(module)
            questions.append(question)
            initialCodes.append(initialCode)
            answers.append(answer)
            codeAnswers.append(codeAnswer)

        

        indexList = []
        incrementer = 1
        # Providing all options for question removal
        for i in range(len(questions)):
            if module[i] == moduleKey:
                indexList.append(i)
                codedAns = '\n'.join(codeAnswer[i].split('~~'))

                # Basically printing a list of questions and answers in the module
                print(f"[{incrementer}]\nQuestion: {questions[i]}\n\nAnswer:\n {codedAns}\n\n")
                incrementer += 1
                

        # Prompting for option to remove
        while True:
            try:
                removeInput = int(float(input("Pick an option to remove by number (Pick 0 to return without removing): \n")))
                if removeInput > len(indexList) or removeInput < 0:
                    print("Invalid selection.") 
                elif removeInput == 0:
                    break
                else:
                    removeInput = indexList[removeInput - 1]
                    modules.pop(removeInput)
                    questions.pop(removeInput)
                    initialCodes.pop(removeInput)
                    answers.pop(removeInput)
                    codeAnswers.pop(removeInput)
                    break
            except ValueError:
                print("Invalid option.") 

        ### End of selection block ###

        # Overwriting list once the options are removed
        overwriteList = []
        for i in range(len(questions)):
            overwriteList.append(f"{modules[i]},{questions[i]},{initialCodes[i]},{answers[i]},{codeAnswers[i]}")

        overwriteFile = open(self.codeData, "w", encoding="utf8")
        overwriteFile.write("\n".join(overwriteList))
        overwriteFile.close()