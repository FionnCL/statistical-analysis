import React from 'react'
import './Navbar.css'

export default function Navbar(){
    return(
        <nav className='navbar'>
            <div className='navbar-text'>
                <h1 className='navbar-text-title'>Statistical Analysis Calculator</h1>
                <p className='navbar-text-subtext'>By FionnCL</p>
            </div>
            <div className='social-block'>
                <a href='https://fionncl.web.app'><h3>Other Projects</h3></a>
            </div>
        </nav>
    );
}