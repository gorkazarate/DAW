'use strict';
var usersService = require('../service/UsersService');

const getUser = (req, res, next, user_id) => {
  try{
    var user = usersService.getUser(user_id);
    console.log("Se entra");

  }catch(err){
    return "404 Invalid User_ID";
  }
  user.then( function (user){
    if(user !== undefined){
      console.log("***********", user);
      res.send(user);
      return user;

    }else{
      console.log("***********UNDEFINED");

      res.send("undefined");
      return user;
    }
  })
  .catch(function(err){
    console.log("***********ERROR", err);

    res.send(err);
    return err;
  });
};

const postUser =  (req, res, next, body, user_id) =>{
  usersService.postUser(body, user_id);
  res.send("200 User Posted");
};

module.exports = {
  getUser,
  postUser
};