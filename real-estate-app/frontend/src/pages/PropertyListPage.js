import React, { useState, useEffect } from 'react';
import PropertyCard from '../components/PropertyCard';
import FilterBar from '../components/FilterBar';
import propertyService from '../services/propertyService';

const PropertyListPage = () => {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    const fetchProperties = async () => {
      const data = await propertyService.getProperties();
      setProperties(data);
    };
    fetchProperties();
  }, []);

  return (
    <div>
      <h1>Property Listings</h1>
      <FilterBar />
      <div>
        {properties.map((property) => (
          <PropertyCard key={property._id} property={property} />
        ))}
      </div>
    </div>
  );
};

export default PropertyListPage;
