#!/usr/bin/env python3
def display_menu():
    #week 0 sepcial instructions 
    print("What is the meaning of life")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 0
        for movie in movie_list:
            row = movie
            print(str(i+1) + ". " + row[0]
                  + " [" + str(row[1]) + "]"    #add concatenate for pricing & display the pricing in square brackets
                  + " @ " + str(row[2]))
            i += 1
        print()

def add(movie_list):
    #these 3 rows are concatenated name[0], year[1], price[2]
    name = input("Name: ")
    year = input["Year: "]
    price = input["Price: "]
    movie = []
    movie.append(name)
    movie.append(year)
    #add a movie append method for adding the price 
    movie.append(price)
    movie_list.append(movie)
    print(movie[0] + " was added.\n")
      
def delete(movie_list):
    number = int(input("Number: "))
    #delete function checks for input or if the number exceeds number list array 
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0] + " was deleted.\n")

#create the function for finding the year of the movie 
def find_year(movie_list):
    year = int(input("Year: "))    
    for movie in movie_list:
        if movie[1] == year:
            print(movie[0] + " was released in " + str(year))
    print()

    ##error thrown for null or value less than zero 
    #if year == NULL or year < 1877:
        #print("Invalid year date.\n")
    #else: 
        ##create a pop method to erase the movie year based on release 
        # movie = movie_list.find(year)
         ##print the movie and release date for the find method
         #print(movie[0] + "was released in" + " " + [year])

def main():                                                
    movie_list = [["Monty Python and the Holy Grail", 1975, 9.95],
                 ["On the Waterfront", 1954, 5.59],
                 ["Cat on a Hot Tin Roof", 1958, 7.95],
                 ["Cat on a Hot Tin Roof", 1958, 14.95]]
    
    display_menu()
    print()
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        #add a find command for the user input 
        elif command == "find":
            find_year(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
