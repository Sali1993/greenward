import './App.css';
import React from 'react'
// import Hero from './components/Hero/Hero';
import Nav from './components/Nav/Nav';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Footer from './components/Footer/Footer';
import Home from './components/Home/Home';
import Explore from './components/Explore/Explore';
import Favorites from './components/Favorites/Favorites';
import Switch from 'react-bootstrap/esm/Switch';
function App() {

  return (
      <Router className="App">
        <Nav />
        <Switch>
        <Route path='/' exact component={Home}/>
        <Route path='/Favroites' exact component={Favorites}/>
        <Route path='/Explore' exact component={Explore}/>
        </Switch>
        <Footer />
      </Router>
  );
}

export default App;
