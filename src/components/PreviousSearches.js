import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import axios from 'axios';

export default function PreviousSearches({ searchQuery, setSearchQuery }) {
  const searches = ['pizza', 'burger', 'cookies', 'juice', 'biriyani', 'salad', 'ice cream', 'Shawarma', 'pudding', 'soup'];

  {/*const searchRecipe = () => {
    axios
      .get(`http://127.0.0.1:5000/recipe/${encodeURIComponent(searchQuery)}`)
      .then(function (response) {
        console.log(response);
        const recipeName = response.data.recipename; // Assuming the recipe name is provided in the JSON response
        setSearchQuery(recipeName);
      })
      .catch(function (error) {
        console.log(error);
      });
  };*/}


      return (
        <div className="previous-searches section">
          <h2>Previous Searches</h2>
          <div className="previous-searches-container">
            {searches.map((search, index) => (
              <div key={index} style={{ animationDelay: index * 0.1 + "s" }} className="search-item">
                {search}
              </div>
            ))}
          </div>

          {/*value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}  onClick={searchRecipe} */}
          <div className="search-box">
            <input
              type="text"
              placeholder="Search ..."
              
            />
            <button className="btn" >
              <FontAwesomeIcon icon={faSearch} />
            </button>
          </div>
        </div>
      );
}