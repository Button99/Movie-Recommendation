var express= require("express");
var app= express();
var bodyParser= require("body-parser");
var path= require("path");
var file= require("fs");

 var urlencodedParser= bodyParser.urlencoded({extended: true});

// MovieRecommendation.html
app.use(express.static("Website"));
app.get("/", function(req, res) {
  res.sendFile(path.join(__dirname, "../", "MovieRecommendation.html"));
})


// Register
app.get("/Register.html", urlencodedParser, function(req, res) {
  console.log("Redirect to Register.html");
  res.sendFile(path.join(__dirname, "../", "Register.html"));
})

// Register Submit
app.post("/process_post", urlencodedParser, function(req, res) {
  response= {
    Username: req.body.userName,
    Password: req.body.psw
  };
  /*fs.write("Register.txt", Username+ " "+ Password, function(err) {
    if(err) throw err;
    console.log("File Created!"); */
    res.end(JSON.stringify(response));
//  });
})

// LogIn
app.get("/Login.html", urlencodedParser,  function(req, res) {
  console.log("Redirect to Login.html");
  res.sendFile(path.join(__dirname, "../", "Login.html"));
})

var server= app.listen(8080, function() {
  var host= server.address().address
  var port= server.address().port

  console.log("App listening: %s, %s", host, port)
})
