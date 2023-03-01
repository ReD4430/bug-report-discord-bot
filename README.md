# Simple Bug Report Tracking Discord Bot

This code creates a Discord bot that can be used to report and respond to bug reports. 
It listens for messages that start with "!reportbug" and "!replybug". 
When a user sends a message starting with "!reportbug", the bot sends a message to a specific channel with the details of the bug report. 
The message is in an embedded format that includes the username of the person who reported the bug, a description of the bug, and a unique identifier.

When a user sends a message starting with "!replybug", 
the bot searches for the bug report with the corresponding ID number and updates the embedded message with a response from a staff member.

To use this code, you need to replace "BOT_TOKEN" with the actual bot token, create a Discord server, and invite the bot to the server. You also need to replace the "BUG_REPORT_CHANNEL" with actual channel name where bug reports will be sent. 
When users report bugs, they need to send a message starting with "!reportbug" and provide a description of the bug. When staff members want to respond to a bug report, they need to send a message starting with "!replybug" followed by the bug report ID and their response.
