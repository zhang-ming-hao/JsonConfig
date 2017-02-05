#!/usr/bin/env python
# coding:utf-8

"""
在Python项目中读写Json格式的配置文件
"""

import json
import os

class JsonConfig(dict):
    """
    以Json形式读写配置文件类
    """

    #--------------------------------------------------------------------------------
    def __init__(self, filePath, default=None):
        """
        初始化
        @filePath：字符串，文件路径
        @default：字典，默认配置项，可以为空
        """

        if default:
            dict.__init__(self, default)
        else:
            dict.__init__(self)

        self.filePath = filePath
        if os.path.isfile(filePath):
            # 读取配置文件
            try:
                fp = open(filePath, "r")
                content = fp.read()
                fp.close()
            except:
                raise ValueError('read file "%s" Failure.' % filePath)

            # 解析Json
            try:
                strJson = content.decode("utf-8-sig")
            except:
                strJson = content.decode("gb2312")

            try:
                self.update(json.loads(strJson, encoding="utf-8"))
            except:
                raise ValueError("invalid json format(%s)" % filePath)
        else:
            self.save()

    #--------------------------------------------------------------------------------
    def update(self, dictArgs=None, **kwArgs):
        """
        更新项目
        """

        if dictArgs != None:
            for (k,v) in  dictArgs.items():
                if not isinstance(v, dict):
                    super(JsonConfig, self).update({k:v})
                else:
                    if self.has_key(k):
                        self[k].update(v)
                    else:
                        super(JsonConfig, self).update({k:v})
        for (k,v) in  kwArgs.items():
            if not isinstance(v, dict):
                super(JsonConfig, self).update({k:v})
            else:
                if self.has_key(k):
                    self[k].update(v)
                else:
                    super(JsonConfig, self).update({k:v})

    #--------------------------------------------------------------------------------
    def save(self, filePath = None):
        """
        保存配置文件
        @filePath：字符串，文件路径，为None时保存到打开的文件中
        """

        path = self.filePath
        if filePath:
            path = filePath

        try:
            strJson = json.dumps(self, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
            strJson.replace("\n", "\r\n")
            fp = open(path, "w")
            fp.write(strJson.encode("utf-8"))
            fp.close()
        except:
            raise ValueError('write file "%s" Failure.' % filePath)

if __name__ == "__main__":

    # 生成配置文件1
    # cfg = JsonConfig("test.cfg")
    # cfg["str"] = "a"
    # cfg["int"] = 1
    # cfg["zh"] = u"中文"
    # cfg["dict"] = {"test":"test"}
    # cfg["list"] = [1,2,3,4,5,6]
    # cfg.save()

    # 生成配置文件2
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
    cfg.save()

    # 读取配置文件
    cfg1 = JsonConfig("test.cfg")
    print cfg1["str"]
    print cfg1["int"]
    print cfg1["zh"]
    print cfg1["dict"]
    print cfg1["list"]

    # 修改配置文件
    cfg1["str"] = "b"
    cfg1["int"] = 2
    cfg1["zh"] = u"依然是中文"
    cfg1["dict"]["test1"] = "test1"
    cfg1["dict"]["test"] = "test2"
    cfg1["list"].append(7)
    cfg1.save()

    # 合并配置文件
    cfg2 = JsonConfig("test.cfg", {"default":"default", "dict":{"test3":3}})
    cfg2.update(abc = "abc")
    print cfg2