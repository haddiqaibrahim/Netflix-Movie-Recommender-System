# Netflix Movie Recommender System

Welcome to the "Netflix Movie Recommender System" project! This Python-based application recommends movies to users based on content similarity using cosine similarity. The goal of the project is to help users discover movies similar to the one they select, using a clean dataset from Netflix. The application is built using Python, machine learning libraries, and deployed using Streamlit for a user-friendly interface.

## Project Overview

The objective of this project is to build a movie recommender system using content-based filtering. It consists of the following main components:

1. **Data Collection & Cleaning:** We use the 'netflix_titles.csv' dataset, which includes movie titles, genres, descriptions, and release years. The dataset is cleaned and processed to remove missing values and duplicates.

2. **Feature Engineering & Similarity Calculation:** Movie descriptions are vectorized using TF-IDF and the cosine similarity between all movies is calculated to find the most similar ones.

3. **Model Building:** We build a content-based recommendation model using cosine similarity. When a user selects a movie, the system finds and recommends the top 5 most similar titles.

4. **Web App with Streamlit:** A simple web application is built using Streamlit, allowing users to select a movie from a dropdown list and get similar movie recommendations displayed on the screen with metadata like genre, release year, and description.

5. **Deployment:** The app is deployed using Streamlit Cloud for easy access and demonstration.

## Repository Structure

The repository is structured as follows:

```

Netflix-Movie-Recommender/
├── app.py                             # Main Streamlit app
├── Movies_Recommender_System.ipynb    # Jupyter notebook for data analysis and model building
├── netflix_titles.csv                 # Original raw dataset
├── cleaned_netflix_titles.csv         # Cleaned and preprocessed dataset
├── requirements.txt                   # Required Python packages
├── README.md                          # Project documentation

````

- The `app.py` file is the entry point for the Streamlit app.
- The notebook contains all the code from data exploration to model creation.
- The datasets include the original and cleaned Netflix data.

## Getting Started

To get started with this project on your local machine:

1. **Clone the Repository:**
```bash
git clone https://github.com/haddiqaibrahim/Netflix-Movie-Recommender-System.git
cd Netflix-Movie-Recommender
````

2. **Create a Virtual Environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit App:**

```bash
streamlit run app.py
```

## Data Files

* `netflix_titles.csv`: Original dataset containing Netflix movie/TV show titles and details.
* `cleaned_netflix_titles.csv`: Cleaned and filtered data used for modeling.

## Usage

1. Launch the Streamlit app using the command above.
2. Select a movie title from the dropdown.
3. Click “Recommend” to see the top 5 similar movies with details.

## Contributions

Contributions, ideas, and improvements are welcome! If you notice any bugs or want to enhance functionality, feel free to fork the repo and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

This project uses various Python libraries such as Pandas, Scikit-learn, Streamlit, and others. Special thanks to the open-source community for datasets and tools. Project developed by Haddiqa Ibrahim, BS Data Science student at Islamia University Bahawalpur.

