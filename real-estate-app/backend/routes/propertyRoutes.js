const express = require('express');
const { getProperties, getProperty, createProperty, deleteProperty } = require('../controllers/propertyController');
const auth = require('../middleware/authMiddleware');

const router = express.Router();

router.get('/', getProperties);
router.get('/:id', getProperty);
router.post('/', auth, createProperty);
router.delete('/:id', auth, deleteProperty);

module.exports = router;
