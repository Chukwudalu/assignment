

def initial_options():
        """
            This function returns the main menu options
        """
        print("=========== Main Menu ===========")
        print("a. View All \nb. Choose Student\nc. Add Student\nd. Edit Student")
        
        option = input("Please enter option: ")
        
        return option

def choose_student_options():
    print("=========== Student options ===========")
    print("a. List Courses \nb. Check Status\nc. Back to main menu")
    option = input("Please enter option a, b or c : ").lower()
    return option


def exit_menu():
    """
        This function checks if the user wants to exit the main menu.
        returns True if "y" and False if "n"
    """
    
    response = input("Return to main menu? Select Y/N : ").lower()
    if response not in ['y', 'n']:
        print("Invalid selection. Program closing")
        return True
    return response.lower() == "n"


def check_course_pass(value):
    return value > 50

def get_highest_transcript_id(transcripts):
    highest_id = 0
    for transcript in transcripts:
        if int(transcript["transcript_id"]) > highest_id:
            highest_id = int(transcript["transcript_id"])
    return highest_id