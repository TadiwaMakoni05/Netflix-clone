from django.shortcuts import render
import requests
# Create your views here.
def get_now_playing_movies():
    now_playing_movies = []
    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NWNlYWM0NTgxZDM5YjYyZTRkZDllM2I5ZTFjNzk3YyIsIm5iZiI6MTcxMjQ5Mjg1NC4yNDMsInN1YiI6IjY2MTI5MTM2MWYzMzE5MDE3ZGMzMTQyYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fP5dr2vCz3ZC6DYLVzuMvQrU-qYMFbkkdDHVZb2nbnI" 
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()  
        results = data.get('results', [])
        for movie in results:
            movie_id = movie['id']
            title = movie['title']
            overview =  movie['overview']
            poster_path = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            now_playing_movies.append({
                'id':movie_id,
                'title': title,
                'overview' : overview,
                'poster_path': poster_path
            })
    else:
        print("Failed to fetch data")
        return []
    return now_playing_movies

def get_popular_movies():
    popular_movies = []
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NWNlYWM0NTgxZDM5YjYyZTRkZDllM2I5ZTFjNzk3YyIsIm5iZiI6MTcxMjQ5Mjg1NC4yNDMsInN1YiI6IjY2MTI5MTM2MWYzMzE5MDE3ZGMzMTQyYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fP5dr2vCz3ZC6DYLVzuMvQrU-qYMFbkkdDHVZb2nbnI"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json() 
        results = data.get('results', [])
        for movie in results:
            movie_id = movie['id']
            title = movie['title']
            overview =  movie['overview']
            poster_path = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            popular_movies.append({
                'id':movie_id,
                'title': title,
                'overview' : overview,
                'poster_path': poster_path
            })
    else:
        print("Failed to fetch data")
        return []
    return popular_movies

def get_top_rated_movies():
    top_rated_movies = []
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NWNlYWM0NTgxZDM5YjYyZTRkZDllM2I5ZTFjNzk3YyIsIm5iZiI6MTcxMjQ5Mjg1NC4yNDMsInN1YiI6IjY2MTI5MTM2MWYzMzE5MDE3ZGMzMTQyYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fP5dr2vCz3ZC6DYLVzuMvQrU-qYMFbkkdDHVZb2nbnI"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()  
        results = data.get('results', [])
        for movie in results:
            movie_id = movie['id']
            title = movie['title']
            overview =  movie['overview']
            poster_path = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            top_rated_movies.append({
                'id':movie_id,
                'title': title,
                'overview' : overview,
                'poster_path': poster_path
            })
    else:
        print("Failed to fetch data")
        return []
    return top_rated_movies

def get_upcoming_movies():
    upcoming_movies = []
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NWNlYWM0NTgxZDM5YjYyZTRkZDllM2I5ZTFjNzk3YyIsIm5iZiI6MTcxMjQ5Mjg1NC4yNDMsInN1YiI6IjY2MTI5MTM2MWYzMzE5MDE3ZGMzMTQyYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fP5dr2vCz3ZC6DYLVzuMvQrU-qYMFbkkdDHVZb2nbnI"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()  
        results = data.get('results', [])
        for movie in results:
            movie_id = movie['id']
            title = movie['title']
            overview =  movie['overview']
            poster_path = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            upcoming_movies.append({
                'id':movie_id,
                'title': title,
                'overview' : overview,
                'poster_path': poster_path
            })
    else:
        print("Failed to fetch data")
        return []
    return upcoming_movies

def watch_movie(request,movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NWNlYWM0NTgxZDM5YjYyZTRkZDllM2I5ZTFjNzk3YyIsIm5iZiI6MTcxMjQ5Mjg1NC4yNDMsInN1YiI6IjY2MTI5MTM2MWYzMzE5MDE3ZGMzMTQyYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fP5dr2vCz3ZC6DYLVzuMvQrU-qYMFbkkdDHVZb2nbnI"
    }
    response = requests.get(url, headers=headers)
    movie = {}
    if response.status_code == 200:
        data = response.json().get("results", [])
    
    for video in data:
        if video["site"] == "YouTube":
            movie = video
            print(video, "--video here")
            return render(request,'movie-details.html',{'movie':movie})
        else:
            print("Failed to fetch data")
            return render(request,'movie-details.html',{'movie':'no movie'})

def index(request):
    now_playing = get_now_playing_movies()
    upcoming = get_upcoming_movies()
    top_rated = get_top_rated_movies()
    popular = get_popular_movies()
    context = {
        'now_playing':now_playing,
        'upcoming':upcoming,
        'top_rated':top_rated,
        'popular':popular,
    }
    return render(request,'index.html',context)

