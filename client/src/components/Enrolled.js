import React, { Component } from 'react'
import './Enrolled.css'
import axios from 'axios'

export class Enrolled extends Component {
    constructor(props){
        super(props)
        this.state = {
            buttonMessage: "Enroll"
        }
    }

    enrollHandelr(key){
        axios({ 
                method: 'POST',
                url: 'http://localhost:5000/enroll/',
                headers: { 'Content-Type': 'application/json' },
                data: { nanodegree_key: key, status: 'ENROLLED' }
        })
        .then(() => this.setState({buttonMessage: "Thank you for Enrollment"}))
        .catch(err => console.log(err))

    }

    render() {
        const imgStyle = {width:"25vw", height:"auto"}
        return (
            <div className="card">
                <img src={this.props.img} alt="Avatar" style={imgStyle}/>
                <div className="container">
                    <h4><b>{this.props.title}</b></h4>
                    <p>{this.props.disc}</p>
                   { 
                       this.props.enrollments.every(e => e.nanodegree_key !== this.props.nano_key)? 
                       <button className={'button'} onClick={() => this.enrollHandelr(this.props.nano_key)}>{this.state.buttonMessage}</button> : '' 
                    }
                </div>
            </div>
        )
    }
}

export default Enrolled