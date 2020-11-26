# EgoBot

```sh
killall --quiet --signal 15 -- chrome
killall --quiet --signal 15 -- chromedriver

python src/instagram/bot.py

```

```sh
wget https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm -rf chromedriver_linux64.zip

```

```sh
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list

apt-get update
apt-get install -y google-chrome-stable

```

```sh
apt-get install -y unzip

```
