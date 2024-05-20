import json
from urllib.request import urlopen


def search_movie():
    api_key = "e10deafc"
    insert_movie = input("What movie do you wanna know about? (Name movie in english): ").replace(" ", "+")
    movie_details_access = urlopen(f"http://www.omdbapi.com/?apikey={api_key}&t={insert_movie}&plot=short").read()
    movie_data = json.loads(movie_details_access)
    # print(json.dumps(movie_data))  # use for see the details of the movies.
    print(f"The movie {movie_data['Title']} is released in {movie_data['Released']} with an runtime of: "
                     f"{movie_data['Runtime']}, Genre: {movie_data['Genre']} and with an IMDB Rating of: "
                     f"{movie_data['imdbRating']}")


def main():
    while True:
        what_to_do = input("Choose what you wanna do: A) for search movie or B) for exit: ").upper()
        if what_to_do == "A":
            search_movie()
        elif what_to_do == "B":
            print("Goodbye!")
            break
        else:
            print("Don't recognize that command...")


if __name__ == '__main__':
    main()
