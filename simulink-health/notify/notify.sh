#!/bin/bash

# replace the token and chat_id with your own
TOKEN="5869242526:AAFSB_Kd1u5wHq6tY3SdK989bMSj7w73924"
CHAT_ID="156090378"

# replace the message with your own
MESSAGE="simulink model restarted"

# send the message via Telegram API
curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" -d chat_id="$CHAT_ID" -d text="$MESSAGE"