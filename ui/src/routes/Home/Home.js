import React from 'react';

import './Home.css'

const Home = ({value, onChange, onSubmit}) => 
  <div className="home">
    <div className="search-bar">
      <input 
        type="text" 
        className="search-bar-input" 
        placeholder="Artists, Songs, or Podcasts" 
        onChange={onChange}
        value={value}
      />
      <button 
        className="search-btn"
        onClick={onSubmit} 
      >
        <i className="fas fa-search"></i>      
      </button>
    </div>
  </div>  

export default Home;
