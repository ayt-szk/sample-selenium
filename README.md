# sample-selenium

## Prerequisites
The following are already installed

- docker
- docker-compose

## Installation
```
git clone git@github.com:ayt-szk/sample-selenium.git
```

## Usage
### Build&Start local environment
```sh
cd [WORK_DIRECTORY]/sample-selenium/deployments/local/
docker-compose up -d
```

### Activate venv
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### View browser

Step1. Start Screen Sharing.app for viewing the browser.
```
URL: localhost:12345
PASS: secret
```

Step2. Execute script.

### Execute script
```sh
python src/sample.py
```

### Stop local environment
```
cd [WORK_DIRECTORY]/sample-selenium/deployments/local/
docker-compose down
```