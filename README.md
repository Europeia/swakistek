# swakistek
Yet another Discord welcome bot. 

# Configuration
Bot configuration is done via a YAML file. By default, the bot looks for a file called `config.yaml` in the current working directory. The config file location can be overriden with the `SWAK_CONFIG_FILE` environment variable.
- `bot_token`: Your bot's token, found in the Discord Developer Portal. 
- `welcome_channel_id`: The channel ID of your welcome channel. This should be a channel that both the bot and unregistered users can see.
- `welcome_message`: The text of your welcome message. Use the variable `<@$member_id>` in your message to ping the new user. Note that the bot can only ping users, not roles, though if you wish to include a role name in the message, you can do so using the `<@&{role_id}>` syntax.

# Run
```[SWAK_CONFIG_FILE=/path/to/config.yaml] uv run main.py```
