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
    const NavigateSigin = () =>
    {
     
     window.location.href = "/signin"; 

    }
  return (
    <div>
        <div className="log-container">
              </div>
                <form> 
                    <p className="lead fw-normal mb-0 me-3">Log Into Your Account</p>
                    <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} id="form3Example3" className="form-control form-control-lg" placeholder="Enter a valid email address" />
                    <label className="form-label" for="form3Example3">Email address</label>
                        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} id="form3Example4" className="form-control form-control-lg" placeholder="Enter password" />
                        <label className="form-label" for="form3Example4">Password</label>
                        <input className="form-check-input me-2" type="checkbox" value="" id="form2Example3" />
                        <label className="form-check-label" for="form2Example3">
                        Remember me
                      </label>
                    <a href="#!" className="text-body">Forgot password?</a>

                    <button type="button" className="btn btn-primary btn-lg" onClick={logInUser} >Login</button>
                    <br></br>
    

                    
 
                </form>
            <button className="btn" onClick={NavigateSigin}> Sign Up </button><br></br>
                
            </div>
  );
}