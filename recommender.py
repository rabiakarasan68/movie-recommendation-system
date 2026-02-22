from model import df, similarity 

def recommend(movie_name):
    movie_name_clean = movie_name.lower().strip()  
    titles = df["title"].str.lower().str.strip()      
    titles_no_year = titles.str.replace(r"\(\d{4}\)", "", regex=True).str.strip()

    if movie_name_clean not in titles_no_year.values:
        print("Available movies:", titles.head(10))  
        return ["Movie not found"]
    
    index = df[titles_no_year == movie_name_clean].index[0] 
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i in scores[1:6]:
        recommended_movies.append(df.iloc[i[0]].title)

    return recommended_movies
