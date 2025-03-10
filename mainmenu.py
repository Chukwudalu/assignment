from transcript import Transcript
from helpers import choose_student_options, get_highest_transcript_id

student_transcript = Transcript()

class MainMenu:
    def __init__(self):
        self.main_menu_options = ['a', 'b', 'c', 'd']
        self.main_menu_selection = None
        self.student_menu_options = ['a', 'b', 'c']
        self.return_to_main_menu = False

    def handle_incorrect_selection(self, menu_selection):
        """
            Checks to see if the user enters a valid menu selection

            Parameters -> menu selection. e.g (a, b, c or d)
        """
        if menu_selection not in self.main_menu_options:
            raise ValueError('Invalid selection. Try again.\n')
        self.main_menu_selection = menu_selection


    def view_all_students(self):
        """
            displays all transcripts

            Parameters -> none
        """
        print(student_transcript.transcript_cache)
    

    def choose_student(self):
        """
            defines logic for selecting a specific student/transcript

            Parameters -> none
        """
        student_menu = True
        transcript_id = input("Please enter the transcript id: ").lower()
        while student_menu:
            transcript_id_valid = False
            for data in student_transcript.transcript_cache:
                if transcript_id == data["transcript_id"]:
                    transcript_id_valid = True
                    break
        
            if transcript_id_valid == True:
                student_data = student_transcript.choose_student(transcript_id)
                student_option = choose_student_options()
                if student_option not in self.student_menu_options:
                    raise ValueError('Invalid selection. Try again.\n')
                if student_option == 'a':
                    print("classes")
                    print("================")
                    for course in student_data["grades"]:
                        print(course["course"])

                elif student_option == 'b':
                    
                    courses_failed = []
                    for course in student_data["grades"]:
                        if int(course["mark"]) < 50:
                            courses_failed.append(course)
                    
                    if courses_failed:
                        print("Not all courses achieved an average of 50 or higher")
                        for course in courses_failed:
                            print(f"{course['course']}: {course['mark']}")
                    else:
                        print("All courses acheived an average of 50 or higher")
                    
                elif student_option == 'c':
                    break

                previous_menu = input("\na. return to previous menu\nb. return to main menu\nMake selection, a or b: ").lower()
                if previous_menu not in ['a', 'b']:
                    raise ValueError("Invalid selection. Returning to main menu.\n")
                if previous_menu == 'a':
                    continue
                elif previous_menu == 'b':
                    break

            else:
                print('Invalid selection. Try again.\n')
                student_menu = False
                

    def add_student(self):
        """
            Defines logic for adding a new student/transcript

            Parameters -> none
            Returns -> none
        """
        first_name = input("Please enter first name: ").capitalize()
        last_name = input("Please enter last name: ").capitalize()
        # A while loop to ensure the user enters at least 2 courses
        grade_input_finish = False
        grades = []
    
        while not grade_input_finish:  

            grade = input("Please enter a course and a mark, seperated by a comma (',') OR enter 'Finish': ")

            if grade.lower() == "finish":
                if len(grades) >= 2:
                    grade_input_finish = True
                    break
                else:
                    print("You need to enter at least two grades")
                    continue
            
            grade = tuple(grade.replace(" ", "").split(','))
            
            if len(grade) != 2:
                print("Invalid entry")
                continue
            
            try:
                temp_course_dict = {'course': grade[0], 'mark': int(grade[1])}
                grades.append(temp_course_dict)
            except:
                raise ValueError('Mark should be of numeric type')
            
        transcript_id = str(get_highest_transcript_id(student_transcript.transcript_cache) + 1)
        
        new_transcript = {
            "transcript_id": transcript_id,
            "firstname": first_name,
            "lastname": last_name,
            "grades": grades
        }

        student_transcript.edit_transcript(new_transcript)


    def edit_student(self):
        """
            Defines logic for adding a editing student/transcript

            Parameters -> none
            Returns -> none
        """
        transcript_id_valid = False
        edit_id = input("Please enter transcript id: ")
        for data in student_transcript.transcript_cache:
            if data["transcript_id"] == edit_id:
                transcript_id_valid = True
                print(data)
                edit_selection = input("What would you like to edit \na. firstname\nb. lastname\nc. grades\nEnter Selection: ").lower()
                if edit_selection not in ['a', 'b', 'c']:
                    raise ValueError('Invalid selection. Try again.\n')
                if edit_selection == 'a':
                    new_firstname = input("Please enter new firstname: ").capitalize()
                    data['firstname'] = new_firstname
                elif edit_selection == 'b':
                    new_lastname = input("Please enter new lastname: ").capitalize()
                    data['lastname'] = new_lastname
                elif edit_selection == 'c':
                    print("See courses: ")
                    for course in data['grades']:
                        print(course['course'])
                    course_edit_selection = input("a. Add course\nb. Delete course\nEnter selection: ").lower()
                    if course_edit_selection not in ['a', 'b']:
                        raise ValueError('Invalid selection. Try again.\n')
                    if course_edit_selection == 'a':
                        course_code = input("Enter course code: ")
                        course_mark = input("Enter course mark: ")
                        if not course_mark.isnumeric():
                            return ValueError("The mark must be numeric. Try again")
                        data['grades'].append({'course': course_code, 'mark': int(course_mark)})
                    elif course_edit_selection == 'b':
                        course_code_selection = input("Enter course code to delete: ").lower()
                        for course in data['grades']:
                            if course['course'].lower() == course_code_selection:
                                data['grades'].remove(course)
                student_transcript.edit_transcript(data)
                break
        
        if transcript_id_valid != True:    
            raise ValueError('Invalid selection. Try again')  


    def handle_menu_selection(self):
        if self.main_menu_selection == 'a':
            self.view_all_students()
        elif self.main_menu_selection == 'b':
            self.choose_student()
        elif self.main_menu_selection == 'c':
            self.add_student()
        elif self.main_menu_selection == 'd':
            self.edit_student()

