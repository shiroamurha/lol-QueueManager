const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 375,
    height: 495,
    resizable: false,
    webPreferences: {
      nodeIntegration: true,
  }
});

  win.setMenu(null);
  win.loadFile('index.html');
 
}

app.whenReady().then(() => {
  createWindow()
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})
