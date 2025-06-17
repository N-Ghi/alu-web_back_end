-- SQL script to create a 'users' table with safety checks and wide DB compatibility

-- Check if table exists and create only if it doesn't

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(2) NOT NULL DEFAULT 'US',
    CHECK (country IN ('US', 'CO', 'TN'))
);
