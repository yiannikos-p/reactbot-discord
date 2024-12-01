# reactbot-discord
Python script that runs a ReactBot (as seen on Jacksfils™) discord bot!

# Dependencies / Installation
You'll need the discord python package (install from pip or AUR), and probably python-ffmpeg too. 
# Installation
## Bot Setup
You'll have to make your own discord bot for this one via the [discord developer portal](https://discord.com/developers/docs/intro). 
Under 0Auth2, ReactBot will need permisions for:
 - View channels
 - Read message history
 - Send messages
 - Connect
 - Speak

Don't forget to mark it as *bot* at the scopes.

Once you have a valid token, save it somewhere safe and using the 0auth link, add it to your server.
## Run the script
The script needs two things:
 - a valid bot token
 - a directory full of mp3 files for the reactions
To start the bot simply run
```shell
python reactbot.py <your-token> /path/to/directory/full/of/mp3/files
```
That should be it!
# Usage 
When in a voice channel, send !join for ReactBot to join

You can kick it off the voice channel with !leave

Send !react whenever you want ReactBot's insightful commentary :)
