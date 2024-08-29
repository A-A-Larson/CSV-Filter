import csv


def main():
    file_name = ""

    def filter_by_age(file_name_arg):
        with open(file_name_arg, "r") as file:
            # Converting a csv to dict
            csv_reader = csv.DictReader(file)
            min_age = int(input("Enter a minimum age: "))
            max_age = int(input("Enter a maximum age: "))
            # each row now is a dictionary ,and you can access data with keys
            for row in csv_reader:
                age = int(row["age"])
                if age <= max_age or age >= min_age:
                    print(age)

    retry_file = True
    while retry_file:
        file_name = input('Enter filename or "Q" to exit: ')
        try:
            file_check = open(file_name, "r")
            file_check.close()
            retry_file = False
        except FileNotFoundError:
            print("Filename not found, try again.")
        if file_name == "Q":
            exit()
        else:
            retry_menu = True
            while retry_menu:
                choice = input("Choose a filter: \n"
                               "1. Age \n"
                               "2. City \n"
                               "3. Last name \n"
                               "4. First name \n"
                               "5. ID \n"
                               "Q to quit: ")
                match choice:
                    case "1":
                        filter_by_age(file_name)
                        break
                    case "2":
                        print("option 2")
                        break
                    case "3":
                        print("option 3")
                        break
                    case "4":
                        print("option 4")
                        break
                    case "5":
                        print("option 5")
                        break
                    case "Q":
                        exit()


if __name__ == "__main__":
    main()
