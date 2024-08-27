const mongoose = require('mongoose');

const propertySchema = new mongoose.Schema({
  title: String,
  description: String,
  price: Number,
  location: String,
  images: [String],
  type: String,
  bedrooms: Number,
  bathrooms: Number,
  squareFeet: Number,
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
  },
});

const Property = mongoose.model('Property', propertySchema);

module.exports = Property;
