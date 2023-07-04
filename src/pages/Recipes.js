import PreviousSearches from "../components/PreviousSearches"
import RecipeCard from "../components/RecipeCard"
import React, { useState } from "react";
import { useEffect } from "react";
import axios from 'axios';
import {useNavigate} from "react-router-dom";


export default function Recipes(){
    const [recipes, setRecipes] = useState([{}]);

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/recipes')
          .then(function (response) {
            console.log(response);
            setRecipes(response.data);
          })
          .catch(function (error) {
            console.log(error);
          });
      }, []);


   /* [
        {
            id: 1,
            title: "Chicken Pan Pizza",
            image: "/img/gallery/img_1.jpg",
            authorImg: "/img/top-chiefs/img_1.jpg",
        }, 
        
        {
            id: 2,
            title: "American Cheese Burger",
            image: "/img/gallery/img_5.jpg",
            authorImg: "/img/top-chiefs/img_3.jpg",
        },
        {
            id:3,
            title: "Mutton Biriyani",
            image: "/img/gallery/img_6.jpg",
            authorImg: "/img/top-chiefs/img_5.jpg",
        },
        {
            id:4,
            title: "Japanese Sushi",
            image: "/img/gallery/img_10.jpg",
            authorImg: "/img/top-chiefs/img_6.jpg",
        },
        
        {
            id:5,
            title: "Spaghetti and Meatballs",
            image: "/img/gallery/img_4.jpg",
            authorImg: "/img/top-chiefs/img_2.jpg",
        },
        {
            id: 6,
            title: "American Cheese Burger",
            image: "/img/gallery/img_5.jpg",
            authorImg: "/img/top-chiefs/img_3.jpg",
        },
       
       
      
    ].sort(() => Math.random() - 0.5)  */

    return (
        <div>
            <PreviousSearches />
            <div className="recipes-container">
                {/* <RecipeCard /> */}
                {recipes.map((recipe, index) => (
                    <RecipeCard key={index} recipe={recipe} />
                ))}
            </div>
        </div>
    )
}