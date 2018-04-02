// HTTP server and client test

var result = 0;
var http = require("http");

var server = http.createServer(function (req, res) {
  console.log("Connected");
  var body = '';
  req.on('data', function(data) {
	  console.log("<" + data);
      body += data;
  });
  req.on('end', function() {
      console.log("Request " + JSON.stringify(req), body);
      res.writeHead(200, {'Content-Type': 'text/plain'});
      res.write('42');
      res.end();
  });
  req.on('close', function() {
	  console.log("<close");
  });
});
server.listen(8080);

// http.get("http://localhost:8080/foo.html", function(res) {
var options = {
    host: 'localhost', // host name
    port: 8080,            // (optional) port, defaults to 80
    path: '/post.html',           // path sent to server
    method: 'POST',       // HTTP command sent to server (must be uppercase 'GET', 'POST', etc)
    protocol: 'http:',   // optional protocol - https: or http:
    headers: {
        'Transfer-Encoding': 'chunked'
    }
};
var req = http.request(options, function(res) {
  console.log("Got response: " + JSON.stringify(res));
  var body = '';
  res.on('data', function(data) {
	  console.log(">" + data);
      body += data;
  });
  res.on('end', function() {
	  console.log(">END");
      server.close();
      result = body=="42";
  });
  res.on('close', function() {
	  console.log(">CLOSE");
  });
})
req.write('666');
setTimeout(() => {
    req.write('777');
    setTimeout(() => {
        req.write('888');
        setTimeout(() => {
            req.end();
        }, 400);
    }, 400);
}, 400);
// .on('error', function(e) { console.log("Got error: " + e.message); });

