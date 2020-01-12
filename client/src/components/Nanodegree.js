import React, { Component } from 'react'
import axios from 'axios'

export class Nanodegree extends Component {
    constructor(props){
        super(props)
        this.state = {
            degrees: [],
            enrollments: []
        }
    }
    componentDidMount(){
        axios.get("https://catalog-api.udacity.com/v1/degrees")
            .then(response => { 
                const degrees = response.data.degrees
                this.setState({degrees})
            })
            .catch(err => console.log(err))

        var config = {
            headers: {'Access-Control-Allow-Origin': '*'}
        };

        axios.get("http://localhost:5000/enroll/", config)
            .then(response => { 
                const enrollments = response.data
                this.setState({enrollments})
            })
            .catch(err => console.log(err))
    }

    enrollHandelr(d){
        console.log(d.key)
    }

    render() {
        return(
            <div>
               {this.state.degrees.map(d =>{ return (d.available && d.open_for_enrollment)? 
                 <div key={d.key}> 
                    <div>{d.slug}</div> 
                    <button onClick={() => this.enrollHandelr(d)}>Enroll</button> 
                </div> : "" })}
            </div>
        )
    }
}

export default Nanodegree
