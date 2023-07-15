import CustomImage from "./CustomImage"
import { Link } from 'react-router-dom';

export default function RecipeCard({recipe}){
    return (
        <div className="recipe-card">
            <CustomImage imgSrc={recipe.imageurl} pt="65%"/>
            <div className="recipe-card-info">
                {/*
                <img className="auther-img" src={recipe.authorImg} alt="recipe-img"/>
    */}
                <p className="recipe-title">{recipe.recipename}</p>
                {/*<a className="view-btn"  href="./Recipedetail">VIEW RECIPE</a>*/}
                <Link to={`/Recipedetail/${recipe.recipename}`} className="view-btn">VIEW RECIPE</Link>
            </div>
        </div>
    )
}