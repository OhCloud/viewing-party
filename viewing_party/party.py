def create_movie(title, genre, rating):
    dict_of_movies = {
        "title" : title,
        "genre" : genre,
        "rating" : rating
    }

    if not title or not genre or not rating:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
        return user_data

def get_watched_avg_rating(user_data):
    
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        total = 0
        for movie in user_data["watched"]:
            total += movie["rating"]
    return total / len(user_data["watched"])

def get_most_watched_genre(user_data):
    
    genres = {}
    most_watched = None
    genre_count = 0

    for movie in user_data["watched"]:
        if movie["genre"] in genres:
            genres[movie["genre"]] += 1
        else:
            genres[movie["genre"]] = 1
        
    for genre in genres.items():
        if genre[1] > genre_count:
            genre_count = genre[1]
            most_watched = genre[0]
    
    return most_watched

def get_unique_watched(user_data):

    user_movie_list = []
    friends_watched = []
    unique_watched_list = []
    
    for movie in user_data["watched"]:
        user_movie_list.append(movie["title"])

    for friend in user_data["friends"]:
        for title in friend["watched"]:
            friends_watched.append(title["title"])

    for film in user_movie_list:
        if film not in friends_watched:
            unique_watched_list.append({title:film})
    
    return unique_watched_list

def get_friends_unique_watched(user_data):
    
    user_movie_list = []
    friends_watched = []
    unique_watched_list = []
    
    for movie in user_data["watched"]:
        user_movie_list.append(movie["title"])

    for friend in user_data["friends"]:
        for title in friend["watched"]:
            friends_watched.append(title["title"])
    
    for film in friends_watched:
        if film not in user_movie_list:
            print("This movie not in list: " + film)

            if {"title":film} not in unique_watched_list:
                unique_watched_list.append({"title":film})
                print(unique_watched_list)
            else:
                continue
        
    return unique_watched_list

def get_available_recs(user_data):
    
    recommended_movies = []
    friends_watched= []

    for watched in user_data["friends"]:
        for movie in watched["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)
            
    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    
    return recommended_movies




