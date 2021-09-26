version: '3.1'
services:
    db:
        image: mysql
        restart: always
        environment:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: medical_system
        container_name: mysql
        volumes: 
          - ./mysql_data:/var/lib/mysql/
        ports:
          - "3308:3306"
        networks:
          - custom_network
    phpmyadmin:
        image: phpmyadmin/phpmyadmin:latest
        restart: always
        environment:
          PMA_HOST: db
          PMA_USER: root
          PMA_PASSWORD: root
        ports:
          - "8080:80"
        networks:
          - custom_network 
networks:
  custom_network:
    external:
      name: your_network_name 
