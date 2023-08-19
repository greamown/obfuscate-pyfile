#!/bin/bash
# ---------------------------------------------------------

docker build --network=host -t "pyarmor-encrypt" -f "docker/Dockerfile" . 