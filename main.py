import asyncio
import discord
from discord.ext import commands
import logging
import os
from config import Config
from bot.database import Database
from bot.commands import setup_commands
from web.server import start_web_server

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class RobloxVerificationBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(
            command_prefix='!',
            intents=intents,
            description='Roblox verification bot with OAuth 2.0'
        )
        
        self.db = Database()
        
    async def setup_hook(self):
        """Called when the bot is starting up"""
        await self.db.initialize()
        await setup_commands(self)
        logger.info("Bot setup completed")
        
    async def on_ready(self):
        """Called when bot is ready"""
        logger.info(f'{self.user} has connected to Discord!')
        logger.info(f'Bot is in {len(self.guilds)} guilds')
        
        # Sync slash commands
        try:
            synced = await self.tree.sync()
            logger.info(f"Synced {len(synced)} command(s)")
        except Exception as e:
            logger.error(f"Failed to sync commands: {e}")
            
    async def on_guild_join(self, guild):
        """Called when bot joins a guild"""
        logger.info(f"Joined guild: {guild.name} (ID: {guild.id})")
        
    async def on_command_error(self, ctx, error):
        """Global error handler"""
        logger.error(f"Command error: {error}")

async def main():
    """Main function to start bot and web server"""
    bot = RobloxVerificationBot()
    
    # Start web server in background
    web_task = asyncio.create_task(start_web_server(bot))
    
    # Start bot
    try:
        await bot.start(Config.DISCORD_TOKEN)
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    except Exception as e:
        logger.error(f"Bot error: {e}")
    finally:
        await bot.close()
        web_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
