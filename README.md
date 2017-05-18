vk.com photo saver
==================

# What is it?

Small script for saving vk photos.

# How it works

At first for list of albums:
- Send a querry to api.vk
- Read api.vk JSON answer

Then download all photos from every album

# What i need to start?
- python 3.5

# How to run

- run __init__.py
- copy connection string to your browser and get token
- Fill config.py:
.- API_TOKEN with token
.- CLIENT_ID with your app id
.- USER_ID with id of user, that hold photos
- wait for result

# Troubleshooting

If you get a message with description "too many requests per second" - wait for a minute and try again.
If you want to open a issue - add a stdout and vksaver.log.
