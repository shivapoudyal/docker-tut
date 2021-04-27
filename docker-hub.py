1) Tag an image
	sudo docker build -t any_image_name .

2) Push an image to docker-hub #(before this need to login to docker-hub, "docker login")
	i)  sudo docker tag any_image_name shivapoudyal/any_image_name  #(rename a tagged image with docker-hub-repository-name)
	ii) sudo docker push shivapoudyal/any_image_name #(now, this image will push into docker-hub as "shivapoudyal/any_image_name" )

3) 