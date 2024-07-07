# Use the official ROS Noetic base image
FROM ros:noetic-ros-core

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-noetic-turtlesim \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set the default shell to bash
SHELL ["/bin/bash", "-c"]

# Source ROS setup.bash
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Create and set the working directory
WORKDIR /root/ros_ws

# Initialize a catkin workspace
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && \
    mkdir -p src && \
    cd src && \
    catkin_init_workspace && \
    cd .. && \
    catkin_make"

# Source the workspace setup.bash
RUN echo "source /root/ros_ws/devel/setup.bash" >> ~/.bashrc

COPY ./src /root/ros_ws/src
COPY ./turtlesim_demo.launch /root/ros_ws/

# Build the workspace
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && cd /root/ros_ws && catkin_make"

# Create XDG_RUNTIME_DIR directory with proper permissions
RUN mkdir -p /tmp/runtime-root && chmod 0700 /tmp/runtime-root

# Set the entrypoint to the launch file
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source /root/ros_ws/devel/setup.bash && roslaunch /root/ros_ws/turtlesim_demo.launch"]