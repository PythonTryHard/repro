import lightbulb
import hikari

from lightbulb import context
from remi.core.constant import Global

sanity_plugin = lightbulb.Plugin(name="Sanity checker")


@sanity_plugin.command
@lightbulb.command(name="sanity", description="Check your sanity here!")
@lightbulb.implements(*Global.command_implements)
async def sanity_sanity(ctx: context.Context):
    await ctx.respond("Sanity!")
