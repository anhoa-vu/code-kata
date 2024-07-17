# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the script file into the container
COPY parser.py /app/parser.py

# Command to run the script with command-line arguments
ENTRYPOINT ["python", "parser.py"]

# Example command to provide default arguments (to be overridden)
CMD ["spec.txt", "data.txt", "output.csv", "--encoding", "utf-8"]
