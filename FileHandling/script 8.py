import os ,sys

fileNmae = input("ente the filr name: ")
if os.path.isfile(fileNmae):
    f = open(fileNmae,'+a')
else :
    print("file not found..")
    sys.exit()

def write_to_file():
    line = input("\nEnter a line of text to be written in file:\n")
    if len(line) == 0:
        print('No data entered, nothing added to file.')
    else:
        f.write('\n' + line)
        print('Data added to file.')

# Main program loop - continues until user enters 'q' or 'Q'.
while True:
    choice = input("\n\nMenu\n1. Write Text\n2. View File Contents\n3. Exit Program\n\nEnter your choice (1/2/3/q/Q): ").lower()

    choice = input("\n\nMenu\n1.Write to File\n2.Display Contents\n3.Exit\nEnter your choice (q/Q to quit):\t").lower()
    choice = input("\n\nMenu \n1. Write to File \n2. Quit \nEnter your choice (1/2/q/Q): ").lower()
    if choice == '1':
        write_to_file()
    elif choice == '2' or choice == 'q' or choice == 'Q':
        break
    else:
        print("Invalid Entry! Please enter valid option.")