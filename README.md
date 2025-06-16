# Discord Roblox Verification Bot

A Discord bot that provides secure Roblox account verification using OAuth 2.0 authentication. Users can link their Roblox accounts to gain verified status and access to server privileges.

## Features

- **OAuth 2.0 Authentication**: Secure Roblox account verification
- **Automatic Role Assignment**: Verified users get roles automatically
- **Admin Management**: Manual verification and removal commands
- **User Lookup**: Check linked Roblox accounts
- **Web Interface**: Clean verification pages with responsive design

## Commands

- `/verify` - Start Roblox OAuth verification process
- `/admin-verify <user> <roblox_id>` - Manually link a Roblox account (Admin only)
- `/admin-remove-rblx <user>` - Remove verification link (Admin only)
- `/roblox-whois <user>` - Look up linked Roblox account

## Setup

### Prerequisites

- Python 3.11+
- Discord Bot Token
- Roblox OAuth Application (Client ID & Secret)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd discord-roblox-bot
```

2. Install dependencies:
```bash
pip install discord.py aiohttp aiosqlite
```

3. Set up environment variables:
```bash
export DISCORD_TOKEN="your_discord_bot_token"
export ROBLOX_CLIENT_ID="your_roblox_client_id"
export ROBLOX_CLIENT_SECRET="your_roblox_client_secret"
export ROBLOX_REDIRECT_URI="https://yourdomain.com/callback"
```

4. Run the bot:
```bash
python main.py
```

## Configuration

### Discord Bot Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section and create a bot
4. Copy the bot token for `DISCORD_TOKEN`
5. Enable the following bot permissions:
   - Send Messages
   - Use Slash Commands
   - Manage Roles
   - Read Message History

### Roblox OAuth Setup

1. Go to [Roblox Creator Dashboard](https://create.roblox.com/credentials)
2. Create a new OAuth2 application
3. Set the redirect URI to `https://yourdomain.com/callback`
4. Copy the Client ID and Client Secret
5. Set the scope to `openid profile`

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DISCORD_TOKEN` | Discord bot token | Yes |
| `ROBLOX_CLIENT_ID` | Roblox OAuth client ID | Yes |
| `ROBLOX_CLIENT_SECRET` | Roblox OAuth client secret | Yes |
| `ROBLOX_REDIRECT_URI` | OAuth callback URL | Yes |
| `VERIFIED_ROLE_NAME` | Name of the verified role | No (default: "Verified") |

## Project Structure

```
discord-roblox-bot/
├── bot/
│   ├── commands.py      # Discord slash commands
│   ├── database.py      # SQLite database operations
│   ├── oauth.py         # Roblox OAuth 2.0 client
│   └── utils.py         # Utility functions and classes
├── web/
│   ├── static/
│   │   └── style.css    # Web interface styling
│   ├── templates/
│   │   └── verify.html  # Verification page template
│   └── server.py        # Web server for OAuth callbacks
├── config.py            # Configuration management
├── main.py              # Bot entry point
└── README.md            # This file
```

## How It Works

1. **User runs `/verify`**: Bot creates a verification session and provides OAuth link
2. **User clicks verification**: Redirected to Roblox OAuth authorization
3. **User authorizes**: Roblox redirects back with authorization code
4. **Bot processes callback**: Exchanges code for access token and user info
5. **Verification complete**: User gets verified role and confirmation message

## Database Schema

The bot uses SQLite with two main tables:

- `user_verifications`: Stores Discord-Roblox account links
- `verification_sessions`: Temporary sessions for OAuth process

## Security Features

- Secure OAuth 2.0 flow with state validation
- Session expiration (10 minutes)
- Duplicate account prevention
- Admin permission checks
- Encrypted database storage

## Development

### Running Locally

1. Set up a local development environment
2. Use `localhost:5000` for the redirect URI during testing
3. Update your Roblox OAuth app settings accordingly

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the logs for error details
3. Open an issue on GitHub

## Troubleshooting

### Common Issues

- **"Invalid redirect URI"**: Make sure your Roblox OAuth app redirect URI matches exactly
- **"Bot missing permissions"**: Ensure the bot has Manage Roles permission
- **"Verification timeout"**: Sessions expire after 10 minutes, user needs to restart
- **"Role not found"**: Bot will create the "Verified" role automatically if missing

### Logs

The bot logs to both console and `bot.log` file. Check these for detailed error information.