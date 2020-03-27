const http = require('http');
const util = require('util');
const exec = util.promisify(require('child_process').exec);
//create a server object:
http.createServer(function (req, res) {
    let url = req.url;
    console.log('receive response');
    if(url ==='/googlehome'){
        async function initGoogleHome() {
            try {
                const { stdout, stderr } = await exec('python3 googleHome.py');
                console.log('stdout:', stdout);
                console.log('stderr:', stderr);
            }catch (err)=>{
                console.error(err);
            };
        };
        initGoogleHome();
        console.log('active google home');
        res.end();
    }
    res.end(); //end the response
}).listen(3001, function(){
    console.log("server start at port 3001"); //the server object listens on port 3000
});
