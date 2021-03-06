import config
import time
import toml
import os
from rich.console import Console
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sync import TelegramClient

console = Console()
settings = {}

if not os.path.exists("authorization.toml"):
    settings["api_id"] = int(console.input("[bold red]API ID> [/]"))
    settings["api_hash"] = console.input("[bold red]API HASH> [/]")

    with open("authorization.toml", "w") as file:
        toml.dump(settings, file)

else:
    with open("authorization.toml") as file:
        settings = toml.load(file)

client = TelegramClient(
    "my_session",
    settings["api_id"],
    settings["api_hash"]
)

while True:
    with client:
        time_obj = datetime.now()

        local_now = time_obj.astimezone()
        local_tz = local_now.tzinfo

        local_tzname = local_tz.tzname(local_now)
        utc_offset = local_tz.utcoffset(local_now).seconds // 3600
        
        minute = str(time_obj.minute)
        month = str(time_obj.month)
        day = str(time_obj.day)
        
        if len(minute) == 1:
            minute = "0" + minute
        
        if len(month) == 1:
            month = "0" + month
        
        if len(day) == 1:
            day = "0" + day


        bio = config.TEMPLATE.format(
            hour=time_obj.hour,
            minute=minute,
            month=month,
            day=day,
            year=time_obj.year,
            timezone=f"UTC+{utc_offset}",
            tzname=local_tzname
        )

        console.print(f"[bold white][{time_obj}] Updating bio to [/][bold yellow]{bio}[/]")

        client(
            UpdateProfileRequest(about=bio)
        )

    console.print(f"[bold white][{time_obj}] Sleeping {config.INTERVAL} seconds...")
    time.sleep(config.INTERVAL)

