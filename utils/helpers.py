from database.database import (
    get_roles,
    get_users,
    get_channels
)


def is_user_whitelisted(member):
    """Returns True if the member is whitelisted."""

    # User whitelist
    if member.id in get_users(member.guild.id):
        return True

    # Role whitelist
    role_ids = get_roles(member.guild.id)

    for role in member.roles:
        if role.id in role_ids:
            return True

    return False


def is_channel_whitelisted(channel):
    """Returns True if the channel is whitelisted."""

    return channel.id in get_channels(channel.guild.id)


def should_ignore_message(message):
    """
    Returns True if the bot should ignore this message.
    """

    if message.author.bot:
        return True

    if is_user_whitelisted(message.author):
        return True

    if is_channel_whitelisted(message.channel):
        return True

    return False