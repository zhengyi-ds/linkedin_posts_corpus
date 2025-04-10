# LinkedIn Corpus Project Docker Run Guide for Streamlit App

This guide provides step-by-step instructions to pull the Docker image, run the container, and clean up after use. The application can be accessed via a web browser using the provided URLs.

---

## Frontend Documentation

For user guidance on how to use the application, refer to the **Frontend Documentation**.
**https://github.ubc.ca/zyshan/COLX523_linkedin_corpus/blob/main/documents/Front-End_Documentation.pdf**

---

## Prerequisites

1. **Docker Installed**: Ensure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).
2. **Command Line Access**: Use a terminal or command prompt to execute the commands.

---

## Steps to Run the Docker Container

### 1. Pull the Docker Image

Pull the Docker image from Docker Hub using the following command:

```bash
docker pull timchristilaw/streamlit-app:latest
```

### 2. Run the Docker Container

Run the container and map port 8501 (used by Streamlit) to your local machine. The `--rm` flag ensures the container is automatically removed when it stops:

```bash
docker run -it --rm -p 8501:8501 timchristilaw/streamlit-app
```

- **Windows URL**: Open your browser and navigate to [http://127.0.0.1:8501](http://127.0.0.1:8501).
- **Mac URL**: Open your browser and navigate to [http://127.0.0.0:8501](http://127.0.0.0:8501).

Press `Ctrl/Cmd C` on bash to stop the execution of the docker image, this will also delete the container

---

## Steps to Delete the Docker Image (Optional)

If you want to delete the Docker image after use, follow these steps:

### 1. List Docker Images

List all Docker images to find the image ID:

```bash
docker images
```

### 2. Remove the Docker Image

Delete the image using the image ID:

```bash
docker rmi <IMAGE_ID>
```

**Notes:**

- Replace `<IMAGE_ID>` with the actual ID from your system.
- Ensure Docker is running before executing the commands.
- If you encounter any issues, check the Docker logs for debugging:

```bash
docker logs <CONTAINER_ID>
```

---

Enjoy using the Streamlit app! 🚀

