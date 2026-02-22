# 🎬 Movie Recommendation System

A content-based movie recommendation system built with Python using TF-IDF and cosine similarity.
The project includes a simple Tkinter GUI for user interaction.

## 🚀 Features

Content-based recommendation system

TF-IDF vectorization

Cosine similarity for similarity calculation

Tkinter graphical user interface

Case-insensitive movie search

Automatic year removal from titles (e.g., "Toy Story (1995)")

## 🧠 How It Works

Movie genres are converted into numerical vectors using TF-IDF (Term Frequency – Inverse Document Frequency).

Cosine similarity is calculated between all movies.

When the user enters a movie name:

The system finds the movie in the dataset

Computes similarity scores

Returns the top 5 most similar movies

## ⚠️ Dataset Notice

movies.csv is not included in this repository.

To run the project:

Download a movie dataset

Place movies.csv inside the project folder.

Ensure the dataset contains at least:

title column

genres column

## 🛠️ Installation

Make sure Python 3.x is installed.

Install required libraries:

pip install pandas scikit-learn

⚠️ Tkinter usually comes pre-installed with Python.

## ▶️ How to Run

Run:

python main.py

The GUI window will open.

Enter a movie name and click Recommend.

## 🖥️ GUI Details

Users can only type in the movie input field.

Recommendation results cannot be manually edited.

Right-click and mouse modifications are disabled in the results area.

## 📊 Technologies Used

Python

Pandas

Scikit-learn

TF-IDF Vectorizer

Cosine Similarity

Tkinter
