import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faBarsProgress, faBookOpen,  faBowlFood, faCarrot, faCartShopping, faClockFour, faCocktail,  faPlateWheat } from "@fortawesome/free-solid-svg-icons"





export default function Recipedetail({recipe}){
    return (
        <div >
        <h1>Recipe Title</h1><br></br><hr></hr><br></br>
        <center>
        <div class="img_container">
        <img src="/img/gallery/img_4.jpg" className="rec_img" alt="recipe-img" /><br></br><br></br><hr></hr><br></br>
        </div>
        </center>
        <h2><FontAwesomeIcon className="icon" icon={faBookOpen} />Recipe Descirption</h2><br></br><hr></hr><br></br>
        <h3><FontAwesomeIcon className="icon" icon={faClockFour} />Total timing</h3><br></br><hr></hr><br></br>
        <h3><FontAwesomeIcon className="icon" icon={faCocktail} />Cuisine</h3><br></br><hr></hr><br></br>
        <h3><FontAwesomeIcon className="icon" icon={faBowlFood} />Course</h3><br></br><hr></hr><br></br>
        <h3><FontAwesomeIcon className="icon" icon={faCarrot} />Diet</h3><br></br><hr></hr><br></br>
        <h3><FontAwesomeIcon className="icon" icon={faPlateWheat} />No. of Servings</h3><br></br><hr></hr><br></br>
        <h3><FontAwesomeIcon className="icon" icon={faCartShopping} />Ingredients</h3><br></br><hr class="custom-hr"></hr><br></br>
        <h3><FontAwesomeIcon className="icon" icon={faBarsProgress} />Steps</h3>


        </div>
    )
    }
