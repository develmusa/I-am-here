from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction

class SystemTray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.setVisible(True)

        menu = QMenu() 
        option1 = QAction("Geeks for Geeks") 
        option2 = QAction("GFG") 
        menu.addAction(option1) 
        menu.addAction(option2) 
        
        # To quit the app 
        quit = QAction("Quit") 
        # quit.triggered.connect(app.quit) 
        menu.addAction(quit) 
        
        # Adding options to the System Tray 
        self.setContextMenu(menu) 