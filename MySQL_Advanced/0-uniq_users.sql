-- SQL script to create a 'users' table with safety checks and wide DB compatibility

-- Check if table exists and create only if it doesn't

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
