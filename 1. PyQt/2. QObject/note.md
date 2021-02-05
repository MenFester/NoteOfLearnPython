# 学习笔记

* QObject继承的父类
  * 是所有Qt对象的基类
* QObject对象的名称和属性
  * `setObjectName("唯一名称")` ：给一个Qt对象设置一个名称
  * `ObjectName()` ：获取一个Qt对象的名称
  * `setProperty("属性名称", 值)` ：给Qt对象动态的添加一个属性与值
  * `property("属性名称")` ：获取一个对象的属性值
  * `dynamicPropertyNames()` ：获取一个对象中所有通过setProperty()设置的属性
  * 