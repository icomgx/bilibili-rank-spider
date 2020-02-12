let {exec,spawn} = require("child_process");
let crypto = require("crypto");
let os = require("os");
let path = require("path");
let fs = require("fs")
let _execpython = function(pythonpath,callback,paramslist){
    return new Promise((resolve,reject)=>{
        try {
            let spwanparmas = [pythonpath]
            if(paramslist){
                paramslist.forEach(
                    (value,index)=>{
                        value!="" && (spwanparmas.push(value))
                    }
                )
            }
            let spawnObj = spawn("python",spwanparmas,{encoding:"utf-8"});
            spawnObj.stdout.on("data",function(chunk){
                console.log('success : ' + chunk.toString());
                callback && callback({data:chunk.toString(),pythonpath})
            })
            spawnObj.stderr.on("data",function(chunk){
                console.log('err : ' + chunk.toString());
                reject({data:`执行${pythonpath} 错误:${chunk}`,pythonpath})
                // callback && callback({data:chunk.toString(),pythonpath})
            })
            spawnObj.on('close', function(code) {
                console.log('close code : ' + code);
            })
            // var makeProcess = exec(`python ${pythonpath}`,function(err,data){
            //     if(err){
            //         reject({data:`执行${pythonpath} 错误:${err}`,pythonpath})
                    
            //     }else{
            //         resolve({data,pythonpath})
            //         callback && callback({data,pythonpath})
            //     }
            // })

        } catch (error) {
            reject({data:`执行${pythonpath} 异常:${error}`,pythonpath})
        }
        
    })
}


function runpath(path,callback){
    _execpython(path,callback).then(
        data=>{
            console.log('执行py文件成功 :', data);
        },
        err=>{
            console.log('执行py路劲错误 :', err);
            callback(err)
        }
    )
}
function runpath_with_params(path,params,callback){
    //"[object Array]"
    let paramslist = []
    if(Object.prototype.toString.call(params) === "[object String]"){
        paramslist = params.split(" ")
    }
    if(Object.prototype.toString.call(params) === "[object Array]"){
        paramslist=params
    }
    // if(Object.prototype.toString.call(params) === "[object Object]"){
    //     for(let key in params){
    //         if(key[0]!=="-"){
    //             // console.log('key, :', key,params[key]);
    //             if(key === params[key]){
    //                 paramslist.push(key)
    //             }else{
    //                 console.log('你必须在参数前添加-或者--you should use -/-- before params:');
    //                 callback('你必须在参数前添加-或者--you should use -/-- before params:')
    //                 return
    //             }
                
    //         }else{
    //             paramslist.push(key)
    //             paramslist.push(params[key])
    //         }
    //     }
    // }
    _execpython(path,callback,paramslist).then(
        data=>{
            console.log('执行py文件成功 :', data);
        },
        err=>{
            console.log('执行py路劲错误 :', err);
            callback(err)
        }
    )
}

/**
 * 把文本输入到　路劲
 * @param {*} pythontext 类python文件
 * @param {*} tmppath  路径
 */
let _writeFile = function(pythontext,tmppath){
    return new Promise((resolve,reject)=>{
        fs.writeFile(tmppath,pythontext,function(err){
            if(err){
                reject(`writing data err! ${err}`)
            }else{
                resolve(tmppath)
            }
        })
    })
}

let _removeFile = function(tmppath){
    return new Promise((resolve,reject)=>{
        fs.unlink(tmppath,function(err){
            if (err) {
                reject(`remove file err! ${err}`)
            }else{
                resolve(`成功删除${tmppath}`)
            }
        })
    })
}


let runpytext = (pythontext,dosomething,hasdeletething)=>{
    let md5 = crypto.createHash("md5");
    let pathname = md5.update(pythontext).digest("hex")
    let tmppath = path.join(os.tmpdir(),`${pathname}.py`)
    console.log('tmppath :', tmppath);
    _writeFile(pythontext,tmppath).then(
        data=>{
            dosomething &&　dosomething()
            console.log("成功创建文件",data);
            return _execpython(data)
        },
        err=>{
            console.log(' 创建失败 :', err);
        }
    ).then(
        filedata =>{
            let {data,pythonpath} = filedata
            console.log(' 成功执行 :', data);
            return _removeFile(pythonpath)
        },
        err=>{
            let {data,pythonpath} = err
            console.log(' 执行失败:', data);
            return _removeFile(pythonpath)
        }
    ).then(
        data =>{
            console.log(' 删除成功file :', data);
        },
        err=>{
            console.log(' 删除失败err :', err);
        }
    )
}

module.exports = {
    runpath,
    runpytext,
    runpath_with_params
}