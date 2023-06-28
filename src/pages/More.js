
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faEnvelopeSquare,  faMapMarkedAlt, faMobileAlt } from "@fortawesome/free-solid-svg-icons"


export default function more(){
  
  
    return (
        
         <center>
            <h2>About Us</h2>
            <br></br>
            <br></br>
            <h4>Foodcourt is a place where you can please your soul and tummy with delicious food recepies of all cuisine.<br>
            </br> And our service is absolutely free.
            </h4>
            <br></br>
            <br></br>
            <hr></hr>
            <br></br>
            <br></br>
            <h2>Contact Us </h2>
            <br></br>
            <br></br>
            <h4><FontAwesomeIcon icon={faEnvelopeSquare}/>  MailID : foodcourt@gmail.com</h4>
            <h4><FontAwesomeIcon icon={faMobileAlt}/>  Phone NUmber : +91-9632587410</h4>
            <h4><FontAwesomeIcon icon={faMapMarkedAlt}/>  Address : Guindy</h4>
            <br></br>
            <br></br>
           <hr></hr>
           <br></br>
           <br></br>
           <h2>Feedback</h2>
           <br></br>
           <br></br>
           <form>
           <input type="textarea" placeholder="Share your thoughts about us...."/>
           <br></br>
           <br></br>
           <button className="btn" type="submit">Submit</button>
           </form>
           <br></br>
         </center>
        
    )
}