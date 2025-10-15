#use the official slim Python 3.11 image as the base
FROM python:3.11-slim   
#set the working directory inside the container to /app
WORKDIR /app
#copy only the dependency file first for efficient caching
COPY pyproject.toml ./
#upgrade pip and install dependencies defined in pyproject.toml
#this layer is cached unless pyproject.toml changes
RUN pip install --upgrade pip && pip install .
#copy the rest of the project files into the container
COPY . .
#expose port 8000 to allow external access (FastAPI default)
EXPOSE 8000
#define the default command to run the API service
CMD ["uvicorn", "src.serving.service:app", "--host", "0.0.0.0", "--port", "8000"]
