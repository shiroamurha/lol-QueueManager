const { app, BrowserWindow } = require('electron')


const createWindow = () => {

    const win = new BrowserWindow({
        width: 484,
        height: 520,
        resizable: false,
        webPreferences: {
            nodeIntegration: true
        }
        
    });

    var python = require('child_process').spawn('py', ['./main.py']);
    python.stdout.on('data', function (data) {
        console.log("data: ", data.toString('utf8'));
    }); 
    python.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`); // when error
    });

    win.setMenu(null);
    win.loadFile('index.html');
    win.loadURL("http://localhost:5000/")
}


app.whenReady().then(() => {
    createWindow()
})

app.on("quit", function () {});

// C:\Users\amurha_p\my-electron-app\queueManager.py