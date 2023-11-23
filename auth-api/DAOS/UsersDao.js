var MongoClient = require('mongodb').MongoClient;

// Connection URI
const uri ="mongodb://localhost:27017/";

// Funcion para insertar un usuario en la BD
exports.insert = function (userInfo){
    MongoClient.connect (uri, function (err, db) {
        if (err) throw err; 
        var dbo = db.db("OAUTH");
        dbo.collection("Users").insertOne(userInfo, function(err, res) {
            err ? console.log("[Error] User not inserted" + err) : console.log("[+] User inserted") ;
            db.close();
            console.log("Se inserta");

        });
    });
}


// Funcion que busca un usuario en la BD en base a su ID.
exports.findOne = function(userId){
    return new Promise(function(resolve, reject) {
      if (userId.length > 0) {
        MongoClient.connect (uri, function(err, db){
          console.log("el usuario se busca");

          if (err) throw err; 
          var dbo = db.db("OAUTH");
          dbo.collection("Users").findOne({_id: userId}).then(result => {
              if(result) {
                return resolve(result);
                
              } else {
                return resolve();
              }
          });        
        });
      } else {
        return resolve();
      }
    })
    
}