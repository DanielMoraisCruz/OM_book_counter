"""
Um software mobile criado para auxiliar o escoque e venda de livros
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class OMBookCounter(toga.App):

    def startup(self):
        main_box = toga.Box()
                
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return OMBookCounter()
