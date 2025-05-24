![](https://github.com/5hojib/5hojib/raw/main/images/Aeon-MLTB.gif)

---

# Aeon Bot

Aeon is a streamlined and feature-rich bot designed for efficient deployment and enhanced functionality.

---

## Features

- **Minimalistic and Optimized**: Simplified by removing unnecessary code for better performance.
- **Effortless Deployment**: Fully configured for quick and easy deployment to Heroku.
- **Enhanced Capabilities**: Integrates features from multiple sources to provide a versatile bot experience.

---
--- 
## 🗄 *Deployment Guide for vps*

<details>
  <summary><b>View All Steps</b> <sup><kbd>Click Here</kbd></sup></summary>
    <ol><li><details>
      <summary>Prerequisites</summary>

- Tutorial Video from A to Z:</li>
  - Thanks to [Wiszky](https://github.com/vishnoe115)</li>

<p><a href="https://youtu.be/IUmq1paCiHI"> <img src="https://img.shields.io/badge/See%20Video-black?style=for-the-badge&logo=YouTube" width="160"/></a></p>
  </details></li>
  <li><details>
    <summary>Installing requirements</summary>

- Clone this repo:
'''
git clone https://github.com/shadow-Senpai0/Aeon mirrorbot/ && cd mirrorbot
'''
- For Debian based distros
'''
sudo apt install python3 python3-pip
'''
Install Docker by following the [official Docker docs](https://docs.docker.com/engine/install/debian/)

- For Arch and it's derivatives:

sudo pacman -S docker python
- Install dependencies for running setup scripts:
'''
pip3 install -r requirements.txt
'''
    
  </details></li>
  <li><details>
    <summary>Setting up config file</summary>

'''   
cp config_sample.env config.env
'''
- Remove the first line saying:
'''
_____REMOVE_THIS_LINE_____=True
'''
Fill up rest of the fields. Meaning of each field is discussed below. NOTE: All values must be filled between quotes, even if it's Int, Bool or List.

  </details></li>
  <li><details>
    <summary>Build And Run the Docker Image</summary>
Make sure you still mount the app folder and installed the docker from official documentation.

- There are two methods to build and run the docker:
  1. Using official docker commands.
  2. Using docker-compose. (Recommended)

------

#### Build And Run The Docker Image Using Official Docker Commands

- Start Docker daemon (SKIP if already running, mostly you don't need to do this):

sudo dockerd
- Build Docker image:
'''
sudo docker build . -t leechx
'''
- Run the image:
'''
sudo docker run -p 80:80 -p 8080:8080 leechx
'''
- To stop the running image:
sudo docker ps
```
'''
sudo docker stop id
'''
----

#### Build And Run The Docker Image Using docker-compose

**NOTE**: If you want to use ports other than 80 and 8080 for torrent file selection and rclone serve respectively, change it in [docker-compose.yml](https://github.com/weebzone/WZML-X/blob/master/docker-compose.yml) also.

- Install docker-compose

sudo apt install docker-compose

- Build and run Docker image or to view current running image:

sudo docker-compose up

- After editing files with nano for example (nano start.sh):

sudo docker-compose up --build

- To stop the running image:

sudo docker-compose stop

- To run the image:

sudo docker-compose start

- To get latest log from already running image (after mounting the folder):

sudo docker-compose up

- Tutorial video from Tortoolkit repo for docker-compose and checking ports

<p><a href="https://youtu.be/c8_TU1sPK08"> <img src="https://img.shields.io/badge/See%20Video-black?style=for-the-badge&logo=YouTube" width="160"/></a></p>

------

#### Docker Notes

**IMPORTANT NOTES**:

1. Set `BASE_URL_PORT` and `RCLONE_SERVE_PORT` variables to any port you want to use. Default is `80` and `8080` respectively.
2. You should stop the running image before deleting the container and you should delete the container before the image.
3. To delete the container (this will not affect on the image):

sudo docker container prune

4. To delete the images:

sudo docker image prune -a
## Deployment Instructions (Heroku)

Follow these steps to deploy Aeon to Heroku:

### 1. Fork and Star the Repository
- Click the **Fork** button at the top-right corner of this repository.
- Give the repository a star to show your support.

### 2. Navigate to Your Forked Repository
- Access your forked version of this repository.

### 3. Enable GitHub Actions
- Go to the **Settings** tab of your forked repository.
- Enable **Actions** by selecting the appropriate option in the settings.

### 4. Run the Deployment Workflow
1. Open the **Actions** tab.
2. Select the `Deploy to Heroku` workflow from the available list.
3. Click **Run workflow** and fill out the required inputs:
   - **BOT_TOKEN**: Your Telegram bot token.
   - **OWNER_ID**: Your Telegram ID.
   - **DATABASE_URL**: MongoDB connection string.
   - **TELEGRAM_API**: Telegram API ID (from [my.telegram.org](https://my.telegram.org/)).
   - **TELEGRAM_HASH**: Telegram API hash (from [my.telegram.org](https://my.telegram.org/)).
   - **HEROKU_APP_NAME**: Name of your Heroku app.
   - **HEROKU_EMAIL**: Email address associated with your Heroku account.
   - **HEROKU_API_KEY**: API key from your Heroku account.
   - **HEROKU_TEAM_NAME** (Optional): Required only if deploying under a Heroku team account.
4. Run the workflow and wait for it to complete.

### 5. Finalize Setup
- After deployment, configure any remaining variables in your Heroku dashboard.
- Use the `/botsettings` command to upload sensitive files like `token.pickle` if needed.

---

## Contributing

We welcome contributions! Whether it's bug fixes, feature enhancements, or general improvements:
- **Report issues**: Open an issue for bugs or suggestions.
- **Submit pull requests**: Share your contributions with the community.

---

## License

This project is licensed under the MIT License. Refer to the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Special thanks to the original developers of the [Mirror-Leech-Telegram-Bot](https://github.com/anasty17/mirror-leech-telegram-bot).
- Gratitude to contributors from various repositories whose features have been integrated into Aeon.


## Recent activity [![Time period](https://images.repography.com/58464391/AeonOrg/Aeon-MLTB/recent-activity/MUUzwqnoU_5n6kL3Jc8TTWcA3UxPyCHC2emNNSTGJh8/4gYNvj3-wi0i5zQVemeNAbqB7TrkUx_7BxZxhReSIVg_badge.svg)](https://repography.com)
[![Timeline graph](https://images.repography.com/58464391/AeonOrg/Aeon-MLTB/recent-activity/MUUzwqnoU_5n6kL3Jc8TTWcA3UxPyCHC2emNNSTGJh8/4gYNvj3-wi0i5zQVemeNAbqB7TrkUx_7BxZxhReSIVg_timeline.svg)](https://github.com/AeonOrg/Aeon-MLTB/commits)
