# Poe-API-Server
 An API server that lets you interact with Poe.com, using Selenium. It's just a test project and should not be used for any productive purposes.

API Endpoints:

    GET /latest-message
    Returns the bot's latest message, message generation status, and suggestions if they exist

    POST /send-message
    Sends a message after clearing the bot's context. Requires 'message'

    POST /clear-context
    Clears the bot's context

    POST /start-driver
    Starts the driver. Requires 'p_b_cookie' and 'bot_name'

    POST /kill-driver
    Kills the driver

    POST /abort-message
    Aborts the current message generation

    GET /is-generating
    Returns the current message generation status

Guide:
1. Install it with 'docker compose up'
2. Wait until it's running and listening (by default to 0.0.0.0:5000)
3. Initialize the web-driver with /start-driver
