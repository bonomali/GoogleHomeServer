const http = require('http');
// const util = require('util');
// const exec = util.promisify(require('child_process').exec);
const fs = require('fs');
const {spawn} = require('child_process');


http.createServer(function (req, res) {
    let url = req.url;
    console.log('receive response');
    if(url ==='/googlehome'){
        res.write('<h1>google home<h1>');
        async function initGoogleHome() {
            try {
                // const { stdout, stderr } = await exec('python3 googleHome.py');
                // const { stdout, stderr } = await exec('python3 testVolume.py');
                // console.log('stdout:', stdout);
                // console.log('stderr:', stderr);
                let python = spawn('python3', ['googleHome.py']);

            } catch (err){
                console.error(err);
            }
        }
        initGoogleHome();
        console.log('active google home');
        res.end();
    } else if (url ==='/mp3_cache') {
        // let filePath = `${__dirname}/mp3_cache/bbf12b4197e8122835f67e3551678174.mp3`;
        let filePath = `${__dirname}/mp3_cache/f3757829c2aea1300ee4020222b31f91.mp3`;
        let stat = fs.statSync(filePath);
        res.writeHead(200, {
            'Content-Type': 'audio/mpeg',
            'Content-Length': stat.size,
            "Accept-Ranges": "bytes"
        });
        fs.createReadStream(filePath).pipe(res);
        console.log('active mp3_cache');
    }
}).listen(3001, function(){
    console.log("server start at port 3001");
});
