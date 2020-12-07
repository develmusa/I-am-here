
from PyQt5.QtWidgets import QApplication
import sys
from models.model import Model
from controllers.main_ctrl import MainController
from views.main_view import MainView
from helpers.icon_helper import IconHelper
from utils.system_tray import SystemTray

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.setQuitOnLastWindowClosed(True)

        # Connect everything together
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.system_tray = SystemTray()
        self.icon_helper = IconHelper(self, self.system_tray, self.model)

        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
