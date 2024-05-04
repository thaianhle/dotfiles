#!/usr/bin/python3

import os

def debina_install():
	#DEBIAN_PKG = "lxterminal lxappearance rofi picom awesome awesome-extra xfce4-power-manager alsa-utils"
	#os.system(f"sudo apt-get install {DEBIAN_PKG}")

	folder = "config_test"
	os.system("echo '...copying and configure awesomwem before starting....'")

	print("creating folder config")

	os.system(f"mkdir $HOME/{folder}")
	os.system(f"cp -r .config/* $HOME/{folder}")


def rhel_install():
	pass
linux_name = os.popen("cat /etc/*release | grep '^ID='").read()
OS_DEBIAN="debian|ubuntu"
OS_RHEL="almalinux|centos|fedora"
CUR_PKG = None

if linux_name.find(OS_DEBIAN):
	print("start with debian")
	debina_install()
elif linux_name.find(OS_RHEL):
	print("start with rhel or fedora")
else:
	print("don't support linux, only support debian or rhel or fedora")



