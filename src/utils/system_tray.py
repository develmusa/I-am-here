from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import pyqtSlot

class SystemTray(QSystemTrayIcon):
    def __init__(self, app, model, main_ctrl, parent=None):
        super(SystemTray, self).__init__(parent)

        self._model = model
        self._app = app
        self._main_ctrl = main_ctrl
        
        self.setVisible(True)
        
        menu = QMenu(parent)

        self.start_stop_action = menu.addAction("Start")
        self.start_stop_action.triggered.connect(lambda: self._main_ctrl.start_stop())

        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(self._app.quit) 

        self.setContextMenu(menu)

        # listen for model event signals
        self._model.dont_sleep_started_changed.connect(self.on_dont_sleep_started_changed)


    @pyqtSlot(bool)
    def on_dont_sleep_started_changed(self, value):
        if value:
            self.start_stop_action.setText("Stop")
        else: 
            self.start_stop_action.setText("Start")


        # menu = QMenu(parent) 
        # option1 = QAction("Geeks for Geeks") 
        # option2 = QAction("GFG") 
        # o = menu.addAction(option1) 
        # o2 = menu.addAction(option2) 
        # self.setContextMenu(menu) 

        # self._ui.pushButton.clicked.connect(lambda: self._main_controller.start_stop())

    #         QtCore.QObject.connect(exitAction,QtCore.SIGNAL('triggered()'), self.exit)

    # def exit(self):
    #   QtCore.QCoreApplication.exit()

        # menu = QMenu(parent) 
        # option1 = QAction("Geeks for Geeks") 
        # option2 = QAction("GFG") 
        # menu.addAction(option1) 
        # menu.addAction(option2) 
        
        # # To quit the app 
        # quit = QAction("Quit") 
        # # quit.triggered.connect(app.quit) 
        # menu.addAction(quit) 
        
        # # Adding options to the System Tray 
        # self.setContextMenu(menu) 