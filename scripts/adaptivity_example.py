__author__ = 'mmadaio'
import csv

data_folder = "../data/"

# Global constants defined by curriculum and design teams
MIN_QUESTIONS = 15      # Minimum number of questions given to user, before considering them for mastery
PERCENT_CORRECT_THRESHOLD = 0.60    # IF they have been given the minimum number of questions, correctly answering over this percent suggests they have mastered this question type
MAX_QUESTIONS = 100     # At this number of questions, if they still have not mastered this question type, we provide additional help



# Reads simulated user data file
def readUserData():

    print("Reading user data...")
    output = []
    with open('{0}/mastery_data_example.csv'.format(data_folder)) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            output.append(row)
        csv_file.close()
    print("User data read.\n")
    return output


# Parses user data
def checkMastery(user_data):
    print("Checking user mastery...")

    # Define headers
    headers = user_data[0]
    print("Column headers are:")
    print(headers)

    # Limit array to all rows but the header
    user_data = user_data[1:]

    print("\n\n\nStarting to review users...")

    # Iterate over all the users
    for i in range(len(user_data)):

        # Concatenate Unit ID and Question ID for the question_type
        question_type = user_data[i][1] + "_" + user_data[i][2]


        # Check if number of questions given from that question_type is above minimum number of questions
        if int(user_data[i][3]) > MIN_QUESTIONS and int(user_data[i][3]) < MAX_QUESTIONS:
            print("\nUser_{0}".format(user_data[i][0]),"has been given", MIN_QUESTIONS, "questions of type",question_type)


            # Check if percent correct from that question_type is below the mastery threshold
            if float(user_data[i][5]) < PERCENT_CORRECT_THRESHOLD:
                print("But User_{0}".format(user_data[i][0]),"only has {0} percent correct, and not {1}.".format(user_data[i][5], PERCENT_CORRECT_THRESHOLD))
                print("User_{0}".format(user_data[i][0]),"has NOT mastered question type",question_type)
                print("Continue to give User_{0}".format(user_data[i][0]),"more questions of type",question_type,"\n")


                # If it is above the threshold, they have mastered it
            else:
                print("User_{0}".format(user_data[i][0]),"has answered {0} percent correct.".format(user_data[i][5]))
                print("User_{0}".format(user_data[i][0]),"has mastered question type",question_type,"\n")


        # Check if user needs remedial help on this question type
        elif int(user_data[i][3]) > MAX_QUESTIONS:

            # Check if percent correct from that question_type is below threshold
            if float(user_data[i][5]) < PERCENT_CORRECT_THRESHOLD:
                print("User_{0}".format(user_data[i][0]),"needs more help on question type",question_type)
                print("Give User_{0}".format(user_data[i][0]), "additional examples, hints, or alert their adult supporter for help with",question_type)



# Example to demonstrate item selection logic
def adaptivityExample():
    print("This is an example to demonstrate the adaptive item selection for the core product: \n")
    user_data = readUserData()
    checkMastery(user_data)

if __name__ == "__main__":
    adaptivityExample()
