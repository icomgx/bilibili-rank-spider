let {exec,spawn} = require("child_process");
let crypto = require("crypto");
let os = require("os");
let path = require("path");
let fs = require("fs")
let {runpath} = require("./runpython")

// core idea 
// jupyter nbconvert --to notebook mynb --output mynb

let ipynb2py = function(ipynbpath,tmppythonpath,callback){
    return new Promise((resolve,reject)=>{
        try {
            let spawnObj = spawn("jupyter",["nbconvert","--to","script",ipynbpath,"--output",tmppythonpath],{encoding:"utf-8"});
            spawnObj.stdout.on("data",function(chunk){
                console.log('success : ' + chunk.toString());
                callback && callback({data:chunk,ipynbpath})
            })
            spawnObj.stderr.on("data",function(chunk){
                console.log('err : ' + chunk.toString());
                reject({data:`执行${ipynbpath} 错误:${chunk}`,ipynbpath})
                // callback && callback({data:chunk.toString(),pythonpath})
            })
            spawnObj.on('close', function(code) {
                console.log('close code : ' + code);
                runpath(tmppythonpath+".py",callback)
            })
        } catch (error) {
            reject({data:`执行${ipynbpath} 异常:${error}`,ipynbpath})
        }
        
    })
}

let run_ipynb_code = (abspath,callback)=>{
    let md5 = crypto.createHash("md5");
    let pathname = md5.update(abspath).digest("hex")
    let tmppath = path.join(os.tmpdir(),`${pathname}`)
    ipynb2py(abspath,tmppath,callback)
}

module.exports = {
    run_ipynb_code
}