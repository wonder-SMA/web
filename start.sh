sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo pip3 install django==2.0
sudo pip3 install mysqlclient
sudo /etc/init.d/mysql start
