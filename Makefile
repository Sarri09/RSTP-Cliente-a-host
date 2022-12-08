DOCKER_IMAGE_NAME = test

build:
	docker build -t ${USER}/${DOCKER_IMAGE_NAME} .

run:
	docker run --privileged -it ${USER}/${DOCKER_IMAGE_NAME}
