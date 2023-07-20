# Start with a Python image.
FROM python:latest

# Set environment variables for Firefox
ENV GECKO_DRIVER_VERSION=0.33.0 \
    FIREFOX_BIN=/usr/bin/firefox \
    FIREFOX_PATH=/usr/local/bin/geckodriver

# Install Firefox
RUN apt-get update && apt-get install -y wget gnupg2 unzip firefox-esr --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install GeckoDriver
RUN wget -q --show-progress --https-only --timestamping https://github.com/mozilla/geckodriver/releases/download/v$GECKO_DRIVER_VERSION/geckodriver-v$GECKO_DRIVER_VERSION-linux64.tar.gz \
    && tar -xzf geckodriver-v$GECKO_DRIVER_VERSION-linux64.tar.gz \
    && rm geckodriver-v$GECKO_DRIVER_VERSION-linux64.tar.gz \
    && mv geckodriver $FIREFOX_PATH \
    && chmod +x $FIREFOX_PATH

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app 
COPY ./app /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]