let {run_ipynb_code,runpath,run,runpath_with_params} = require("../index")

// run_ipynb_code("../test.ipynb",function(data){
//     console.log(data);
// })
let path = require("path")

// runpath_with_params(path.resolve(__dirname,"./test.py"),"aa bb cc",function(data){
//     console.log(data);
// })

let aa = "as"
let dd = "cd"
let c = "dd"//aa,dd,c,
runpath_with_params(path.resolve(__dirname,"./test.py"),["a","bb","--a=80s","-a=90"],function(data){
    console.log(data);
})
