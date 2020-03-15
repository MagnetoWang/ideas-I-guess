var fs = require("fs");

var data = fs.readFileSync('./demo/helloworld.js');

console.log(data.toString());
console.log("程序执行结束!");
