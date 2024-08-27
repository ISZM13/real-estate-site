const Property = require('../models/propertyModel');

// Get all properties
exports.getProperties = async (req, res) => {
  try {
    const properties = await Property.find().populate('user', 'name email');
    res.status(200).json(properties);
  } catch (error) {
    res.status(500).json({ message: 'Something went wrong' });
  }
};

// Get single property
exports.getProperty = async (req, res) => {
  try {
    const property = await Property.findById(req.params.id).populate('user', 'name email');
    res.status(200).json(property);
  } catch (error) {
    res.status(500).json({ message: 'Something went wrong' });
  }
};

// Create new property
exports.createProperty = async (req, res) => {
  const { title, description, price, location, type, bedrooms, bathrooms, squareFeet } = req.body;

  try {
    const property = await Property.create({
      title,
      description,
      price,
      location,
      type,
      bedrooms,
      bathrooms,
      squareFeet,
      user: req.user.id,
    });

    res.status(201).json(property);
  } catch (error) {
    res.status(500).json({ message: 'Something went wrong' });
  }
};

// Delete property
exports.deleteProperty = async (req, res) => {
  try {
    await Property.findByIdAndDelete(req.params.id);
    res.status(200).json({ message: 'Property deleted successfully' });
  } catch (error) {
    res.status(500).json({ message: 'Something went wrong' });
  }
};
