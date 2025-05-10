


# 🎬 Netflix Clone

A Netflix clone built with **Django** and styled with **TailwindCSS**. This project fetches movie data from the [TMDB API](https://www.themoviedb.org/) and provides a similar interface to Netflix. It was my first time using TailwindCSS, and the goal was to practice building a dynamic website with a modern UI.

## 🚀 Features

- 🎥 Displays movie data fetched from the [TMDB API](https://www.themoviedb.org/)
- 🔍 Search functionality for movies and TV shows
- 🎬 Movie details page with additional information
- 📱 Responsive UI using TailwindCSS
- 🎨 Clean and minimal design



&nbsp;

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** TailwindCSS, HTML, CSS
- **API:** [TMDB API](https://www.themoviedb.org/)


## 🧑‍💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/TadiwaMakoni05/netflix-clone.git
cd netflix-clone
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up TMDB API Key

* Sign up and get your API key from [TMDB](https://www.themoviedb.org/).
* Create a `.env` file in the root directory and add the following:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the app

```bash
python manage.py runserver
```

The app will run at `http://localhost:8000` (or as specified in your setup).

## 📁 Folder Structure

```
/netflix-clone
  ├── /static/          # Static files (e.g., images, JS, CSS)
  ├── /templates/       # HTML templates
  ├── /movies/          # App that handles movie data
  ├── /accounts/        # App for user authentication
  ├── /media/           # Media files (e.g., user-uploaded images)
  ├── /netflix_clone/   # Project configuration files
  ├── manage.py         # Django management file
  └── requirements.txt  # Project dependencies
```


## 🤛️ Author

* [Tadiwa Makoni](https://github.com/TadiwaMakoni05)

## 📄 License

This project is licensed under the [MIT License](LICENSE).


