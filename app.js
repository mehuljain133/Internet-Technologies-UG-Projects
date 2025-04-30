/* Develop an interactive website using jquery, JSON, NODE.js and BOOTSTRAP with
following functionalities.
1. Design a home page and other allied pages of the website using HTML and CSS
2. Create a registration form and insert the data into tables at the backend. Creating an html
form with content validation using JavaScript.
3. Handle HTML form using jQuery, store the data in JSON objects, pass them to another
page and display it there using jQuery
4. Logging system to manage various types of accounts
5. Create pages with dynamic content fetching and display
6. Perform event handling in node.js
*/

#!/usr/bin/env node

// Required packages
const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcryptjs');
const session = require('express-session');
const mongoose = require('mongoose');
const app = express();

// MongoDB connection setup (Make sure MongoDB is running)
mongoose.connect('mongodb://localhost:27017/websiteDB', { useNewUrlParser: true, useUnifiedTopology: true });

// User schema and model
const userSchema = new mongoose.Schema({
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
    role: { type: String, default: 'user' }, // 'admin' or 'user'
    logs: [{ action: String, timestamp: { type: Date, default: Date.now } }] // Simple logging system
});

const User = mongoose.model('User', userSchema);

// Middleware setup
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'ejs');
app.use(session({
    secret: 'secret-key',
    resave: false,
    saveUninitialized: true,
}));

// Home Page - Display registered users
app.get('/', (req, res) => {
    User.find({}, (err, users) => {
        if (err) {
            console.log(err);
            res.status(500).send('Error fetching users');
        } else {
            res.render('index', { users });
        }
    });
});

// Registration Page
app.get('/register', (req, res) => {
    res.render('register');
});

// Handle Registration Form
app.post('/register', async (req, res) => {
    const { username, email, password } = req.body;

    // Basic validation
    if (!username || !email || !password) {
        return res.status(400).send('All fields are required.');
    }

    // Hash the password before saving to DB
    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = new User({ username, email, password: hashedPassword });

    newUser.save((err) => {
        if (err) {
            console.log(err);
            res.status(500).send('Error saving user');
        } else {
            res.redirect('/');
        }
    });
});

// Login Page
app.get('/login', (req, res) => {
    res.render('login');
});

// Handle Login Form
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    User.findOne({ username }, async (err, user) => {
        if (err) {
            console.log(err);
            res.status(500).send('Error during login');
        } else if (!user) {
            res.send('No such user found');
        } else {
            const validPassword = await bcrypt.compare(password, user.password);
            if (validPassword) {
                req.session.userId = user._id;
                // Log user login event
                user.logs.push({ action: 'Logged In' });
                user.save();
                res.redirect('/dashboard');
            } else {
                res.send('Invalid password');
            }
        }
    });
});

// Dashboard Page - Only for logged-in users
app.get('/dashboard', (req, res) => {
    if (req.session.userId) {
        User.findById(req.session.userId, (err, user) => {
            if (err) {
                console.log(err);
                res.status(500).send('Error fetching user data');
            } else {
                res.render('dashboard', { user });
            }
        });
    } else {
        res.redirect('/login');
    }
});

// Admin Panel
app.get('/admin', (req, res) => {
    if (req.session.userId) {
        User.findById(req.session.userId, (err, user) => {
            if (err || !user || user.role !== 'admin') {
                res.redirect('/');
            } else {
                User.find({}, (err, users) => {
                    res.render('admin', { users });
                });
            }
        });
    } else {
        res.redirect('/login');
    }
});

// Logout User
app.get('/logout', (req, res) => {
    req.session.destroy((err) => {
        if (err) {
            console.log(err);
        }
        res.redirect('/');
    });
});

// Start the server
app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});

// EJS Templates (HTML content)

// Index Page (home page showing users)
app.get('/views/index.ejs', (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Welcome to the Home Page</h1>
        <h2>Registered Users:</h2>
        <ul>
            <% users.forEach(function(user) { %>
                <li><%= user.username %> - <%= user.email %></li>
            <% }) %>
        </ul>
        <a href="/register" class="btn btn-primary">Register</a>
        <a href="/login" class="btn btn-success">Login</a>
    </div>
</body>
</html>
    `);
});

// Register Page (registration form)
app.get('/views/register.ejs', (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $('form').on('submit', function(e) {
                var username = $('#username').val();
                var email = $('#email').val();
                var password = $('#password').val();
                
                if (!username || !email || !password) {
                    alert('All fields are required!');
                    e.preventDefault();
                }
            });
        });
    </script>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Registration Form</h1>
        <form action="/register" method="POST">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" name="password" required>
            </div>
            <button type="submit" class="btn btn-primary">Register</button>
        </form>
    </div>
</body>
</html>
    `);
});

// Login Page (login form)
app.get('/views/login.ejs', (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Login</h1>
        <form action="/login" method="POST">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" name="password" required>
            </div>
            <button type="submit" class="btn btn-success">Login</button>
        </form>
    </div>
</body>
</html>
    `);
});

// Dashboard Page (for logged-in users)
app.get('/views/dashboard.ejs', (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Dashboard</h1>
        <p>Welcome, <%= user.username %>! You are logged in.</p>
        <a href="/logout" class="btn btn-danger">Logout</a>
    </div>
</body>
</html>
    `);
});

// Admin Panel
app.get('/views/admin.ejs', (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Admin Panel</h1>
        <h2>User Management</h2>
        <ul>
            <% users.forEach(function(user) { %>
                <li><%= user.username %> - <%= user.email %> - <%= user.role %></li>
            <% }) %>
        </ul>
        <a href="/" class="btn btn-primary">Go to Home</a>
    </div>
</body>
</html>
    `);
});

