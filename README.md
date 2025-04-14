# Smart Scheduler Bot

## Description
This project is a smart scheduler bot designed to send scheduled messages on Telegram. It allows users to schedule messages at specific times, track the messages sent each day, and reset the counter at midnight. The bot stores its state between restarts to ensure persistence.

## Features
- **Message Scheduling**: Schedule messages to be sent at specific times of the day.
- **Telegram Integration**: Send messages to a specified Telegram chat.
- **Daily Message Limit**: Track how many messages have been sent during the day.
- **Daily Reset**: Reset the sent messages count at midnight.
- **State Persistence**: Save the bot state between restarts.
- **Manual Schedule Addition**: Add schedules manually using the `add_schedule.py` script.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Naumenko0Nikita/smart-scheduler-bot.git
   cd smart-scheduler-bot

2. ```bash pip install 
   -r requirements.txt

4. Configure your bot by editing the config.py file (you can leave the Telegram token part for now and add it later).

## Running the Bot
To run the bot in development mode with automatic file monitoring, use the following setup:

1. Using watchdog to monitor changes: You can use watchdog to automatically restart the bot when code changes are made during development.

First, make sure you have watchdog installed: 
2. ```bash 
    pip install watchdog

2. Running the bot: Run the bot with a watchdog file monitoring changes (dev mode):
python watcher.py
The bot will restart automatically every time a .py file is modified.

## Adding a Schedule Manually

Will be done in the future

## Quick commands for terminal:

You can reset the list of sent messages:
python manage.py reset

## Configuration
The bot uses the config.py file for its configuration. Here you can set various parameters like the target Telegram chat ID, the schedule of messages, and the reset time for sent messages.

## Project Structure
manage.py: Main entry point for managing schedules.

modules/: Contains all the main bot logic such as message sending, logging, and scheduling.

tools/: Contains utility scripts for managing schedules and resetting the bot.

watcher.py: Monitors code changes and restarts the bot automatically in development mode.

config.py: Configuration file for the bot.

state.json: File to store the state between bot restarts.
