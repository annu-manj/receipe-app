
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faArrowCircleRight, faEnvelope,  faKey } from "@fortawesome/free-solid-svg-icons"

import { Navigate } from "react-router-dom"

export default function Login(){
    const NavigateSigin = () => {
        
        window.location.href = "/signin"; 

    };
  
    return (
        <div>
         
            <div className="log-container">
            <center>
            <h2> <u>Login Page</u></h2><br></br>
            <hr></hr>
            <br></br>
            
            <form className="login-form">
               
            <FontAwesomeIcon className="icon" icon={faEnvelope} />  
            <input type="email" name="mail" placeholder="Enter your mail.." required/><br></br><br></br>
            <FontAwesomeIcon className="icon" icon={faKey} />
            <input type="password" name="password" placeholder="Enter your password.." required /><br></br><br></br>
            <button className="btn" type="submit">Login  <FontAwesomeIcon icon={faArrowCircleRight} /></button><br></br><br></br>
            </form>
            
            <h4> Forgot password?<a href="#"> Click Here</a></h4><br></br>
            <h4>Or</h4><br></br>
            <button className="btn" onClick={NavigateSigin}>Sign Up  <FontAwesomeIcon icon={faArrowCircleRight} /></button><br></br>
            <br></br><hr></hr>
            </center>
            </div>
           
        </div>
    )
}