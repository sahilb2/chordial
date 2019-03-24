import React, { Component, Suspense, lazy } from 'react';


const Home = lazy(() => import('./Home'));

class HomeContainer extends Component {
  constructor(props) {
    super(props);
    this.onChange = this.onChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
    this.state = {
      value: ''
    }
  }
  
  onChange({target: {value}}) {
    this.setState({value});
  }

  onSubmit() {
    // TODO: add api search request here
    console.log(this.state.value)
  }

  render() {
    const {value} = this.state;
    return (
      <div className="home-container">
        <Suspense fallback={<div>Loading...</div>}>
          <Home 
            value={value}
            onChange={this.onChange}
            onSubmit={this.onSubmit}
          />
        </Suspense>
      </div>
    );
  }
}

export default HomeContainer;
