1) Vist get.docker.com run these two commands

	curl -fsSL https://get.docker.com -o get-docker.sh
	sh get-docker.sh

2) Install Docker Compose
	sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

3) Apply executable permission
	sudo chmod +x /usr/local/bin/docker-compose

4) Create docker path
	sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

5) Check docker compose version
	sudo docker-compose version

