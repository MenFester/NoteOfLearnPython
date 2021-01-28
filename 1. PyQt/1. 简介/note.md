# 学习笔记

* GUI：Graphical User Interface，图形化用户接口
* Python有很多库可用，做一个功能需要：
  * 相关理论学习
  * 相关的库使用学习
  * 参考：https://wiki.python.org/moin/GuiProgramming
* 选库标准：
  * 没有最好的，只有最适合的
  * 看最新版本，看最近更新时间
  * 功能得强大，但是要看功能需求（简单需求不用强大的库，加载消耗更多资源）
  * 文档齐全、方便查看
  * 性能高
  * 生态支持
  * 跨平台支持（看需求）
  * 开源免费
  * 用的人多的
* PyQt
  * Qt：C++写的跨平台GUI框架，https://resources.qt.io/cn
  * PyQt：Qt最流行的Python绑定。就是用Python重新实现了一遍相关的功能
  * 选择：Python3+、PyQt5
* PyQt的优势
  * 文档齐全，且和Qt文档几乎一致，可以通用
  * 稳定性高
    * 面向对象
    * 信号与槽的机制
    * 界面设计和业务代码完全隔离
  * 生态支持
    * 辅助工具
    * ui转py文件
    * 资源处理
  * 开源免费GPL
    * 软件所有权为开发者本人所有
    * 允许其他用户对原作者软件进行复制和发行
    * 也可以更改后，发行自己的软件
  * 安装
    * 创建虚拟环境：pipenv --three
    * 切换至虚拟环境：pipenv shell
    * 修改配置文件，指定库托管地址：https://pypi.tuna.tsinghua.edu.cn/simple
    * 在虚拟环境下安装库：
      * pipenv install pyqt5
      * pipenv install pyqt-tools
    * 全局安装：
      * PyQt5安装：pip install PyQt5 -i https://pypi.douban.com/simple
      * 辅助工具安装：pip install PyQt5-tools -i https://pypi.douban.com/simple
    * 