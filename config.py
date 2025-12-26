"""
Configuration settings for VPN Telegram Bot
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class"""
    
    # Bot Token
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    # Admin IDs (add your Telegram User IDs here)
    ADMIN_IDS = [int(id.strip()) for id in os.getenv("ADMIN_IDS", "").split(",") if id.strip()]
    
    # Firebase Collection Name
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "users")
    
    # Bot Settings
    MAX_USERS_PER_PAGE = 10
    DATE_FORMAT = "%Y-%m-%d"
    
    # Paths
    SERVICE_ACCOUNT_PATH = "firebase/serviceAccountKey.json"
    
    # Messages
    WELCOME_MESSAGE = "🔐 *VPN User Management System*\n\n*Welcome Admin!*\nChoose an option below:"
    ACCESS_DENIED_MESSAGE = "⚠️ *Access Denied*\nYou are not authorized to use this system."
    
    @classmethod
    def validate_config(cls):
        """Validate configuration"""
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is not set in .env file")
        if not cls.ADMIN_IDS:
            raise ValueError("ADMIN_IDS is not set in .env file")
        return True
