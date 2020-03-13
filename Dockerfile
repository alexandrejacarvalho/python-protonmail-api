FROM python:3.7-buster

# Install ChromeDriver
RUN cd /tmp/
RUN wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /root/chromedriver

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update
RUN apt-get -y install google-chrome-stable
RUN google-chrome --version && which google-chrome

# Copy files and install pip requirements
RUN cd /root/
RUN mkdir webserver/
WORKDIR /root/webserver/
COPY . ./
RUN pip install -r requirements.txt
RUN pip install gunicorn


# Configs
EXPOSE 5000

# Run
CMD gunicorn -b 0.0.0.0:5000 --timeout 3600 main:app
