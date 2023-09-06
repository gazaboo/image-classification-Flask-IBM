# Image de base
FROM python:3.10.7-slim-buster

# Create /app and cd into it
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the Flask app
CMD ["python", "server.py"]