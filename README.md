# 🎬 FlickSift - Movie Recommendation System

A content-based movie recommendation system that helps users discover their perfect movies instantly using machine learning and natural language processing techniques.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

FlickSift is an intelligent movie recommendation system that analyzes movie content (overview, genre) to find similar movies. The system uses content-based filtering with cosine similarity to provide personalized movie recommendations based on user preferences.

## ✨ Features

- **Content-Based Filtering**: Recommends movies based on content similarity
- **Interactive Web Interface**: User-friendly Streamlit web application
- **Real-time Recommendations**: Instant movie suggestions
- **Large Movie Database**: Comprehensive collection of movies with detailed information
- **Cosine Similarity Algorithm**: Advanced similarity calculation for accurate recommendations

## 🛠️ Technology Stack

- **Python 3.8+**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning library
- **CountVectorizer** - Text feature extraction
- **Cosine Similarity** - Similarity calculation algorithm
- **Pickle** - Model serialization
- **Hugging Face Hub** - Model hosting and distribution

## 📁 Project Structure

```
01. Recommendation System/
├── app.py              # Streamlit web application
├── model.py            # Machine learning model training
├── dataset.csv         # Movie dataset (3.4MB)
├── Notebook.ipynb      # Jupyter notebook for analysis
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gandharvk422/FlickSift
   cd "01. Recommendation System"
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 💻 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Select a movie** from the dropdown menu

4. **Click "Show Recommendations"** to get 5 similar movie suggestions

## 🔬 How It Works

### 1. Data Processing
- Loads movie dataset with columns: `id`, `title`, `genre`, `overview`
- Combines `overview` and `genre` into a single `tags` column
- Preprocesses text data for feature extraction

### 2. Feature Extraction
- Uses CountVectorizer to convert text tags into numerical vectors
- Extracts up to 10,000 features from movie descriptions
- Removes English stop words for better feature quality

### 3. Similarity Calculation
- Computes cosine similarity between all movie vectors
- Creates a similarity matrix for efficient recommendation lookup
- Stores pre-computed similarities for fast retrieval

### 4. Recommendation Generation
- Finds the index of the selected movie
- Retrieves similarity scores for all other movies
- Returns top 5 most similar movies based on cosine similarity

## 📊 Dataset

The system uses a comprehensive movie dataset containing:
- **Movie ID**: Unique identifier for each movie
- **Title**: Movie name
- **Genre**: Movie categories (comma-separated)
- **Overview**: Movie description/synopsis
- **Additional metadata**: Language, popularity, release date, ratings

**Dataset Size**: 3.4MB with thousands of movies

## 🧠 Model Architecture

```
Input: Movie Selection
    ↓
Content Analysis (Overview + Genre)
    ↓
Text Vectorization (CountVectorizer)
    ↓
Similarity Matrix (Cosine Similarity)
    ↓
Top-K Recommendations
    ↓
Output: Similar Movies
```

### Key Components:

1. **CountVectorizer**
   - `max_features=10000`: Limits vocabulary size
   - `stop_words="english"`: Removes common English words
   - Converts text to TF-IDF vectors

2. **Cosine Similarity**
   - Measures angle between vectors
   - Range: 0 (dissimilar) to 1 (identical)
   - Computes pairwise similarities

3. **Recommendation Algorithm**
   - Sorts movies by similarity score
   - Excludes the selected movie itself
   - Returns top 5 recommendations

## 🔌 API Reference

### Main Functions

#### `recommend(movie)`
Returns 5 movie recommendations based on content similarity.

**Parameters:**
- `movie` (str): Title of the selected movie

**Returns:**
- `list`: List of 5 recommended movie titles

#### `train_model()`
Trains the recommendation model and saves to pickle files.

**Files Created:**
- `movies_list.pkl`: Processed movie data
- `similarity.pkl`: Pre-computed similarity matrix

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest

# Format code
black .
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Skyhighes Internship Course** for project guidance
- **TMDB Dataset** for movie information
- **Streamlit** for the web framework
- **Scikit-learn** for machine learning capabilities

## 📞 Contact

For questions or support, please open an issue in the repository.

---

**Made with ❤️ for movie lovers everywhere!** 