import React from 'react'
import './Nav.css'
import { Link } from 'react-router-dom'
import { Twirl as Hamburger } from 'hamburger-react'
import { useState } from 'react'




const Nav = () => {
    const [isOpen, setOpen] = useState(false)

    const handleBurger = () => {
        const nav = document.querySelector('nav')
       nav.classList.toggle('active')
    }

    const closeMobile = () => {
        setOpen(false)
        document.querySelector('nav').classList.remove('active')
    }

    return (
        
        <nav>
            <Link to='/'>
                <h1 onClick={closeMobile}>Greenward</h1>
            </Link>
            <ul>
              
                <Link to='/login'><li>Login</li></Link>
                <Link to='/Favorites'><li>Favorites</li></Link>
                <Link to='/Explore'><li>Explore</li></Link>
               
             </ul>
            {isOpen ? <div className='hamburger-menu hamburger-container'>
                <ul>
                    <Link to='/login'><li onClick={closeMobile}>Login</li></Link>
                    
                    <Link to='/Favorites'><li onClick={closeMobile}>Favorites</li></Link>
                    <Link to='/Explore'><li onClick={closeMobile}>Explore</li></Link>
                </ul>
            </div> : null}
            <div onClick={handleBurger} className='hamburger-container'>
                <Hamburger toggled={isOpen} toggle={setOpen} duration={0.2} />
            </div>
        </nav>
    )
}

export default Nav
