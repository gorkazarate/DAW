//var MongoClient = require('mongodb').MongoClient;

// Connection URI
//const uri ="mongodb://localhost:27017/";

const { MongoClient, ServerApiVersion } = require('mongodb');
// const uri="mongodb://127.0.0.1:27017/conversions";
const uri = "mongodb://localhost:27017?retryWrites=true&w=majority";
var conversionsXML = "";

const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

// Funcion para insertar un usuario en la BD
exports.insert = function (userInfo) {
    
    
    async function run() {
      // Connect the client to the server	(optional starting in v4.7)
      await client.connect();

      try {
        // Connect to the "insertDB" database and access its "haiku" collection
        const database = client.db("OAUTH");
        const users = database.collection("Users");

        // Create a document to insert
        console.log(userInfo);
        //const doc = {_id: idConversion, username: user, operation: op, value: val, result: resu, timestamp: ts };
        // Insert the defined document into the "haiku" collection
        const result = await users.insertOne(userInfo);
        // Print the ID of the inserted document
        console.log(`A document was inserted with the _id: ${result.insertedId}`);
      } finally {
        // Close the MongoDB client connection
        await client.close();
      }
    }
    // Run the function and handle any errors
    run().catch(console.dir);
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