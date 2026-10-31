# CSCI461 Assignment 1 - Dockerized Data, Text Analysis and Machine Learning
# Custom JupyterLab image for the SMS Spam Collection analysis.

# 1) Base image: official Jupyter "scipy" stack (Python, pandas, numpy,
#    scikit-learn, matplotlib, seaborn, JupyterLab) maintained on quay.io.
FROM quay.io/jupyter/scipy-notebook:latest

LABEL org.opencontainers.image.title="bd-a1" \
      org.opencontainers.image.description="CSCI461 Assignment 1: SMS spam text analysis, classification and K-Means in JupyterLab" \
      org.opencontainers.image.source="https://archive.ics.uci.edu/dataset/228/sms+spam+collection"

# 2) Project folder inside the image. $HOME is /home/jovyan, the default
#    non-root user (jovyan, UID 1000) of the Jupyter Docker Stacks.
ENV PROJECT_DIR=/home/jovyan/bd-a1

# 3) Install additional Python dependencies. requirements.txt is copied on its
#    own first so this layer stays cached while the notebook/data change.
COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# 4) Create the project folder structure.
RUN mkdir -p ${PROJECT_DIR}/data ${PROJECT_DIR}/notebook ${PROJECT_DIR}/output/figures

# 5) Copy the dataset and the notebook (prepared on the host) into the image.
COPY --chown=${NB_UID}:${NB_GID} data/dataset.csv ${PROJECT_DIR}/data/dataset.csv
COPY --chown=${NB_UID}:${NB_GID} notebook/analysis.ipynb ${PROJECT_DIR}/notebook/analysis.ipynb

# 6) Working directory = project folder (JupyterLab opens here).
WORKDIR ${PROJECT_DIR}

# 7) JupyterLab listens on port 8888 inside the container.
EXPOSE 8888

# 8) Start JupyterLab. The base image's start-notebook.py wrapper sets up the
#    jovyan user and prints the access URL + token to the container logs.
CMD ["start-notebook.py", "--ServerApp.root_dir=/home/jovyan/bd-a1", "--ServerApp.ip=0.0.0.0", "--ServerApp.port=8888"]
