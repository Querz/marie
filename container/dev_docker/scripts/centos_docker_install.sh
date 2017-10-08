# install script for cent os 7

# install virtualbox
cd /etc/yum.repos.d
wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
yum --enablerepo rpmforge install dkms

yum groupinstall "Development Tools"
yum install kernel-devel

yum install VirtualBox-5.0

usermod -a -G vboxusers username



# docker-machine

sudo curl -L https://github.com/docker/machine/releases/download/v0.5.0/docker-machine_linux-amd64.zip >machine.zip && \
sudo unzip machine.zip && \
sudo rm machine.zip && \
sudo mv docker-machine* /usr/local/bin

# docker-compose

cd /usr/local/bin && \
sudo curl -L https://github.com/docker/compose/releases/download/VERSION_NUM/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
sudo chmod +x /usr/local/bin/docker-compose