import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/fc06688a71c96183133f7.jpg https://telegra.ph/file/2623a6a6c763b299143dc.jpg https://telegra.ph/file/f14605ffad7443e4c0163.jpg https://telegra.ph/file/78e70dda2214d4a132a72.jpg https://telegra.ph/file/d8224d6b1a800dba48ed6.jpg https://telegra.ph/file/4c7fdf79893a072ab5e45.jpg https://telegra.ph/file/e68c9358e8de813e54982.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "BaiLu")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'MovieBot')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'cinemacollections')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<code>{file_name}</code>\n\n<b>Size:</b> {file_size}\n\n{file_caption}\n\n<b>[© TVSeries & Movie Studio](https://t.me/joinchat/prE6ALN6x2hkY2E1)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>⍞ ᴛɪᴛʟᴇ:</b> <a href={url}>{title}</a>\n<b>〄 ᴛʏᴘᴇ:</b> {kind}\n<b>⟴ ʀᴇʟᴇᴀꜱᴇ ᴅᴀᴛᴇ:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>★ ʀᴀᴛɪɴɢ:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>⌥ ʀᴜɴᴛɪᴍᴇ:</b> <code>{runtime} minutes</code>\n<b>⌗ ɢᴇɴʀᴇ:</b> {genres}\n\n<b>⌬ ʟᴀɴɢᴜᴀɢᴇs:</b> {languages}\n<b>✠ ᴄᴏᴜɴᴛʀɪᴇs:</b> {countries}\n<a href='https://t.me/cinemacollections '>© cinemacollections</a></b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two seperate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as diffrent buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your Currect IMDB template is {IMDB_TEMPLATE}"
