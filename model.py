from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# 레시피 데이터 읽기

def recommend(user_ingredients):
    recipe_df = pd.read_csv("temp.csv")

    # TF-IDF 벡터라이저 생성
    tfidf = TfidfVectorizer(token_pattern=r'[^|]+')
    tfidf_matrix = tfidf.fit_transform(recipe_df['Ingr2'])

    user_ingredients_str = '|'.join(list(user_ingredients))
    user_vector = tfidf.transform([user_ingredients_str])

    scores = cosine_similarity(tfidf_matrix, user_vector).flatten()

    # 상위 N개 레시피 추천
    N = 20
    top_indices = scores.argsort()[-N:]
    top_recipes = recipe_df.iloc[top_indices]

    return top_recipes
