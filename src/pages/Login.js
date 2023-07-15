import React, { useState } from "react";
import axios from 'axios';
import {useNavigate} from "react-router-dom";
import { Navigate } from "react-router-dom";
 
export default function Login(){
    
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');
   
    const navigate = useNavigate();
     
    const logInUser = () => {
        if(email.length === 0){
          alert("Email has left Blank!");
        }
        else if(password.length === 0){
          alert("password has left Blank!");
        }
        else{
            axios.post('http://127.0.0.1:5000/login', {
                email: email,
                password: password
            })
            .then(function (response) {
                console.log(response);
                //console.log(response.data);
                navigate("/Recipes");
            })
            .catch(function (error) {
                console.log(error, 'error');
                if (error.response.status === 401) {
                    alert("Invalid credentials");
                }
            });
        }
    }
    const NavigateSigin = () =>
    {
     
     window.location.href = "/signin"; 

    }
  return (
    
        <div className="log-container">
             <center>
                <form className="login-form"> 
                    <p>Log Into Your Account</p><br></br>
                    <label  for="form3Example3">Email address</label><br></br>
                    <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} id="form3Example3"  placeholder="Enter a valid email address" /><br></br>
                        <label className="form-label" for="form3Example4">Password</label><br></br>
                        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} id="form3Example4"  placeholder="Enter password" /><br></br>
                        <input  type="checkbox" value="" id="form2Example3" />
                        <label className="form-check-label" for="form2Example3">
                        Remember me
                      </label><br></br>
                    <a href="#!" className="text-body">Forgot password?</a><br></br><br></br>

                    <button type="button" className="btn btn-primary btn-lg" onClick={logInUser} >Login</button>
                    <br></br>
    

                    
 
                </form>
            <button className="btn" onClick={NavigateSigin}> Sign Up </button><br></br>
                </center>
            </div>
  );
}