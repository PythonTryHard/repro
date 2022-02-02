import lightbulb
from .sanity import sanity_plugin


__plugin_name__ = sanity_plugin.name
__plugin_description__ = sanity_plugin.description


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(sanity_plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(sanity_plugin)