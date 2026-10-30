# Screenshots (to be captured by the team on your own machine)

The assignment requires screenshots of a successful `docker build`, `docker images`, the running container and the Jupyter notebook. It also requires lifecycle evidence (`docker ps`, `docker ps -a`, `docker logs`, `docker inspect`) and the Docker Hub reproduction.
Save the PNG files in this folder using the names below. Keep the full terminal window visible, including the command you typed.

| # | File name | What must be visible | Command / action |
|---|---|---|---|
| 1 | `01_docker_build.png` | The end of the build with all steps `DONE` and `naming to docker.io/library/bd-a1:latest` | `docker build -t bd-a1:latest .` |
| 2 | `02_docker_images.png` | The `bd-a1` image with its tag, image ID and size | `docker images` |
| 3 | `03_docker_run.png` | The `docker run` command with `-p 8888:8888` and `-v .../output:...` and the returned container ID | see README §8 |
| 4 | `04_docker_ps.png` | `bd-a1-container` with status **Up** and `0.0.0.0:8888->8888/tcp` | `docker ps` |
| 5 | `05_docker_logs.png` | The JupyterLab start-up lines and the `http://127.0.0.1:8888/lab?token=...` URL (you may blur the token) | `docker logs bd-a1-container` |
| 6 | `06_docker_inspect.png` | The mount (`"Type":"bind"`) and the port binding | `docker inspect --format "{{json .Mounts}}" bd-a1-container` and `docker inspect --format "{{json .NetworkSettings.Ports}}" bd-a1-container` |
| 7 | `07_jupyterlab_notebook.png` | JupyterLab in the browser (`localhost:8888`) with `analysis.ipynb` open | browser |
| 8 | `08_notebook_run_all.png` | The end of the notebook after **Kernel → Restart Kernel and Run All Cells**, showing *"All required outputs were generated successfully."* | browser |
| 9 | `09_output_on_host.png` | The host file explorer or terminal showing `output/` with the CSV, the TXT files and `figures/` | `ls output output/figures` (PowerShell: `dir output`) |
| 10 | `10_docker_ps_a.png` | The container in **Exited** state after `docker stop` | `docker stop bd-a1-container`, then `docker ps -a` |
| 11 | `11_docker_push.png` | A successful push of `YOUR_DOCKERHUB_USERNAME/bd-a1:v1` | `docker push ...` (README §12) |
| 12 | `12_dockerhub_page.png` | The repository page on hub.docker.com showing the tag | browser |
| 13 | `13_teammate_pull_run.png` | **Another team member's machine**: `docker pull` + `docker run` + the notebook working | README §13 |
| 14 | `14_github_repo.png` (bonus) | The GitHub repository page with the README rendered | browser |

Tip (Windows): <kbd>Win</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd>. Tip (macOS): <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>4</kbd>.

`docs/validation/` contains a log and a JupyterLab screenshot captured during project validation in a different (sandbox) environment. They show the project working in Docker, but they are **not** a substitute for your own screenshots.
