import os

class FeedbackAction:
    baseFile = os.path.dirname(os.path.realpath('__file__'))
    feedbackData = os.path.join(baseFile,'database\devs.txt')

    def write(self):
        nameInput = input("Please enter your name:\n")
        print("\n")

        while True:
            try:
                ratingInput = int(input("Please rate your experience on the current iteration of the CodeVenture app from\n1 (Very Disatisfactory) - 5 (Very Satisfactory):\n"))
                if ratingInput in range(1,5):
                    print("\n")
                    break
                else:
                    print("\nInvalid input, please try again.")
            except ValueError:
                print("\nInvalid input, please try again.")


        prosInput = input("What did you like most about the current iteration of the CodeVenture app?\n")
        print("\n")
        consInput = input("What do you feel needs improvement most about the current iteration of the CodeVenture app?\n")
        print("\n")

        additionalInput = input("Any additional input for improvement would be appreciated (Optional):\n")
        if additionalInput == None:
            additionalInput = "None"

        feedbackFile = open(self.feedbackData, "a", encoding="utf8")
        writeLine = [nameInput, ratingInput, prosInput, consInput, additionalInput]
        feedbackFile.write("\n" + ",".join(writeLine))
        feedbackFile.close()

    def read(self):
        feedbackFile = open(self.feedbackData, "r", encoding="utf8")
        lines = list(feedbackFile)
        ratings = []

        for line in lines:
            (name, rating, pro, con, additional) = line.strip("\n").split(",")
            print(f"\nName: {name}\nRating: {rating}\nLikes: {pro}\nNeeds Improvement: {con}\nAdditional: {additional}")
            ratings.append(rating)
        if len(ratings > 0):
            print(f"\n\nAverage Ratings: {sum(ratings)/float(len(ratings))}")
        else:
            print("There are currently no ratings.")