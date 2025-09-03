
# Md Mehedi Alam
# CS 500
# Program that creates a dictionary containing course numbers and the room numbers of the rooms where 
# the courses meet, create a dictionary containing course numbers and the names of the instructors 
# that teach each course, create a dictionary containing course numbers and the meeting times of each 
# course, let the user enter a course number and then it should display the course's room number, 
# instructor, and meeting time.




"""
Course Information Management System
This program creates dictionaries for course information and allows users to look up course details.
"""

def main():
    # Dictionary containing course numbers and room numbers
    course_rooms = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }
    
    # Dictionary containing course numbers and instructor names
    course_instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }
    
    # Dictionary containing course numbers and meeting times
    course_times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }
    
    print("Course Information Management System")
    print("=" * 40)
    
    # Display all available courses
    print("\nAvailable courses:")
    for course in course_rooms.keys():
        print(f"  {course}")
    
    print("\n" + "=" * 40)
    
    # Main program loop
    while True:
        # Get course number from user
        course_number = input("\nEnter a course number (or 'quit' to exit): ").upper()
        
        # Check if user wants to quit
        if course_number == 'QUIT':
            print("Thank you for using the Course Information System!")
            break
        
        # Check if course exists
        if course_number in course_rooms:
            print(f"\nCourse Information for {course_number}:")
            print(f"  Room Number: {course_rooms[course_number]}")
            print(f"  Instructor: {course_instructors[course_number]}")
            print(f"  Meeting Time: {course_times[course_number]}")
        else:
            print(f"Error: Course {course_number} not found.")
            print("Please enter a valid course number from the list above.")

if __name__ == "__main__":
    main()




