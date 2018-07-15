from cloudbot import hook


@hook.command(permissions=["zncadmin"])
def add(text, message):
    message(text)