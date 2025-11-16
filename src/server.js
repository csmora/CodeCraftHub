require('dotenv').config();
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const userRoutes = require('./routes/userRoutes');
const errorHandler = require('./utils/errorHandler');
const connectDB = require('./config/db');
const initServer = () => {
    const app = express();
    app.use(cors());
    app.use(bodyParser.json());
    return app;
};
// module.exports = initServer;

// const initServer = require('./server.js'); // path to your file
const app = initServer();
connectDB();
app.use('/api/users', userRoutes);
app.use(errorHandler);
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));