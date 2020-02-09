if (!process.argv[1]) {
    console.log('file required in arg')
    process.exit(1);
}

var http = require('http');
var fs = require('fs');
var index = fs.readFileSync(process.argv[2]);

http.createServer((req, res) => {
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(index);
}).listen(3000);