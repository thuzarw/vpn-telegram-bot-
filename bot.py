#!/usr/bin/env python3
"""
VPN User Management Telegram Bot
Firestore Database Integration
"""

import os
import logging
from telebot import TeleBot
from dotenv import load_dotenv

# Import modules
from config import Config
from firebase.firebase_init import db
from handlers.commands import setup_commands
from handlers.callbacks import setup_callbacks
from handlers.messages import setup_messages

# Load environment variables
load_dotenv()

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

def main():
    """Main function to start the bot"""
    try:
        # Initialize bot
        bot = TeleBot(Config.BOT_TOKEN)
        
        # Setup handlers
        setup_commands(bot)
        setup_callbacks(bot)
        setup_messages(bot)
        
        logger.info("🤖 VPN Bot is starting...")
        logger.info(f"👑 Admin IDs: {Config.ADMIN_IDS}")
        logger.info(f"📁 Collection: {Config.COLLECTION_NAME}")
        
        # Start bot
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
        
    except Exception as e:
        logger.error(f"❌ Bot failed to start: {e}")
        raise

if __name__ == "__main__":
    main()
