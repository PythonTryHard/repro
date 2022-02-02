import lightbulb
import hikari

from lightbulb import commands, context

sanity_plugin = lightbulb.Plugin(name="Sanity checker")


@sanity_plugin.command
@lightbulb.command(name="sanity", description="Check your sanity here!")
@lightbulb.implements(commands.PrefixCommand, commands.SlashCommand)
async def sanity_sanity(ctx: context.Context):
    await ctx.respond("Sanity!")
