import random
import string
from datetime import datetime
import os
from colorama import init
import keyboard

main_frag = True

user_list = {111111: {"fullname": "daniel",
                      "national id": "1273953193",
                      "birthday": "1/5/1382",
                      "address": "isfahan",
                      "Registration Date": "2023-6-5",
                      "Registration Time": "19:44:14"
                      }, 222222: {"fullname": "ali",
                                  "national id": "1111111111",
                                  "birthday": "1/5/1382",
                                  "address": "isfahan",
                                  "Registration Date": "2023-6-5",
                                  "Registration Time": "19:44:14"
                                  }, 333333: {"fullname": "reza",
                                              "national id": "2222222222",
                                              "birthday": "1/5/1382",
                                              "address": "isfahan",
                                              "Registration Date": "2023-6-5",
                                              "Registration Time": "19:44:14"
                                              }}
book_list = {1111111: {"name book": "riazi",
                       "publisher": "ali",
                       "year": "1993",
                       "filed": "riazi"
                       }, 2222222: {"name book": "physics",
                                    "publisher": "reza",
                                    "year": "1993",
                                    "filed": "physics"
                                    }, 3333333: {"name book": "operating system",
                                                 "publisher": "daniel",
                                                 "year": "1993",
                                                 "filed": "operating system"
                                                 }}
borrowed_book_list = {}
list_register_user_id = [111111, 222222, 333333]
list_book_id = [1111111, 2222222, 3333333]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def id_generator(first_num, last_num, list_checker):
    while True:
        p_id = random.randint(first_num, last_num)
        if p_id in list_checker:
            continue
        else:
            list_checker.append(p_id)
            return p_id


def remover(name_in_str, list_for_check):
    while True:
        input_remove_register_id = int(input(f"Enter your register ID for remove {name_in_str} : "))
        if input_remove_register_id in list_for_check:
            print(f"Information for this ID {input_remove_register_id} :")
            show_info_for_remove = book_list[input_remove_register_id]
            for key, value in show_info_for_remove.items():
                print(f"{key} ------> {value}")

            pass_remove_register_id = input("Are you sure (y/n) ? :")
            if pass_remove_register_id == "y":
                del list_for_check[input_remove_register_id]
                print("success your order. ")
                break
            else:
                print("canceled ! ")
                break
        else:
            print(f"The {input_remove_register_id} Register ID not found !!!")


def show_generator(list, name):
    while True:
        for kay, value in list.items():
            print(f"{name} Register ID : {kay}")
            for x, y in value.items():
                print(f"{x}  ------>  {y}")
            print('=' * 20)
        exit_key = input("Press Enter key to exit...")
        if exit_key == "":
            clear_terminal()
            break
        else:
            break


def show_generator_ones(list, id):
    while True:
        print(f"Register ID: {id}")
        for x, y in list.items():
            print(f"{x}  ------>  {y}")
        print('=' * 20)

        exit_key = input("Press Enter key to exit...")
        if exit_key == "":
            clear_terminal()
            break
        else:
            break


def user():
    user_frag = True

    def get_name():
        frag_name = True
        while frag_name:

            input_name = input("Enter the full name : ")
            for i in range(len(input_name)):
                if input_name[i] in string.digits:
                    print("Incorrect name format . please enter alphabet.")
                    break
            else:
                return input_name
                frag_name = False

    def national_id_checker(def_input_national_id):
        for key, value in user_list.items():

            if def_input_national_id == value["national id"]:
                print("National ID is duplicated !!!")
                return def_input_national_id
            # else:
            #     return def_input_national_id

    def get_national_id():
        frag_id = True
        while frag_id:
            input_national_id = input("Enter your National ID : ")
            for i in range(len(input_national_id)):
                if input_national_id[i] in string.ascii_letters or not len(input_national_id) == 10:
                    print("incorrect National ID, Please Enter the number ")
                    break
                elif input_national_id == national_id_checker(input_national_id):
                    break
                else:
                    return input_national_id
                    frag_id = False

    def get_birthday():
        while True:
            try:
                date = input("Enter your birthday (dd/mm/yyyy): ")
                day, month, year = date.split('/')

            except:
                print("this format is invalid !!!! ")
                continue

            if not day.isdigit() or not month.isdigit() or not year.isdigit():
                print("Input must be number. Please try again.")
                continue

            day = int(day)
            month = int(month)
            year = int(year)

            if not (1 <= day <= 31) or not (1 <= month <= 12) or not (1300 <= year <= 1500):
                print("The date entered incorrect !!!")
                continue
            break

        return day, month, year

    def get_address():
        input_address = input("Enter your Address : ")
        return input_address

    def add_user():
        p_id = id_generator(100000, 999999, list_register_user_id)
        input_name = get_name()
        input_national_id = get_national_id()
        day, month, year = get_birthday()
        input_address = get_address()
        registration_time = datetime.now()

        user_info_list = {
            "fullname": input_name,
            "national id": input_national_id,
            "birthday": f"{day}/{month}/{year}",
            "address": input_address,
            "Registration Date": f"{registration_time.year}-{registration_time.month}-{registration_time.day}",
            "Registration Time": f"{registration_time.hour}:{registration_time.minute}:{registration_time.second}"
        }
        user_list[p_id] = user_info_list
        print("\n")
        show_generator_ones(user_list[p_id], p_id)

    def edit_user_info():
        edit_info_while = True
        while edit_info_while:

            register_id = input("Enter the Register ID of the user account you want to edit (or Enter for Back) : ")
            if register_id.isdigit():
                register_id = int(register_id)
                if register_id in user_list:
                    print("Member found. Here are the current information:")
                    current_info = user_list[register_id]
                    print("Fullname: ", current_info["fullname"])
                    print("National ID: ", current_info["national id"])
                    print("Birthday: ", current_info["birthday"])
                    print("Address: ", current_info["address"])

                    print("\nEnter the new information (leave empty for no change):")
                    input_name = input(f"New Full name (current : {current_info['fullname']}): ") or current_info[
                        "fullname"]
                    if input_name:
                        user_list[register_id]["fullname"] = input_name

                    while True:
                        input_national_id = input(f'New National ID (current : {current_info["national id"]}) : ') or \
                                            current_info["national id"]

                        if input_national_id.isdigit() and len(input_national_id) == 10:
                            user_list[register_id]["national id"] = input_national_id
                            break
                        else:
                            print("false national id !!!")

                    while True:
                        input_birthday = input(
                            f"New birthday (dd/mm/yyyy) (current : {current_info['birthday']}) : ") or current_info[
                                             'birthday']
                        try:
                            day, month, year = input_birthday.split('/')
                        except:
                            print("invalid format try again!")
                            continue
                        if day.isdigit() and month.isdigit() and year.isdigit():
                            day = int(day)
                            month = int(month)
                            year = int(year)
                        else:
                            print("incorrect birthday!!!")
                            continue
                        if 1 <= day <= 31 and 1 <= month <= 12 and 1300 <= year <= 1500:
                            user_list[register_id]["birthday"] = input_birthday
                            break
                        else:
                            print("incorrect birthday!!!")
                            continue

                    input_address = input(f"New address (current : {current_info['address']}) : ") or current_info[
                        'address']
                    if input_address:
                        user_list[register_id]["address"] = input_address

                    print("Information updated successfully.")
                else:
                    print("Member not found.")
            else:
                break

    while user_frag:
        request_input_user_layer1 = input(
            "What can you do ? \n\n1) Add member\n2) Edit info\n3) Show accounts\n4) Remove account\n0) "
            "Back\n\nEnter option number: ")
        clear_terminal()

        if request_input_user_layer1 == "1":
            add_user()
        elif request_input_user_layer1 == "2":
            edit_user_info()
        elif request_input_user_layer1 == "":
            pass
        elif request_input_user_layer1 == "3":
            show_generator(user_list, "user")
        elif request_input_user_layer1 == "4":
            remover("user account", user_list)
        elif request_input_user_layer1 == "0":
            user_frag = False


def library():
    library_frag = True

    def get_name_book():
        frag_get_name_book = True
        while frag_get_name_book:

            input_get_name_book = input("Enter the book name : ")
            for i in range(len(input_get_name_book)):
                if input_get_name_book[i] in string.digits:
                    print("Incorrect name format . please enter alphabet.")
                    break
            else:
                return input_get_name_book
                frag_get_name_book = False

    def get_publisher_book():
        frag_get_publisher_book = True
        while frag_get_publisher_book:

            input_get_publisher_book = input("Enter the publisher book : ")
            for i in range(len(input_get_publisher_book)):
                if input_get_publisher_book[i] in string.digits:
                    print("Incorrect name format . please enter alphabet.")
                    break
            else:
                return input_get_publisher_book
                frag_get_publisher_book = False

    def get_book_year():
        frag_get_book_year = True
        while frag_get_book_year:

            input_get_book_year = input("Enter the book year : ")
            for i in range(len(input_get_book_year)):
                if input_get_book_year[i] in string.ascii_letters:
                    print("Incorrect year format . please enter Number.")
                    break
            else:
                return input_get_book_year
                frag_get_book_year = False

    def get_filed():
        frag_filed = True
        while frag_filed:

            input_filed = input("Enter the book filed : ")
            for i in range(len(input_filed)):
                if input_filed[i] in string.digits:
                    print("Incorrect name format . please enter alphabet.")
                    break
            else:
                return input_filed
                frag_filed = False

    def add_book():
        book_id = id_generator(1000000, 9999999, list_book_id)
        input_name_book = get_name_book()
        input_publisher_book = get_publisher_book()
        input_book_year = get_book_year()
        input_filed = get_filed()
        book_info_list = {"name book": input_name_book,
                          "publisher": input_publisher_book,
                          "year": input_book_year,
                          "filed": input_filed
                          }
        book_list[book_id] = book_info_list
        show_generator_ones(book_list[book_id], book_id)

    def edit_book_info():
        edit_book_info_while = True
        while edit_book_info_while:

            register_id = input("Enter the Register ID of the book you want to edit (or Enter for Back) : ")
            if register_id.isdigit():
                register_id = int(register_id)
                if register_id in book_list:
                    print("Book found. Here are the current information:")
                    current_info = book_list[register_id]
                    print("name book: ", current_info["name book"])
                    print("publisher: ", current_info["publisher"])
                    print("year: ", current_info["year"])
                    print("filed: ", current_info["filed"])

                    # change name book
                    print("\nEnter the new information :")
                    input_book_name = input(f"New name book (current : {current_info['name book']}): ") or current_info[
                        "name book"]
                    book_list[register_id]["name book"] = input_book_name
                    print("Information updated successfully.")

                    # change publisher
                    while True:
                        input_publisher = input(f"New publisher book (current : {current_info['publisher']}): ") or \
                                          current_info["publisher"]
                        if input_publisher.isalpha():
                            book_list[register_id]["publisher"] = input_publisher
                            print("Information updated successfully.")
                            break
                        else:
                            print("incorrect name format!!!")
                            continue

                    # change book year
                    while True:
                        input_year = input(f"New book year (current : {current_info['year']}): ") or current_info[
                            "year"]
                        if input_year.isdigit():
                            book_list[register_id]["year"] = input_year
                            print("Information updated successfully.")
                            break
                        else:
                            print("incorrect year format!!!")
                            continue

                    # change book filed
                    while True:
                        input_filed = input(f"New book year (current : {current_info['filed']}): ") or current_info[
                            "filed"]
                        if input_filed.isalpha():
                            book_list[register_id]["filed"] = input_filed
                            show_generator_ones(book_list[register_id], register_id)
                            break
                        else:
                            print("incorrect Filed format!!!")
                            continue
                else:
                    print("Member not found.")
            else:
                break

    def borrowed_books():
        current_borrowed_books = {}
        for bookID, userID in borrowed_book_list.items():
            if bookID in book_list.keys():
                current_borrowed_books[bookID] = borrowed_book_list[bookID]
        show_generator(current_borrowed_books, "book")

    def unborrowed_books():
        current_unborrowed_books = {}
        for i in book_list.keys():
            if i not in borrowed_book_list.keys():
                current_unborrowed_books[i] = book_list[i]

        show_generator(current_unborrowed_books, "Book")

    while library_frag:
        request_input_library = input(
            "What cad you do : \n\n1) Add book\n2) edit Book\n3) Remove book \n4) show all books\n5) show of borrowed books\n6) been not borrowed book\n0) back\n\nEnter option number: ")
        clear_terminal()

        if request_input_library == "1":
            add_book()
        elif request_input_library == "2":
            edit_book_info()
        elif request_input_library == "3":
            remover("book", book_list)
        elif request_input_library == "4":
            show_generator(book_list, "book")
        elif request_input_library == "5":
            borrowed_books()
        elif request_input_library == "6":
            unborrowed_books()
        elif request_input_library == "":
            pass
        elif request_input_library == "0":
            library_frag = False
        else:
            print(f"'{request_input_library}' not found !!!")
            continue


def get_book():
    registration_time = datetime.now()
    while True:
        input_get_book_id = input("Enter the book ID or enter for back : ")
        if input_get_book_id == "":
            clear_terminal()
            break

        elif int(input_get_book_id) in book_list and int(input_get_book_id) not in borrowed_book_list:

            input_get_user_id = input("Enter the user ID : ")
            if int(input_get_user_id) in user_list:
                input_Return_date = input("Return date : ")
                borrowed_book_user = {"user ID": int(input_get_user_id),
                                      "Date Received": f"{registration_time.year}-{registration_time.month}-{registration_time.day}",
                                      "Return date": input_Return_date}
                borrowed_book_list[int(input_get_book_id)] = borrowed_book_user

                print_ = borrowed_book_list[int(input_get_book_id)]
                for x, y in print_.items():
                    print(f"{x} ------> {y}")
                exit_key = input("Press Enter key to exit...")
                if exit_key == "":
                    clear_terminal()
                    break
                else:
                    break

            else:
                print("user not found !!!")
        else:
            print("This book not found !!!")


while main_frag:

    init()
    clear_terminal()

    request_input_leyer_main = input(
        "Which section would you like to enter? \n\n1) User\n2) Library\n3) Get book\n0) Exit\n\nEnter option number: ")
    clear_terminal()

    if request_input_leyer_main == "1":
        user()
    elif request_input_leyer_main == "2":
        library()
    elif request_input_leyer_main == "3":
        get_book()
    elif request_input_leyer_main == "":
        pass
    elif request_input_leyer_main == "0":
        main_frag = False
    else:
        print(f"'{request_input_leyer_main}' not found!!!")
