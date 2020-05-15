cd C:\Users\doer\
python -m venv .\venv\standalone
.\venv\standalone\Scripts\activate
pyinstaller --paths=src --name=batch_tabs src/manage.py
pyinstaller --name=batch_tabs batch_tabs.spec
pyinstaller --paths=src --name=batch_tabs batch_tabs.spec

# --key用来加密打包后的字节码，需要加密库，需要下载windows基础库支持，安装有点麻烦，暂时不管, -F打包生成一个.exe文件，不适合需要nuxt前端的情况
pyi-makespec -F --additional-hooks-dir D:\data_files\batch_tabs\src\pyinstaller_hooks --name=batch_tabs --hidden-import corsheaders --hidden-import rest_framework  --key zI1NiJ91QiLCJ manage.py

# --add-data=".;."
# --add-data="nuxt;nuxt" --add-data="static;static" --add-data="templates;templates"
# 发布之前自己现在本地运行一次创建运行时缓存，用户启动就会快很多，把batch_tabs.bat拷贝进程序目录，一起压缩到batch_tabs.zip，然后上传百度云分发销售
pyi-makespec --add-data="nuxt;nuxt" --additional-hooks-dir pyinstaller_hooks --name=batch_tabs --hidden-import corsheaders --hidden-import corsheaders.middleware --hidden-import rest_framework  --hidden-import url --hidden-import cmd_tool  --hidden-import url.urls --hidden-import cmd_tool.urls manage.py

pyinstaller --clean --noconfirm batch_tabs.spec
.\dist\batch_tabs.exe runserver localhost:8888
.\dist\batch_tabs\batch_tabs.exe runserver localhost:8888