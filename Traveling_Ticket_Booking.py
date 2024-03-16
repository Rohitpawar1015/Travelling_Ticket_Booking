import random

def get_user_details():
    first_name = input("\t\t\t First Name :\t")
    last_name = input("\t\t\t Last Name :\t")
    age = input("\t\t\t Age :\t")
    while True:
        mobile_no = input("\t\t\t Mobile no. :")
        length = len(mobile_no)
        if length == 10:
            return 0
        else:
            print("\t\t\t Invalid mobile number please reenter again....")

def print_transport_details(transport_mode, selected_destination, details):
    print("\t\t\tDetails as shown below:")
    destination_details = details[transport_mode][selected_destination.capitalize()]
    print("\t\t\t\tDate: ", destination_details["Date"])
    print("\t\t\t\tTime: ", destination_details["Time"])
    print("\t\t\t\tBudgets: ", destination_details["Budgets"])
    print("\t\t\t\tduration: ", destination_details["duration"])

def main():
    print("\n\t\t**************Welcome To Travelling World****************")
    print("\n")
    print("\t\t\t\t--------------\t\t\t")
    print("\t\t\t\t| Login Page |\t\t\t")
    print("\t\t\t\t--------------\t\t\t")
    print("\n")

    # Authentication
    admin = input("\t\t\tEnter userId :\t")
    password = input("\t\t\tEnter the Password :\t")

    if admin == "abc" and password == "123":
        print("\t--------------------------------------------------------------")
        r1 = random.randint(1, 50)
        r2 = random.randint(51, 100)
        addition = r1 + r2
        print("\t\t\tThe captcha is:\t", "(", r1, "+", r2, ")")
        captcha = int(input("\t\t\tSolve the captcha :\t"))
        if captcha == addition:
            print("\t--------------------------------------------------------------")
            print("\t\t\tYou Are Succefully Logged In.....\t")
            print("\t--------------------------------------------------------------")
        else:
            print("\t\t\tInvalid capture...... \t")
            print("\t\t\tRe-enter the capture......")
            captcha = input("\t\t\tSolve the captcha :\t")
    else:
        print("\t\t\tinvalid information\t")
        print("\t--------------------------------------------------------------")

    print("\t\t\tYour transport mediums are: \n\t\t\t\t\t1)BUS\n\t\t\t\t\t2)TRAIN\n\t\t\t\t\t3)AIROPLANE\n")
    transport_medium = input("\t\t\tEnter your transport medium:\t").upper()
    print("\t\t\tYour Arrival location is PUNE.")
    print("\t\t\tYour Destination's location are:\n\t\t\t\t\t1)Mumbai\n\t\t\t\t\t2)Thane\n\t\t\t\t\t3)Nagpur\n\t\t\t\t\t4)Nashik\n\t\t\t\t\t5)SambhajiNagar")
    selected_destination = input("\t\t\tChoose one of them:\t").capitalize()

    details = {
        "BUS": {
            "Mumbai": {"Date": "27-06-2022", "Time": "10:30 AM", "Budgets": 600, "duration": "4hr"},
            "Thane": {"Date": "27-06-2022", "Time": "10:30 AM", "Budgets": 800, "duration": "5hr"},
            # Add other destinations
        },
        # Add other transport modes
    }

    if transport_medium in details:
        if selected_destination in details[transport_medium]:
            print_transport_details(transport_medium, selected_destination, details)
        else:
            print("Invalid destination")
    else:
        print("Invalid transport medium")

    n = int(input("\t\t\tEnter no of passengers:"))
    print("\t--------------------------------------------------------------")

    for i in range(1, n + 1):
        print("\t\t\tPassenger No:", i)
        get_user_details()
        if n == i:
            break
        i += 1

    bill = details[transport_medium][selected_destination]["Budgets"] * n
    print("\t\t\tYour total bill amount is :", bill)
    print("\n\t\t\tYour details are successfully saved")
    print("\n\t\t\tTHANK YOU!")

if __name__ == "__main__":
    main()
