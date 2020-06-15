const { app, BrowserWindow} =  require('electron')


async function pageHome () {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
        },
    })
    
    // win.setMenu(null)
    win.loadURL('https://web.whatsapp.com/', {
        userAgent: 'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.104 Safari/537.36'
    })
}

app.whenReady().then(pageHome)

app.on('window-all-closed', () => {
    if(process.platform !== 'darwin'){
        app.quit()
    }
})

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
    }
})
