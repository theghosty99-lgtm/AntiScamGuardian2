import discord
from discord.ext import commands
from discord import app_commands

from database.database import (
    add_role,
    remove_role,
    get_roles,
    add_user,
    remove_user,
    get_users,
    add_channel,
    remove_channel,
    get_channels,
)


class Whitelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


whitelist = app_commands.Group(
    name="whitelist",
    description="Manage AntiScamGuardian whitelist"
)

role_group = app_commands.Group(
    name="role",
    description="Role whitelist",
    parent=whitelist
)

user_group = app_commands.Group(
    name="user",
    description="User whitelist",
    parent=whitelist
)

channel_group = app_commands.Group(
    name="channel",
    description="Channel whitelist",
    parent=whitelist
)


# =====================================================
# ROLE
# =====================================================

@role_group.command(name="add", description="Whitelist a role")
@app_commands.checks.has_permissions(administrator=True)
async def role_add(interaction: discord.Interaction, role: discord.Role):

    add_role(interaction.guild.id, role.id)

    await interaction.response.send_message(
        f"✅ Added {role.mention} to the whitelist.",
        ephemeral=True
    )


@role_group.command(name="remove", description="Remove a role")
@app_commands.checks.has_permissions(administrator=True)
async def role_remove(interaction: discord.Interaction, role: discord.Role):

    remove_role(interaction.guild.id, role.id)

    await interaction.response.send_message(
        f"🗑 Removed {role.mention} from the whitelist.",
        ephemeral=True
    )


@role_group.command(name="list", description="List whitelisted roles")
async def role_list(interaction: discord.Interaction):

    roles = get_roles(interaction.guild.id)

    if not roles:
        return await interaction.response.send_message(
            "No roles are whitelisted."
        )

    text = "\n".join(f"<@&{r}>" for r in roles)

    await interaction.response.send_message(text)


# =====================================================
# USER
# =====================================================

@user_group.command(name="add")
@app_commands.checks.has_permissions(administrator=True)
async def user_add(interaction: discord.Interaction, user: discord.Member):

    add_user(interaction.guild.id, user.id)

    await interaction.response.send_message(
        f"✅ {user.mention} added."
    )


@user_group.command(name="remove")
@app_commands.checks.has_permissions(administrator=True)
async def user_remove(interaction: discord.Interaction, user: discord.Member):

    remove_user(interaction.guild.id, user.id)

    await interaction.response.send_message(
        f"Removed {user.mention}"
    )


@user_group.command(name="list")
async def user_list(interaction: discord.Interaction):

    users = get_users(interaction.guild.id)

    if not users:
        return await interaction.response.send_message("No users.")

    await interaction.response.send_message(
        "\n".join(f"<@{u}>" for u in users)
    )


# =====================================================
# CHANNEL
# =====================================================

@channel_group.command(name="add")
@app_commands.checks.has_permissions(administrator=True)
async def channel_add(interaction: discord.Interaction, channel: discord.TextChannel):

    add_channel(interaction.guild.id, channel.id)

    await interaction.response.send_message(
        f"✅ {channel.mention} added."
    )


@channel_group.command(name="remove")
@app_commands.checks.has_permissions(administrator=True)
async def channel_remove(interaction: discord.Interaction, channel: discord.TextChannel):

    remove_channel(interaction.guild.id, channel.id)

    await interaction.response.send_message(
        f"Removed {channel.mention}"
    )


@channel_group.command(name="list")
async def channel_list(interaction: discord.Interaction):

    channels = get_channels(interaction.guild.id)

    if not channels:
        return await interaction.response.send_message(
            "No channels."
        )

    await interaction.response.send_message(
        "\n".join(f"<#{c}>" for c in channels)
    )


async def setup(bot):
    cog = Whitelist(bot)

    bot.tree.add_command(whitelist)

    await bot.add_cog(cog)