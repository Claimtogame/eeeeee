import os

class Config:
    # Discord Bot Configuration
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', '')
    
    # Roblox OAuth Configuration
    ROBLOX_CLIENT_ID = os.getenv('ROBLOX_CLIENT_ID', '')
    ROBLOX_CLIENT_SECRET = os.getenv('ROBLOX_CLIENT_SECRET', '')
    ROBLOX_REDIRECT_URI = os.getenv('ROBLOX_REDIRECT_URI', 'https://workspace.claimsgames.repl.co/callback')
    
    # Role Configuration
    VERIFIED_ROLE_NAME = os.getenv('VERIFIED_ROLE_NAME', 'Verified')
    
    # Web Server Configuration
    WEB_HOST = '0.0.0.0'
    WEB_PORT = 5000
    
    # Database Configuration
    DATABASE_PATH = 'bot_data.db'
    
    # Admin Role/Permission Configuration
    ADMIN_ROLE_NAMES = ['Admin', 'Moderator', 'Staff']
    
    # Roblox API URLs
    ROBLOX_OAUTH_URL = 'https://apis.roblox.com/oauth/v1/authorize'
    ROBLOX_TOKEN_URL = 'https://apis.roblox.com/oauth/v1/token'
    ROBLOX_USER_INFO_URL = 'https://apis.roblox.com/oauth/v1/userinfo'
    ROBLOX_USER_API_URL = 'https://users.roblox.com/v1/users'
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        required_vars = [
            ('DISCORD_TOKEN', cls.DISCORD_TOKEN),
            ('ROBLOX_CLIENT_ID', cls.ROBLOX_CLIENT_ID),
            ('ROBLOX_CLIENT_SECRET', cls.ROBLOX_CLIENT_SECRET)
        ]
        
        missing_vars = [var_name for var_name, var_value in required_vars if not var_value]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True
