from cloudbot import hook


@hook.command(permissions=["playwerewolf"]"werewolf", "mafia")
def playgamecmd(nick, notice,conn):
    notice("You will be connected to the miningame werewolf!")
	conn.send("SAJOIN '" + nick + "' #youth-werewolf")
	

