from cloudbot import hook

helpmsg = ["Commands you may use (wil be added later)"]

infomsg = ["Youth Bot - This bot it managed by Youth Team"]








@hook.command(info, information, botinfo)
def mycmd(message):
    message(infomsg)

@hook.command(help, bothelp)
def mycmd2(message):
    message(helpmsg)