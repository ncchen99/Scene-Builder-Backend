FROM ros:foxy

# install ros package
RUN apt-get update && apt-get install -y \
    python3-pip \
    wget \
    zsh \
    curl && \
    pip3 install boto3 fastapi uvicorn && \
    rm -rf /var/lib/apt/lists/*  && \
    mkdir /root/.aws && \
    sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)" && \
    zsh

COPY config /root/.aws/config
COPY credentials /root/.aws/credentials


# launch ros package
# CMD ["ros2", "launch", "demo_nodes_cpp", "talker_listener.launch.py"]
