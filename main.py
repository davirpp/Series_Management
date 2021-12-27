from treatment import *


os.system('cls')
user_input = input("""
What do you wanna do: 

1) List finished series
2) List ongoing series
3) Add a finished serie
4) Add an ongoing serie
5) Update serie's episode
6) Delete a serie
0) Close the application and save changes

Your option(digit): """)

# Instantiating the class
mySerie = Series()

# Read the input from the user and do the action chosen by the user
while True:
    match user_input:
        case '0' | '':
            break
        case '1':
            mySerie.show_final_df()
        case '2':
            mySerie.show_ongoing_df()
        case '3':
            mySerie.add_finished_serie()
        case '4':
            mySerie.add_ongoing_serie()
        case '5':
            mySerie.update_serie()
        case '6':
            mySerie.delete_serie()
        case _:
            print('Your number is not an option. Try again...')

    print()
    os.system('pause')
    os.system('cls')
    # Instantiating again to avoid problems of unsaved changes
    # mySerie = Series()
    user_input = input("""
What do you wanna do: 

1) List finished series
2) List ongoing series
3) Add a finished serie
4) Add an ongoing serie
5) Update serie's episode
6) Delete a serie
0) Close the application and save changes

Your option(digit): """)

print('\nYou are closing the program...')
mySerie.try_save()
print('\nYour changes have been saved!\n')
os.system('pause')
