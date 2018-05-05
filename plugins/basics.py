from cloudbot import hook


@hook.command("info", "information", "botinfo")
def mycmd(notice):
    notice("Youth Bot - This bot it managed by Youth Team")

@hook.command("help", "bothelp")
def mycmd2(notice):
    notice("Commands you may use (wil be added later)")
