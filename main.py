import discord
import sys
import os
import traceback
from discord.ext import commands
from discord.ext.commands import ExtensionAlreadyLoaded, bot
from config import (
    DISCORD_TOKEN,
    ACTIVITY_LIST,
    STATUS,
)
def run_check():
    version = sys.version_info
    if not int(version.major) >= 3 and int(version.minor) >= 10:
        if int(version.major) == 0:
            return
        raise SystemExit(
            f"Du brauchst eine aktuellere Python Version um das Skript auszuführen, mindestens 3.10 oder höher!"
        )
    return
run_check()
class Saturnbot(commands.Bot):
    async def on_ready(self):
        print(f"{self.user} hat sich erfolgreich eingeloggt")
        async def on_message(self, message):
            print(f"message form {message.author}:{message.content}")
            await self.process.command(message)
            client.loop.create_task(self.status_task())
client = Saturnbot(command_prefix=commands.when_mentioned_or("t."))
client.remove_command("help")
check = 0
for directory in os.listdir("./cogs"):
    if directory != "Ignore":
        for directory2 in os.listdir(f"./cogs/{directory}"):
            if check == 0:
                print(f"\n\nDirectory: {directory}/{directory2}\n")
            for filename in os.listdir(f"./cogs/{directory}/{directory2}/"):
                if filename.endswith(".py") and "ignore_" not in filename:
                    extension = f"cogs.{directory}.{directory2}.{filename[:-3]}"
                    try:
                        client.load_extension(extension)
                        print(
                            f"Das Modul {extension} konnte erfolgreich geladen werden."
                        )
                    except ExtensionAlreadyLoaded:
                        pass
                    except Exception:
                        print(
                            f'Das Modul "{extension}" konnte nicht geladen werden.',
                            file=sys.stderr,
                        )
                        traceback.print_exc()
            check = 0
client.run(DISCORD_TOKEN)