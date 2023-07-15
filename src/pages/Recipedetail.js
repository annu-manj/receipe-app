import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBarsProgress, faBowlFood, faCarrot, faCartShopping, faClockFour, faCocktail, faPlateWheat } from "@fortawesome/free-solid-svg-icons";
import { useEffect, useState } from "react";
import { useParams } from 'react-router-dom';
import axios from 'axios';

export default function Recipedetail() {
  const [recipeData, setRecipeData] = useState([]);
  const { recipename } = useParams(); // Retrieve recipename from URL parameter

  useEffect(() => {
    // Function to fetch recipe details from the API
    const fetchRecipeDetails = async () => {
      try {
        const response = await axios.get('http://localhost:5000/viewdetails', {
          params: {
            recipename: recipename
          }
        });
        console.log(response.data); 
        setRecipeData(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchRecipeDetails();
  }, [recipename]);

  return (
    <>
      {recipeData.map((recipe) => (
        <div key={recipe.recipeid}>
          <h1>{recipe.recipename}</h1><br></br><hr></hr><br></br>
          <center>
            <div className="img_container">
              <img src={recipe.imageurl} className="rec_img" alt="recipe-img" /><br></br><br></br><hr></hr><br></br>
            </div>
          </center>

          <h3><FontAwesomeIcon className="icon" icon={faClockFour} />Total timing:{recipe.totaltimeinmins}</h3><br></br><hr></hr><br></br>
          <h3><FontAwesomeIcon className="icon" icon={faCocktail} />Cuisine:{recipe.cuisine}</h3><br></br><hr></hr><br></br>
          <h3><FontAwesomeIcon className="icon" icon={faBowlFood} />Course:{recipe.course}</h3><br></br><hr></hr><br></br>
          <h3><FontAwesomeIcon className="icon" icon={faCarrot} />Diet:{recipe.diet}</h3><br></br><hr></hr><br></br>
          <h3><FontAwesomeIcon className="icon" icon={faPlateWheat} />No. of Servings:{recipe.servings}</h3><br></br><hr></hr><br></br>
          <h3><FontAwesomeIcon className="icon" icon={faCartShopping} />Ingredients</h3><br></br><p>{recipe.ingredients}</p><hr className="custom-hr"></hr><br></br>
          
          <h3><FontAwesomeIcon className="icon" icon={faBarsProgress} />Instruction</h3><br></br>
          {recipe.instructions}
        </div>
      ))}
    </>
  );
}

