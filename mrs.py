# Movie Recommendation System Project

def add_movie(movie_db):
    title = input("Enter the movie title: ")
    genre = input("Enter the movie genre: ")
    
    if genre not in movie_db:
        movie_db[genre] = []
    movie_db[genre].append(title)
    print(f"Movie '{title}' added to the genre '{genre}'.")

def recommend_movies(user_history, user_genres, movie_db):
    recommendations = []
    for genre in user_genres:
        if genre in movie_db:
            for movie in movie_db[genre]:
                if movie not in user_history:
                    recommendations.append(movie)
    if recommendations:
        print("We recommend these movies for you:")
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print("No new recommendations available.")

def main():
    movie_db = {}
    user_history = []
    user_genres = set()
    
    while True:
        print("\nMovie Recommendation System")
        print("1. Add a movie")
        print("2. Add to user history")
        print("3. Add to user favorite genres")
        print("4. Get recommendations")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_movie(movie_db)
        elif choice == '2':
            movie = input("Enter the movie you watched: ")
            user_history.append(movie)
            print(f"Added '{movie}' to your history.")
        elif choice == '3':
            genre = input("Enter your favorite genre: ")
            user_genres.add(genre)
            print(f"Added '{genre}' to your favorite genres.")
        elif choice == '4':
            recommend_movies(user_history, user_genres, movie_db)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
