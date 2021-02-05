from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.test_QObject()

    def test_QObject(self):
        mros = QObject.mro()
        for mro in mros:
            print(mro)

        object = QObject()
        object.setObjectName("notice")
        print("object name is: ", object.objectName())

        object.setProperty("notice_level1", "error")
        object.setProperty("notice_level2", "warning")
        print("value of notice_level1: ", object.property("notice_level1"))
        print("dynamicProperty include: ", object.dynamicPropertyNames())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())