import csv
FILENAME ='movies.csv'

def write_movies(movies):
 with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)

def read_movies():
    movies = []
    with open(FILENAME, "r", newline=" ") as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append(row)
    return movies

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0] ({movie[1]})}")
    print()

def add_movies():
        name = input("Name: ")
        year = input("Year Released: ")
        movie = [name,year]
        movie.append(movie)
        write_movies(movie)
        print(f"{name} was added.\n")

def delete_movies():
    index = int(input("Enter Movie Number: "))
    if index < 1 or index > len(movie):
        print("Invalid movie number.\n")
    else:
        movie = movie.pop(index - 1)
        write_movies(movie)
        print(f"{movie[0]} was deleted.\n")
def display_menu():
    print("The CSV Movie List Program")
    print()
    print("COMMAND MENU")
    print("List - List all movies")
    print("Add - Add a movies")
    print("Del - Delete a movie")
    print("Exit - Exit the program")
    print()

def main():
    display_menu()
    movies= read_movies()
    while True:
        command = input("What do you want to do ?:")
        if command.lower == "list":
            list_movies(movies)
        elif command.lower == "add":
            add_movies(movies)
        elif command.lower== "del":
             delete_movies(movies)
        elif command.lower == "exit":
            break
        else:
            print("Not a valid command. please try again.\n")
            print("bye")
    
if __name__ == "__main__":
    main()