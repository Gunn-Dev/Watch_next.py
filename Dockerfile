# Use the official Python image as the base image
FROM python:3.11.4

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY watch_next.py /app/
COPY movies.txt /app/
COPY requirements.txt /app/

# Install project requirements
RUN pip install --no-cache-dir -r requirements.txt

# Run the watch_next.py script when the container starts
CMD ["python", "watch_next.py"]
