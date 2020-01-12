import React, { PureComponent } from 'react'
import './Header.css'

export class Header extends PureComponent {

    render() {
        return (
                <div className="card1">
                    <div className="container1">
                        <span className={"title"}>Nanodegrees Enrollment</span>
                        <span className={"span"}>Enrolled at: <span className={"span-colored"}>{this.props.enrollments.length}</span> degrees</span>
                        <div className={"clear"}></div>
                    </div>
                </div>
        )
    }
}

export default Header   