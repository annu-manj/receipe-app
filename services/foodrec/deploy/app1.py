from flask import Flask, request, jsonify
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Load the necessary data
food = pd.read_csv("food.csv")
ratings = pd.read_csv("ratings.csv")
combined = pd.merge(ratings, food, on='Food_ID')

@app.route('/recommend', methods=['POST'])
def recommend_food():
    data = request.json
    
    # Extract the input parameters from the request data
    cuisine = data.get('cuisine', '')
    vegn = data.get('vegn', '')
    val = data.get('val', 0)
    finallist = data.get('finallist', '')

    # Perform the recommendation based on the input
    recommendations = food_recommendation(cuisine, vegn, val, finallist)
    
    # Return the recommended dishes as a JSON response
    return jsonify({'recommendations': recommendations})

def food_recommendation(cuisine, vegn, val, finallist):
    ans = combined.loc[(combined.C_Type == cuisine) & (combined.Veg_Non == vegn) & (combined.Rating >= val), ['Name', 'C_Type', 'Veg_Non']]
    names = ans['Name'].tolist()
    x = np.array(names)
    ans1 = np.unique(x)

    display = []
    if finallist:
        dataset = ratings.pivot_table(index='Food_ID', columns='User_ID', values='Rating')
        dataset.fillna(0, inplace=True)
        csr_dataset = csr_matrix(dataset.values)
        dataset.reset_index(inplace=True)

        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
        model.fit(csr_dataset)

        n = 10
        FoodList = food[food['Name'].str.contains(finallist)]
        if len(FoodList):
            Foodi = FoodList.iloc[0]['Food_ID']
            Foodi = dataset[dataset['Food_ID'] == Foodi].index[0]
            distances, indices = model.kneighbors(csr_dataset[Foodi], n_neighbors=n + 1)
            Food_indices = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key=lambda x: x[1])[:0:-1]
            Recommendations = []
            for val in Food_indices:
                Foodi = dataset.iloc[val[0]]['Food_ID']
                i = food[food['Food_ID'] == Foodi].index
                Recommendations.append(food.iloc[i]['Name'].values[0])
            display = Recommendations
    
    return display

if __name__ == '__main__':
    app.run()
