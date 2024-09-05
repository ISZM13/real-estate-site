import React from 'react';
import PropertyCard from '../components/PropertyCard';
import FilterBar from '../components/FilterBar';

const HomePage = () => {
    const properties = [
        { title: 'Beautiful House', description: 'A beautiful house in the city', price: 500000 },
        { title: 'Luxury Apartment', description: 'A luxury apartment with great views', price: 750000 },
    ];

    return (
        <div>
            <h1>Welcome to Real Estate App</h1>
            <FilterBar />
            <div>
                {properties.map((property, index) => (
                    <PropertyCard key={index} property={property} />
                ))}
            </div>
        </div>
    );
};

export default HomePage;
