import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faFacebook, faTwitter, faInstagram } from "@fortawesome/free-brands-svg-icons"
import { faEnvelopeSquare, faMapLocation, faPhone } from "@fortawesome/free-solid-svg-icons"



export default function Footer(){
    return (
        <div className="footer container">
            <div className="footer-section">
                <p className="title">Foodcourt.com</p>
                <p>Foodcourt is a place where you can please your soul and tummy with delicious food recepies of all cuisine. And our service is absolutely free.</p>
                <p>&copy; 2023 | All Rights Reserved</p>
            </div>
            <div className="footer-section">
                <p className="title">Contact Us</p>
                <p><FontAwesomeIcon icon={faEnvelopeSquare} /> foodcourt@gmail.com</p>
                <p><FontAwesomeIcon icon={faPhone} /> +91-9632587410</p>
                <p><FontAwesomeIcon icon={faMapLocation} /> Guindy</p>
            </div>
            <div className="footer-section">
                <p className="title">Social-Media</p>
                <p><FontAwesomeIcon icon={faFacebook} /> Facebook</p>
                <p><FontAwesomeIcon icon={faTwitter} /> Twitter</p>
                <p><FontAwesomeIcon icon={faInstagram} /> Instagram</p>
            
                    
                    
            </div>
        </div>
    )
}