from decouple import config

# Load configurations using decouple
API_ID = config('API_ID', "21344245")  # Cast to int if the value is an integer
API_HASH = config('API_HASH', "e72de40c666f1664f847a79f97dd3882")        # No cast needed for string values
BOT_TOKEN = config('BOT_TOKEN', "7082591322:AAGQm5X0B5pvrT0AeNfe3KUB_cQWOq3zp5c")
# Convert the ADMIN field from the .env into a list of integers
ADMIN = [int(admin_id) for admin_id in config('ADMIN', "7585839477").split(',') if admin_id]
CAPTION = config('CAPTION', default="")  # Optional field, set a default value if missing

# Set download location for media (can be changed to a configurable value)
DOWNLOAD_LOCATION = "./DOWNLOADS/"
