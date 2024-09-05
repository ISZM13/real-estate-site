import React from 'react';
import './PropertyCard.css';

const PropertyCard = ({ property }) => {
    return (
        <div className="property-card">
            <h2>{property.title}</h2>
            <p>{property.description}</p>
            <p><strong>Price:</strong> ${property.price}</p>
            <button>View Details</button>
        </div>
    );
};

export default PropertyCard;
