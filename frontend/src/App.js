import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      hello: 'Hello from React',
    };
  }


  componentDidMount() {
    // Fetch the "Hello, World" message from the Python back-end
    fetch('http://localhost:5000/api/message')
      .then((response) => response.json())
      .then((data) => {
        this.setState({ hello: data.message });
      })
      .catch((error) => {
        console.error('Error fetching message:', error);
      });
  }

  render() {
    return (
      <div className="App">
        <h1>{this.state.hello}</h1>
      </div>
    );
  }
}

export default App;
