# JsonConfig
在Python项目中读写Json格式的配置文件

## 安装
执行```setup.py install```来安装本模块

## 使用
生成或读取配置文件：
```python
import JsonConfig

cfg = JsonConfig("test.cfg")
cfg["str"] = "a"
cfg["int"] = 1
cfg["zh"] = u"中文"
cfg["dict"] = {"test":"test"}
cfg["list"] = [1,2,3,4,5,6]
cfg.save()
```

生成或读取带有默认值的配置文件：
```python
import JsonConfig

d = {
    "dict": {
        "test": "test"
    },
    "int": 1,
    "list": [
        1,
        2,
        3,
        4,
        5,
        6
    ],
    "str": "a",
    "zh": u"中文"
}
cfg = JsonConfig("test.cfg", d)
```
当test.cfg存在且文件的内容与默认值不一致时，以文件中的内容为准。

JsonConfig继承自dict，可以像使用字典一样使用。