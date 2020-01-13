import React, { Component } from 'react'
import axios from 'axios'
import Degrees from './Degrees'
import Header from './Header';

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
                const enrollments = response.data.enrollment
                this.setState({enrollments})
            })
            .catch(err => console.log(err))
    }   

    render() {
        return(
            <div>
                <Header enrollments={this.state.enrollments}/>
               {this.state.degrees.map(d =>{ return (d.available && d.open_for_enrollment)? 
                 <div key={d.key}> 
                    <Degrees img={d.image} title={d.title} disc={d.short_summary} degrees={this.state.degrees} nano_key={d.key} 
                        enrollments={this.state.enrollments}/>
                </div> : "" })}
            </div>
        )
    }
}

export default Nanodegree
