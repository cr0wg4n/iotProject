import React, { Component } from 'react'
import {
  Route,
  BrowserRouter as Router,
  Link,
  Redirect,
  Switch
} from 'react-router-dom'
import 'semantic-ui-css/semantic.min.css';
import Home from './pages/Home'
import Login from './pages/Login'
import {sendGET} from './helpers/methods'
const hostname = 'http://localhost:3000'
class App extends Component {
  constructor (...props) {
    super (...props)

    this.state = {
      authed: false,
      user: null
    }
    
    this.modifiedState = this.modifiedState.bind(true)
  }

  componentDidMount () {
    sendGET(`${hostname}/user`)
      .then((data) => {
        this.setState({
          authed: true,
          user: data.user
        })
      })
      .catch(() => {
        this.setState({authed: false})
      })
  }

  modifiedState (data) {
    this.setState({data})
  }
  
  

  render() {
    return (
      <Router>
        <div>
          {
            (this.state.authed === true)
            ?
              <Redirect  to="/" />
            :
              <Redirect  to="/login" />
          }
          <Switch>
            <PrivateRoute component={Login} mofifieState={this.modifiedState} path='/login'  />
            <PrivateRoute  component={Home} mofifieState={this.modifiedState} path='/'  />
          </Switch>
        </div>
      </Router>
    )
  }
}

const PrivateRoute = ({component: Component, ...rest}) => (
  <Route
    {...rest}
    render={
      props => <Component {...props} {...rest} />
    }
  />
)


export default App
