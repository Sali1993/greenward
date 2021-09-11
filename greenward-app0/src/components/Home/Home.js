import React from 'react'
import './Home.css'

const Home = () => {
    return (
        <div>
            <div className='hero'>
            <h1>Welcome to Greenward</h1>
            <div className='hero-content'>
                <input type="text" className='search' placeholder="where you headed?"/>
                <button type="submit" className='searchBtn'>ENTER</button>
            </div>
            
            </div>
            <div className='exploreBtns'>
                <button className='foodBtn myBtn'>Food</button>
                <button className='shoppingBtn myBtn'>Shopping</button>
                <button className='funBtn myBtn'>Fun</button>
            </div>

          
        </div>
        
        
    )
}

export default Home
