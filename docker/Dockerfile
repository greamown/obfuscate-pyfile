FROM python:3.10.11
# ------------------------------------------------------------------
# Close noninteractive
ENV DEBIAN_FRONTEND noninteractive
# ------------------------------------------------------------------
USER root
WORKDIR /workspace
# ------------------------------------------------------------------
# Install requirements.sh & entrypoint.sh
COPY ./docker /workspace/docker
RUN chmod u+x /workspace/docker/install.sh \
                && /workspace/docker/install.sh