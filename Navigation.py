from Graph import *


class Navigation(object):
    def __init__(self, csv):
        self.__map = Graph(csv)
        self.__prev = None
        self.__finished = False
        self.__cnt = 0

    def navigate(self, start, end, disabled=False):
        try:
            dist, path = self.__map.shortest_path(start, end, disabled)
            self.__map.parse_path(path)
            print("Total distance: " + str(dist))
        except ValueError as err:
            print(err)

    def simulate(self):
        self.__map.print_nodes()
        FLAGS = True
        while FLAGS:
            if self.__cnt == 0:
                input("Welcome to the zoo! All the input is case-sensitive (press Enter to continue)")
            start = input("start (press Enter to continue): ")
            if not start or start.strip() == "":
                start = self.__prev
            end = input("end (press Enter to continue): ")
            print("Need disabled accessibility? Y/N (press Enter to continue) ")
            disabled = self.yes_or_no()
            self.navigate(start, end, disabled)
            self.__prev = end
            self.__cnt += 1
            print("Do you want to continue? Y/N (press Enter to continue) ")
            answer = self.yes_or_no()
            if answer == False:
                FLAGS = False
                print("Thanks for using the tool. Bye!")

    def yes_or_no(self):
        x = input("Your Input: ")
        if x == "Y":
            y = True
            return y
        elif x == "N":
            y = False
            return y
        else:
            x = None
            self.yes_or_no()
