import React, { Component } from 'react'
import Navbar1 from "./Components/Navbar"
import  CardList from "./Components/CardList"
import data from './Data'
export default class App extends Component {
  render() {
    return (
      <div>
        <Navbar1 />
        <CardList data={data}/>
      </div>
    )
  }
}




