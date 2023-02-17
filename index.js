/*jshint esversion: 11 */

// Required modules and constants
const express = require('express');
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const app = express();
const port = 2023;

// Configure the express application instance
app.disable('x-powered-by');
app.set('trust proxy',true); 
var rawBodySaver = function (req, res, buf, encoding) {
  if (buf && buf.length) {
    req.rawBody = buf.toString(encoding || 'utf8');
  }
};
app.use(bodyParser.json({ verify: rawBodySaver, limit:'50mb' }));
app.use(cookieParser());
app.use(bodyParser.urlencoded({ verify: rawBodySaver, extended: true, limit:'50mb' }));
app.use(bodyParser.raw({ verify: rawBodySaver, type: '*/*', limit:'50mb' }));
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');

app.listen(port, '0.0.0.0', () => {
    console.log(`Webserver running on port ${port}.`);
});

app.get('/', (req, res) => {
    if(!req.cookies.theme) req.cookies.theme = 'standard';

    res.render('index.ejs', {theme: req.cookies.theme});
});



// helper functions
function db_connection() {
    return mysql.createConnection({
        host: process.env.DBHOST,
        user: process.env.DBUSER,
        password: process.env.DBPASS,
        database: process.env.DBNAME
    });
}

function execute_query_get_results(sql, callback) {
    var connection = db_connection();
    connection.connect(function(err) {
        if(err) {
            con.end().catch(() => console.log(""));
            return callback({success: false, error: err, message: "Error connecting to database."});
        } else {
            con.query(sql, (err, result) => {
                if(err) {
                    con.end().catch(() => console.log(""));
                    return callback({success: false, error: err, message: "Error executing query."});
                } else {
                    con.end();
                    return callback({success: true, result: result});
                }
            });
        }
    });
}