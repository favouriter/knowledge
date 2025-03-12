# 知识管理
* 通过脚本扫描文件夹，生成config.json配置文件，index.html加载配置文件，生成目录树。点击目录树，查看目录下的文件，点击文件名称，可查看文件内容，支持pdf、html、markdown三种文件格式

## 添加知识文件
* 将知识文件添加到docs/articles目录下，支持pdf、html、markdown三种文件格式，可以建立多级目录

## 生成config.json
```
python3 generate_config.py
```

## weh部署
```
cd docs
python3 -m http.server 80
# 访问http://127.0.0.1
```