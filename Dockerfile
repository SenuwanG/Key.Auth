# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY your_python_script.py /app
COPY requirements.txt /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "your_python_script.py"]
