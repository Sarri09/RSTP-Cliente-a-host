DOCKER_IMAGE_NAME = nfqueue-mitm-scapy

build:
	docker build -t ${USER}/${DOCKER_IMAGE_NAME} .

run:
	docker run -it ${USER}/${DOCKER_IMAGE_NAME}