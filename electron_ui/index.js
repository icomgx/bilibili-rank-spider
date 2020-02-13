if (require('electron-squirrel-startup')) return;
const { app, BrowserWindow } = require('electron')
const jsexecpy = require("jsexecpy")

function callback() {

}
jsexecpy.runpath_with_params("../ajax_api/__init__.py", [""], callback)

function createWindow() {
    // 创建浏览器窗口
    let win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    })

    // 加载index.html文件
    win.loadFile('index.html')
}
app.setUserTasks([{
    program: process.execPath,
    arguments: '--pull-data',
    iconPath: process.execPath,
    iconIndex: 0,
    title: 'Pull data',
    description: 'Pull data from bilibili.com'
}])
app.whenReady().then(createWindow)