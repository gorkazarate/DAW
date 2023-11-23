'use strict'
const SERVER_PORT = 9090;
var express = require("express");
var fs = require('fs')
var path = require("path");
const session = require('express-session');
var server = require('./controller/server')


// Initialize APP
var app = express();

// APP Config
app.use(express.static(path.join(__dirname, 'static')));

app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.set('view engine', 'ejs');
app.use(session({
  resave: false,
  saveUninitialized: true,
  secret: 'SECRET' 
}));

// ADD server
app.use(server)

// START APP
app.listen(SERVER_PORT, function () {
    console.log('Your server is listening on port %d (http://localhost:%d)', SERVER_PORT, SERVER_PORT);
    console.log('Swagger-ui is available on http://localhost:%d/api-docs', SERVER_PORT);
});