import React from 'react';

const PropertyCard = ({ property }) => {
  return (
    <div>
      <h3>{property.title}</h3>
      <p>{property.description}</p>
      <p>Price: ${property.price}</p>
    </div>
  );
};

export default PropertyCard;
