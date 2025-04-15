# Dockerfile

# 1. Choose a base Python image
# Use an official Python image. Choose a specific version for consistency.
# '-slim' variants are smaller than the full image.
FROM python:3.13-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file first (for Docker cache optimization)
COPY requirements.txt .

# 4. Install the dependencies
# --no-cache-dir reduces image size slightly
# --trusted-host pypi.python.org helps if you are behind certain firewalls/proxies
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# 5. Copy your application code into the container
COPY . .

# 6. Expose the port Streamlit runs on (default is 8501)
EXPOSE 8501

# 7. Define the command to run your Streamlit app
# This command runs when the container starts.
# Replace 'app.py' if your main script has a different name.
CMD ["streamlit", "run", "1_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
