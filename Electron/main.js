const { app, BrowserWindow, Menu, dialog } =  require('electron')

function createWindow () {
    let win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
        }
    })

    var menu = Menu.buildFromTemplate([
        {
            label: 'Automatize',
            submenu: [
                {
                    label: 'Start',
                    click() {
                        dialog.showMessageBox({
                            message: 'Start clicked'
                        })
                    }
                },
                {
                    label: 'Configure',
                    click(){
                        dialog.showMessageBox({
                            message: 'Configure clicked'
                        })
                    }
                }
            ]
        }
    ])

    Menu.setApplicationMenu(menu); 
    win.loadURL('https://web.whatsapp.com/', {
        userAgent: 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.104 Safari/537.36'
    })
    const ses = win.webContents.session
}

app.whenReady().then(createWindow)

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
