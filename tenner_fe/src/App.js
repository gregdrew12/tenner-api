import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import React, { Component, Fragment } from 'react';
import Header from './components/Header';
import {Login} from './components/Login';
import {Register} from './components/Register';
import Logout from './components/Logout';
import Home from './components/Home';

function App() {
  return (
    <BrowserRouter>
      <Header></Header>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/logout' element={<Logout/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;