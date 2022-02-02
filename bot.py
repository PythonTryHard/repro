import hikari
import lightbulb

# Get our bot instance
bot = lightbulb.BotApp(
    token='TOKEN',
    prefix="!",
    banner=None,
)


# Set up some listener for events. In the future we might do some fancy async or DB that needs
# graceful construction and deconstruction, so it's better to have some scaffold in place beforehand
@bot.listen(hikari.StartingEvent)
async def on_starting(_) -> None:
    pass


@bot.listen(hikari.StoppingEvent)
async def on_stopping(_) -> None:
    pass


@bot.listen(hikari.StartedEvent)
async def on_started(_) -> None:
    pass


bot.load_extensions("repro.command.sanity")
bot.reload_extensions("repro.command.sanity")

bot.run()