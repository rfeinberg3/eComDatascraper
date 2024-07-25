#syntax=docker/dockerfile:1

# Pull the selenium image with chrome driver. Setting the platform is necessary for ARM based machines.
FROM --platform=linux/amd64 selenium/standalone-chrome:126.0-chromedriver-126.0

# Set the working directory
WORKDIR /app

# Install Python and pip
USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set Python3 as default
RUN ln -s /usr/bin/python3 

# Install dependencies
COPY /requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy in the source code
COPY /sandbox_scraper.py /app/sandbox_scraper.py
COPY /datascraper/ /app/datascraper
COPY /config /app/config

# Create directory to retrieve volume dataset
RUN mkdir -p /volume/item_data

# Copy in keywords list(s) to scrape
COPY /keywords /app/keywords

ENTRYPOINT ["python3", "sandbox_scraper.py"]