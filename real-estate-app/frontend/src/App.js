import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from '../pages/HomePage';
import PropertyListPage from '../pages/PropertyListPage';
import UserProfilePage from '../pages/UserProfilePage';
import Navbar from '../components/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/properties" component={PropertyListPage} />
        <Route path="/profile" component={UserProfilePage} />
      </Switch>
    </Router>
  );
}

export default App;
