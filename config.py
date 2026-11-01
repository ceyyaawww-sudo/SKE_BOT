# ==========================================
# ملف الإعدادات الأساسية للبوت (Configuration)
# ==========================================
import os

# الأسماء (عربي وإنجليزي) للردود أو الاستخدام
BOT_NAME_AR = os.environ.get("BOT_NAME_AR", "مهند")
BOT_NAME_EN = os.environ.get("BOT_NAME_EN", "SKE")

# بيانات حساب منصة مطوري تيليجرام (my.telegram.org)
API_ID = int(os.environ.get("API_ID", "12345678"))
API_HASH = os.environ.get("API_HASH", "your_api_hash_here")

# توكن البوت من BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token_here")

# أيدي المطور الأساسي
OWNER_ID = int(os.environ.get("OWNER_ID", "123456789"))

# رابط قاعدة بيانات Redis
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")

# معرف قناة الاشتراك الإجباري
CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "kaoaoal")
