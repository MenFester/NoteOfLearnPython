# 导入需要的包
from PyQt5.Qt import *    # 包括常用的类
import sys

# 创建一个应用程序
app = QApplication(sys.argv)    # sys.argv：命令行参数

# 控件操作
window = QWidget()

window.setWindowTitle("社会我强哥， 热狠话不多")
window.resize(500, 600)
window.move(200, 300)

label = QLabel(window)
label.setText("Hello, World!")
label.move(200, 200)

window.show()

# 执行应用程序，进入消息循环
sys.exit(app.exec_())    # sys.exit：退出程序；app.exec_()：程序进入消息循环（无限循环）