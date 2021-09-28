sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chkconfig docker on
sudo yum install -y git
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo chmod +xr /home/ec2-user/docker/.docker-compose.yml.swp
docker-compose version

#run docker commands without sudo, ec2-user is already added into docker group
#if permission denied error occurs, run this
#sudo chmod 777 /var/run/docker.sock
