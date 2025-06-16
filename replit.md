# Roblox Discord Verification Bot

## Overview

This is a Discord bot that provides Roblox account verification using OAuth 2.0 authentication. The bot allows Discord users to link their Roblox accounts to gain verified status and access to server privileges. The system includes both a Discord bot component and a web server for handling OAuth callbacks.

## System Architecture

The application follows a modular architecture with clear separation of concerns:

- **Discord Bot**: Core bot functionality built with discord.py
- **Web Server**: Async HTTP server using aiohttp for OAuth callbacks
- **Database Layer**: SQLite database with async operations via aiosqlite
- **OAuth Integration**: Roblox OAuth 2.0 implementation for secure account verification
- **Configuration Management**: Environment-based configuration system

## Key Components

### Bot Module (`bot/`)
- **commands.py**: Discord slash commands implementation
- **database.py**: SQLite database operations with async support
- **oauth.py**: Roblox OAuth 2.0 client implementation
- **utils.py**: Utility classes for permissions, roles, and embeds

### Web Module (`web/`)
- **server.py**: Aiohttp web server for OAuth callbacks
- **templates/**: HTML templates for verification pages
- **static/**: CSS and frontend assets

### Core Files
- **main.py**: Bot entry point and initialization
- **config.py**: Configuration management and validation
- **.replit**: Replit environment configuration

## Data Flow

1. **Verification Process**:
   - User runs `/verify` slash command in Discord
   - Bot generates OAuth session and stores in database
   - User is redirected to Roblox OAuth authorization
   - Roblox redirects back to web server with authorization code
   - Web server exchanges code for access token and user info
   - Bot assigns verified role to Discord user

2. **Database Operations**:
   - User verifications stored with Discord ID, Roblox ID, and username
   - Temporary verification sessions with expiration tracking
   - Indexes on Discord and Roblox IDs for efficient lookups

## External Dependencies

### Required Services
- **Discord API**: Bot functionality and slash commands
- **Roblox OAuth 2.0**: User authentication and profile access
- **SQLite**: Local data persistence

### Python Packages
- **discord.py**: Discord API wrapper
- **aiohttp**: Async HTTP client/server
- **aiosqlite**: Async SQLite operations

### Environment Variables
- `DISCORD_TOKEN`: Discord bot token
- `ROBLOX_CLIENT_ID`: Roblox OAuth application client ID
- `ROBLOX_CLIENT_SECRET`: Roblox OAuth application secret
- `ROBLOX_REDIRECT_URI`: OAuth callback URL (default: http://localhost:5000/callback)
- `VERIFIED_ROLE_NAME`: Discord role name for verified users (default: "Verified")

## Deployment Strategy

The application is configured for Replit deployment with:

- **Python 3.11** runtime environment
- **Automatic dependency installation** via pip
- **Parallel workflow execution** for bot and web server
- **Port 5000** for web server callbacks
- **Environment variable configuration** for sensitive data

The deployment process:
1. Installs required packages (discord.py, aiohttp, aiosqlite)
2. Starts the main.py script
3. Bot initializes database and connects to Discord
4. Web server starts on port 5000 for OAuth callbacks

## Changelog

- June 16, 2025. Initial setup and implementation completed
- June 16, 2025. Fixed Discord interaction timeout issues and redirect URI configuration

## User Preferences

Preferred communication style: Simple, everyday language.