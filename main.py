import student



if __name__ == "__main__":
    while True:
        student.Student.add_student()
        more = input("Do you want to add another student? (y/n): ")
        if more.lower() != "y":
            break
