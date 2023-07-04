
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faEnvelope,  faKey, faPersonCircleCheck, faArrowCircleRight } from "@fortawesome/free-solid-svg-icons"
import React, { useState } from "react";
import axios from 'axios';
import {useNavigate} from "react-router-dom";
import { Navigate } from "react-router-dom";


export default function Signin(){
    const [email,setEmail] = useState('');
    const [fullname,setFullname] = useState('');
    const [password,setPassword] = useState('');
    const [confirm_password,setConfirmPassword] = useState('');
   
    const navigate = useNavigate();
     
    const registerUser = () => {
        if(email.length === 0){
          alert("Email has left Blank!");
        }
        else if(password.length === 0){
          alert("password has left Blank!");
        }
        else{
            axios.post('http://127.0.0.1:5000/signup', {
                email: email,
                password: password,
                fullname:fullname,
                confirm_password:confirm_password
            })
            .then(function (response) {
                console.log(response);
                //console.log(response.data);
                navigate("/");
            })
            .catch(function (error) {
                console.log(error, 'error');
                if (error.response.status === 401) {
                    alert("Invalid credentials");
                }
            });
        }
    }
    
  
  
    return (
        <div className="log-container">
         <center>
            <h2> <u>Sign In Page</u></h2><br></br>
            <hr></hr>
            <br></br>
            <form className="login-form">
            <div className="search-box">
            <FontAwesomeIcon className="icon" icon={faPersonCircleCheck} />
            <input type="text" name="name" value={fullname} onChange={(e) => setFullname(e.target.value)} placeholder="Enter your FullName.." required/><br></br><br></br>
            </div>
            <div className="search-box">
            <FontAwesomeIcon className="icon" icon={faEnvelope} />
            <input type="email" name="mail" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Enter your mail.." required/><br></br><br></br>
            </div>
            <div className="search-box">
            <FontAwesomeIcon className="icon" icon={faKey} />
            <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Enter your password.." required /><br></br><br></br>
            </div>
            <FontAwesomeIcon className="icon" icon={faKey} />
            <input type="password" name="confrim_password" value={confirm_password} onChange={(e) => setConfirmPassword(e.target.value)} placeholder="Renter your password.." required /><br></br><br></br>
            <button className="btn" type="submit" onClick={registerUser}> Sign In  <FontAwesomeIcon icon={faArrowCircleRight} /></button><br></br><br></br>
            </form>
           
         </center>
        </div>
    )
}