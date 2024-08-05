class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)
        print(f"Added grade {grade} for {subject}.")

    def view_grades(self):
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

    def calculate_average(self):
        for subject, grades in self.grades.items():
            average = sum(grades) / len(grades)
            print(f"Average grade for {subject}: {average:.2f}")

    def calculate_overall_average(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        if total_grades:
            overall_average = sum(total_grades) / len(total_grades)
            print(f"Overall average grade: {overall_average:.2f}")
        else:
            print("No grades available to calculate overall average.")

def main():
    tracker = StudentGradeTracker()
    while True:
        print("\nStudent Grade Tracker")
        print("1. Add grade")
        print("2. View grades")
        print("3. Calculate average per subject")
        print("4. Calculate overall average")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            subject = input("Enter the subject: ")
            grade = float(input("Enter the grade: "))
            tracker.add_grade(subject, grade)
        elif choice == '2':
            tracker.view_grades()
        elif choice == '3':
            tracker.calculate_average()
        elif choice == '4':
            tracker.calculate_overall_average()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
