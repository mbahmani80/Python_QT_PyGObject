# pip3 helps
bahmani@mbctux:~/pip3_pkgs$ sudo pip3 list 
Package                Version       
---------------------- --------------
altgraph               0.17          
ansible                2.7.7         
ansible-tower-cli      3.3.0         
apache-libcloud        2.4.0         
asn1crypto             0.24.0        
bcrypt                 3.1.6         
beautifulsoup4         4.7.1         
bottle                 0.12.15       
Brlapi                 0.6.7         
bsddb3                 6.2.6         
CDApplet               1.0           
CDBashApplet           1.0           
certifi                2018.8.24     
....

# Ensure pip, setuptools, and wheel are up to date
bahmani@mbctux:~/pip3_pkgs$ python -m pip install --upgrade pip setuptools wheel

bahmani@mbctux:~/pip3_pkgs$ sudo pip3 show mysqlclient
Name: mysqlclient
Version: 2.0.3
Summary: Python interface to MySQL
Home-page: https://github.com/PyMySQL/mysqlclient
Author: Inada Naoki
Author-email: songofacandy@gmail.com
License: GPL
Location: /usr/local/lib/python3.7/dist-packages
Requires: 
Required-by: 
bahmani@mbctux:~/pip3_pkgs$
#-----------------------------------------------------------------------
bahmani@mbctux:~/pip3_pkgs$ sudo pip3 download wheel PyQt5 PyGObject mysqlclient mysql_connector_python pip setuptools eyed3 python_vlc

bahmani@mbctux:~/pip3_pkgs$ ls
coverage-5.3.1-cp37-cp37m-manylinux2010_x86_64.whl              
pycairo-1.20.0.tar.gz
deprecation-2.1.0-py2.py3-none-any.whl                          
PyGObject-3.38.0.tar.gz
eyeD3-0.9.6-py3-none-any.whl                                    pyparsing-2.4.7-py2.py3-none-any.whl
filetype-1.0.7-py2.py3-none-any.whl                             PyQt5-5.15.2-5.15.2-cp35.cp36.cp37.cp38.cp39-abi3-manylinux2014_x86_64.whl
PyQt5_sip-12.8.1-cp37-cp37m-manylinux1_x86_64.whl
mysqlclient-2.0.3.tar.gz                                        python_vlc-3.0.11115-py3-none-any.whl
mysql_connector_python-8.0.22-cp37-cp37m-manylinux1_x86_64.whl  setuptools-51.1.1-py3-none-any.whl
packaging-20.8-py2.py3-none-any.whl                             six-1.15.0-py2.py3-none-any.whl
pip-20.3.3-py2.py3-none-any.whl                                 toml-0.10.2-py2.py3-none-any.whl
protobuf-3.14.0-cp37-cp37m-manylinux1_x86_64.whl                wheel-0.36.2-py2.py3-none-any.whl
bahmani@mbctux:~/pip3_pkgs$ 

#-----------------------------------------------------------------------

# Installing Python packages from local file system folder with pip
# https://stackoverflow.com/questions/15031694/installing-python-packages-from-local-file-system-folder-to-virtualenv-with-pip

pip3 install ./mypackage-1.0.4.tar.gz


