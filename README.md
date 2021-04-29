# selenium-web-jenkins
1、运行环境：
selenium web driver
python3
pytest
git

配置文件：iselenium.ini，填入设备的chromwebdriver文件的全路径
耿伟通用的做法是：
将配置文件复制到本地磁盘的[user.home]目录，填入设备的chromwebdriver文件的全路径

运行命令：
pytest -sv test/web_ut.py --alluredir ./allure-results