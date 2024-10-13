FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy requirements.txt
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . /code/

# Expose the default Django port
EXPOSE 8000