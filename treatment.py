import pandas as pd
import os


class Series:
    """ Class using CRUD among the series' DataFrames """

    def __init__(self):
        """ Constructor instantiate the class and get the DataFrame's """

        # Put your correct path for both Excel's
        self.__data_frame_final = pd.read_excel("../../../Desktop/Code/Series/s_final.xlsx")
        self.__data_frame_ongoing = pd.read_excel("../../../Desktop/Code/Series/s_ongoing.xlsx")

    def show_final_df(self):
        """ Method to list the finished series """

        counter = 1
        print("\nYour finished series: ")
        for series in self.__data_frame_final['Serie']:
            print(f'{counter:2d} - {series}')
            counter += 1

    def show_ongoing_df(self):
        """ Method to list the ongoing series """

        counter = 1
        print("\nYour ongoing series: ")

        # Iterating the DataFrame to show the list
        for iterator in range(0, len(self.__data_frame_ongoing)):
            print(
                f"{counter:2d} - {self.__data_frame_ongoing['Serie'][iterator]}: "
                f"Season {self.__data_frame_ongoing['Season'][iterator]}, "
                f"Episode {self.__data_frame_ongoing['Episode'][iterator]}")
            counter += 1

    def add_finished_serie(self):
        """ Method to add finished series being in ongoing series or not """

        # Input to know if the serie to be added is ongoing or not
        user_input = int(input(f"\nWas this serie an ongoing one?\n0) No\n1) Yes\nYour answer(digit): "))

        if user_input == 1:
            self.show_ongoing_df()
            u_input = int(input("\nType the digit of the serie: "))

            finished = self.__data_frame_ongoing['Serie'][u_input - 1]
            self.__data_frame_ongoing = self.__data_frame_ongoing.drop(u_input - 1)
            send_message(finished, 'o', 'del')

            self.__data_frame_final.loc[len(self.__data_frame_final.index)] = finished

        elif user_input == 0:
            finished = input('What is the name of the finished serie: ').title()
            self.__data_frame_final.loc[len(self.__data_frame_final.index)] = finished

        else:
            print('\nNot available option!')
            return

        self.__data_frame_final = sort_df(self.__data_frame_final)
        send_message(finished, 'f', 'add')

    def add_ongoing_serie(self):
        """ Method to add ongoing series """

        serie_name = input('\nWhat is the name of the serie: ').title()
        serie_season = int(input('What is the season that you started(digit): '))
        serie_episode = int(input('What is the next episode(digit): '))

        self.__data_frame_ongoing.loc[len(self.__data_frame_ongoing.index)] = [serie_name, serie_season, serie_episode]
        self.__data_frame_ongoing = sort_df(self.__data_frame_ongoing)

        send_message(serie_name, 'o', 'add')

    def update_serie(self):
        """ Method to update ongoing series """

        self.show_ongoing_df()
        user_input = int(input('Type the number of the serie: '))

        serie = self.__data_frame_ongoing['Serie'][user_input - 1]

        u_input = int(input('\nDo you want to update:\n1) The season\n2) The episode\n3) Both\nYour option(digit): '))

        if u_input == 1:
            season_input = int(input('Type the number of the new season: '))
            self.__data_frame_ongoing.loc[user_input - 1, 'Season'] = season_input

        elif u_input == 2:
            episode_input = int(input('Type the number of the new episode: '))
            self.__data_frame_ongoing.loc[user_input - 1, 'Episode'] = episode_input

        elif u_input == 3:
            s_input = int(input('First, type the number of the new season(digit): '))
            e_input = int(input('Type the number of the new episode(digit): '))
            self.__data_frame_ongoing.loc[user_input - 1] = [serie, s_input, e_input]

        else:
            print('\nNot available option')
            return

        send_message(serie, 'o', 'up')

    def delete_serie(self):
        """ Method to delete any serie """

        user_input = int(input("\nDo you want to delete:\n0) Finished serie\n1) Ongoing serie\n\nYour option(digit): "))

        if user_input == 0:
            self.show_final_df()
            u_input = int(input("\nType the digit of the serie to be deleted: "))
            serie = self.__data_frame_final['Serie'][u_input - 1]
            self.__data_frame_final = self.__data_frame_final.drop(u_input - 1)

            send_message(serie, 'f', 'del')

        elif user_input == 1:
            self.show_ongoing_df()
            u_input = int(input("\nType the digit of the serie to be deleted: "))
            serie = self.__data_frame_ongoing['Serie'][u_input - 1]
            self.__data_frame_ongoing = self.__data_frame_ongoing.drop(u_input - 1)

            send_message(serie, 'o', 'del')

        else:
            print('\nNot available option')
            return

    def try_save(self):
        """Method that try to save the datas depending on the permission being granted or not"""

        try:
            save_excel(self.__data_frame_final, 'f')
            save_excel(self.__data_frame_ongoing, 'o')

        except PermissionError:
            print("\nI can't access your excel to save your changes, please close it, then type something!")
            os.system('pause')
            self.try_save()


def sort_df(Data_Frame):
    """ Function to sort the Dataframe on the necessary way """

    return Data_Frame.sort_values(by='Serie')


def save_excel(Data_Frame, type_):
    """ Function to save the DataFrame on the correct Excel (final/ongoing) """

    mode = None
    if type_ == 'f':
        mode = 'final'
    elif type_ == 'o':
        mode = 'ongoing'

    Data_Frame.to_excel(f's_{mode}.xlsx', index=False)


def send_message(serie, mode, add_del_up):
    """Function that send the specific message of what is going on wih the manipulation on the DataFrame"""

    action = type_ = connector = None

    match add_del_up:
        case 'add':
            action, connector = 'added', 'to'
        case 'del':
            action, connector = 'deleted', 'from'
        case 'up':
            action, connector = 'updated', 'in'

    if mode == 'f':
        type_ = 'finished'
    elif mode == 'o':
        type_ = 'ongoing'

    # Alternative way for who don't have python 3.10
    #
    # dict1 = {'add': ('added', 'to'),
    #          'del': ('deleted', 'from'),
    #          'up': ('updated', 'in')}
    #
    # action, connector = dict1[add_del_up]
    #
    # dict2 = {'f': 'finished', 'o': 'ongoing'}
    # type_ = dict2[mode]

    print(f"\n'{serie}' {action} {connector} {type_} series!")
