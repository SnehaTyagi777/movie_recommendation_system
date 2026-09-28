# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built with **Python, Streamlit, Scikit-learn, Joblib, and the OMDb API**.

The application allows users to select a movie and receive a list of similar movies based on the similarity between their feature vectors. Movie posters are dynamically fetched using the OMDb API and displayed along with the recommendations.

---

## 📌 Project Overview

The Movie Recommendation System is designed to help users discover movies similar to a movie they already like.

The application follows a **content-based recommendation approach**. Instead of relying on ratings from other users, the system uses information/features associated with movies to identify movies that are similar to the selected movie.

### Example

If a user selects:

> **Inception**

the system analyzes the corresponding movie representation and finds other movies with similar feature representations.

The application then displays the recommended movies along with their posters.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Build a movie recommendation system using Python.
- Recommend movies based on content similarity.
- Convert movie information into numerical feature representations.
- Use a nearest-neighbor approach to find similar movies.
- Develop an interactive web interface using Streamlit.
- Fetch movie posters dynamically using the OMDb API.
- Allow users to control the number of recommendations.
- Provide an optional similarity score for recommendations.
- Provide a fallback poster when a movie poster is unavailable.

---

## 🧠 Recommendation Approach

This project uses **Content-Based Filtering**.

In content-based recommendation, the system recommends items that are similar to the item selected by the user.

The general flow is:

```text
Movie Dataset
      ↓
Data Processing
      ↓
Feature Representation
      ↓
Numerical Vectors
      ↓
Similarity / Nearest Neighbor Model
      ↓
Find Similar Movies
      ↓
Streamlit Application
      ↓
Display Recommendations
