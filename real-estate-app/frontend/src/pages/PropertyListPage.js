import React from 'react';
import PropertyCard from '../components/PropertyCard';

const PropertyListPage = () => {
    // Fetch properties from API or use dummy data
    const properties = [
        { title: 'Modern Villa', description: 'A modern villa with a pool', price: 800000 },
        { title: 'Country Cottage', description: 'A cozy country cottage', price: 300000 },
    ];

    return (
        <div>
            <h1>Property Listings</h1>
            <div>
                {properties.map((property, index) => (
                    <PropertyCard key={index} property={property} />
                ))}
            </div>
        </div>
    );
};

export default PropertyListPage;
