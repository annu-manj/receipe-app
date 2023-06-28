
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faEnvelope,  faKey, faPersonCircleCheck, faArrowCircleRight } from "@fortawesome/free-solid-svg-icons"


export default function Signin(){
  
  
    return (
        <div className="log-container">
         <center>
            <h2> <u>Sign In Page</u></h2><br></br>
            <hr></hr>
            <br></br>
            <form className="login-form">
            <div className="search-box">
            <FontAwesomeIcon className="icon" icon={faPersonCircleCheck} />
            <input type="text" name="name" placeholder="Enter your Username.." required/><br></br><br></br>
            </div>
            <div className="search-box">
            <FontAwesomeIcon className="icon" icon={faEnvelope} />
            <input type="email" name="mail" placeholder="Enter your mail.." required/><br></br><br></br>
            </div>
            <div className="search-box">
            <FontAwesomeIcon className="icon" icon={faKey} />
            <input type="password" name="password" placeholder="Enter your password.." required /><br></br><br></br>
            </div>
            <FontAwesomeIcon className="icon" icon={faKey} />
            <input type="password" name="password2" placeholder="Renter your password.." required /><br></br><br></br>
            <button className="btn" type="submit"> Sign In  <FontAwesomeIcon icon={faArrowCircleRight} /></button><br></br><br></br>
            </form>
           
         </center>
        </div>
    )
}