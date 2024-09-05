import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import PropertyListPage from './pages/PropertyListPage';
import UserProfilePage from './pages/UserProfilePage';
import './assets/styles.css';

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/properties" element={<PropertyListPage />} />
                <Route path="/profile" element={<UserProfilePage />} />
            </Routes>
        </Router>
    );
}

export default App;
