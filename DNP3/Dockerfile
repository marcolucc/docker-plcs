# Use an official Python runtime as the base image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

RUN apt-get update

# Install software 
RUN apt-get install -y git
RUN apt-get install -y cmake
RUN apt-get install -y g++
RUN pip install pydnp3
# Install required packages
#RUN pip install -r requirements.txt
#RUN git clone --recursive http://github.com/Kisensum/pydnp3
#RUN python pydnp3/setup.py install

# Copy the Python script to the container
COPY main.py /app/

# Set the default command to run the Python script
CMD ["python", "main.py"]