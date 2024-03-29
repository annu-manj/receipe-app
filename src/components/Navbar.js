import { Link, useLocation } from "react-router-dom"

import { useState } from "react"
import Sidebar from "./Sidebar"

import { faHome, faList, faCog, faUserCircle,  faCircleHalfStroke } from "@fortawesome/free-solid-svg-icons"

export default function Navbar(){
    const [showSidebar, setShowSidebar] = useState(false)
    const location = useLocation()
    const links = [
        {
            name: "Home",
            path: "/",
            icon: faHome
        },
        {
            name: "Recipes",
            path: "/recipes",
            icon: faList
        },
        {
            name: "Login",
            path: "/login",
            icon: faUserCircle
        },
        {
            name: "Settings",
            path: "/settings",
            icon: faCog
        },
        
        {
          name: "More",
          path: "/more",
          icon: faCircleHalfStroke
        }
    ]

    function closeSidebar(){
        setShowSidebar(false)
    }

    window.onload = function() {
        var emoji = document.querySelector('.emoji');
        emoji.style.animation = 'emojiAnimation 0.6s linear';
      }
    return (
        <>
            <div className="navbar container">
                <Link to="/" className="logo">F<span class="emoji">oo</span>dCourt</Link>
                <div className="nav-links">
                    { links.map(link => (
                        <Link className={location.pathname === link.path ? "active" : ""} to={link.path} key={link.name}>{link.name}</Link>
                    )) }
                </div>
                <div onClick={() => setShowSidebar(true)} className={showSidebar ? "sidebar-btn active" : "sidebar-btn"}>
                    <div className="bar"></div>
                    <div className="bar"></div>
                    <div className="bar"></div>
                    <div className="bar"></div>
                </div>
            </div>
            { showSidebar && <Sidebar close={closeSidebar} links={links} /> }
            
        </>
        
    )
}