import React from 'react';
import {BrowserRouter as Router,Routes, Route} from 'react-router-dom';
import Dashboard from './components/Dashboard';
const App = () => {
    return (
        <Router>

            <Routes>
                <Route path="/dashboard" component={Dashboard} />
                {/* Add other routes as needed */}

            </Routes>
        </Router>

    );
};

export default App;
