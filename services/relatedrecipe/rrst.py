import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the CSV data and preprocess it
recipe = pd.read_csv("ff.csv")
recipe = recipe[['RecipeName','Ingredients','Cuisine','Course', 'Diet']]
recipe['tags'] = recipe['Cuisine'] + recipe['Ingredients'] + recipe['RecipeName']
new_data = recipe.drop(columns=['Cuisine', 'Ingredients', 'Course', 'Diet'])

print(new_data)
# Vectorization
cv = CountVectorizer(max_features=99, stop_words='english')
vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray()

# Cosine Similarity
similarity = cosine_similarity(vector)

# Recommendation function
def recommend(recipee):
    index = new_data[new_data['RecipeName'] == recipee].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    return [new_data.iloc[i[0]].RecipeName for i in distance[1:6]]

# Streamlit app
def main():
    st.title("Recipe Recommendation")
    st.write("Enter a recipe name to get related recipe recommendations:")

    recipe_name_input = st.text_input("Enter Recipe Name")
    if st.button("Get Recommendations"):
        if recipe_name_input:
            recommended_recipes = recommend(recipe_name_input)
            st.write("RELATED RECIPES:")
            for rec in recommended_recipes:
                st.write(rec)
        else:
            st.write("Please enter a recipe name.")

if __name__ == "__main__":
    main()
