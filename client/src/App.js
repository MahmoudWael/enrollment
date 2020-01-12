import React from 'react';
import logo from './logo.svg';
import './App.css';
import Nanodegree from './components/Nanodegree';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <Nanodegree/>      
      </header>
    </div>
  );
}

export default App;
