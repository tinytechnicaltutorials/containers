# Use the Python 3.13 image as our base
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/

# Command to run the app when the container starts
# Use -u to run Python in unbuffered mode, printing output immediately
# (otherwise, you won't see output when running in the container)
CMD ["python", "-u", "app.py"]