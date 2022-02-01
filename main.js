const { app, BrowserWindow } = require('electron')
const url = require('url')
const path = require('path')
const {ipcMain} = require('electron')
const shell = require("shelljs");

const createWindow = () => {

    const win = new BrowserWindow({
        width: 375,
        height: 495,
        resizable: false,
        
    });
  
    win.setMenu(null);
    win.loadFile('index.html');
 
    win.loadURL(url.format ({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
   }))
  
}

app.whenReady().then(() => {
    createWindow()
})

app.on('window-all-closed', () => {
    if (process.platform !== 'amurha_p') app.quit()
})

ipcMain.on('asynchronous-message', (event, arg) => {
    shell.exec("explorer.exe")
    console.log(arg)

})

// C:\Users\amurha_p\my-electron-app\queueManager.py