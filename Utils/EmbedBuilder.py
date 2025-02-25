"""
Project Ascend's Discord bot, Written and mainted by @Cloudsify

github.com/Cloudsify
"""

import discord
import json

# Was this a stupid way of doing it? Yes. yes it was.
def createEmbed(content):
    title = content.get('title')
    description = content.get('description')
    color = content.get('color', 0x000000)
    author_name = content.get('author_name')
    author_url = content.get('author_url')
    author_icon_url = content.get('author_icon_url')
    field_name = content.get('field_name', "")
    field_value = content.get('field_value', "")
    field_name_two = content.get('field_name', "")
    field_value_two = content.get('field_value_two', "")
    field_name_three = content.get('field_name_three', "")
    field_value_three = content.get('field_value_three', "")
    field_isInline = content.get('field_is_inline', False)
    footer_text = content.get('footer_text')

    embed = discord.Embed(
        title=title if title else None,
        description=description if description else None,
        color=color,
        timestamp=discord.utils.utcnow()
    )

    if author_name or author_url or author_icon_url:
        embed.set_author(
            name=author_name if author_name else None,
            url=author_url if author_url else None,
            icon_url=author_icon_url if author_icon_url else None
        )

    if field_name or field_value:
        embed.add_field(
            name=field_name,
            value=field_value,
            inline=field_isInline
        )
    if field_name_two or field_value_two:
        embed.add_field(
            name=field_name_two,
            value=field_value_two,
            inline=field_isInline
        )
    if field_name_three or field_value_three:
        embed.add_field(
            name=field_name_three,
            value=field_value_three,
            inline=field_isInline
        )

    if footer_text:
        embed.set_footer(text=footer_text)

    return embed
