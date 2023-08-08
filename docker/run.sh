#!/bin/bash
# ---------------------------------------------------------

# Color ANIS
RED='\033[1;31m';
BLUE='\033[1;34m';
GREEN='\033[1;32m';
YELLOW='\033[1;33m';
CYAN='\033[1;36m';
NC='\033[0m';

# ---------------------------------------------------------
# Set the default value of the getopts variable 
GPU="all"
SET_VERSION=""
SERVER=false
COMMAND="bash"
WORKSPACE="/workspace"
CONTAINER_NAME="pyarmor-encrypt"
DOCKER_IMAGE="pyarmor-encrypt"
TAG_VER="latest"

# ---------------------------------------------------------
# SERVER or DESKTOP MODE
if [ ${SERVER} ];then
	MODE="DESKTOP"
	SET_VERSION="-v /tmp/.x11-unix:/tmp/.x11-unix:rw -e DISPLAY=unix${DISPLAY}"
	# let display could connect by every device
	xhost + > /dev/null 2>&1
else
	MODE="SERVER"
fi

# ---------------------------------------------------------
# Run container
DOCKER_CMD="docker run \
                --name ${CONTAINER_NAME} \
                --user root \
                --rm -it \
                -v /dev:/dev \
                --net=host --ipc=host \
                -w ${WORKSPACE} \
                -v `pwd`:${WORKSPACE} \
                -v /etc/localtime:/etc/localtime:ro \
                -v /var/run/docker.sock:/var/run/docker.sock \
                ${SET_VERSION} \
                ${DOCKER_IMAGE}:${TAG_VER} \
                ${COMMAND}"

# ---------------------------------------------------------
echo -e "${YELLOW}"
echo "----- Command: ${DOCKER_CMD} -----"
echo -e "${NC}"

bash -c "${DOCKER_CMD}"