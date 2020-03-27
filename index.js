const http = require('http');
//create a server object:
http.createServer(function (req, res) {
    let url = req.url;
    console.log('receive response');
    if(url ==='/googlehome'){
        res.write('<h1>googlehome<h1>');
        console.log('active google home');
        res.end();
    }
    res.end(); //end the response
}).listen(3001, function(){
    console.log("server start at port 3001"); //the server object listens on port 3000
});
