import React, { useEffect, useState } from 'react';
import API from '../services/api';

const Dashboard = () => {
    const [financialData, setFinancialData] = useState(null);

    useEffect(() => {
        API.get('financial-health/')
            .then((response) => {
                setFinancialData(response.data);
            })
            .catch((error) => {
                console.error('Error fetching financial data:', error);
            });
    }, []);

    if (!financialData) return <p>Loading...</p>;

    return (
        <div>
            <h1>Dashboard</h1>
            <h2>Financial Health Summary</h2>
            <p>Income: {financialData.income}</p>
            <p>Expenses: {financialData.expenses}</p>
            <p>Savings: {financialData.savings}</p>
            <p>Goals: {financialData.goals}</p>
            <p>Score: {financialData.score}</p>
        </div>
    );
};

export default Dashboard;
