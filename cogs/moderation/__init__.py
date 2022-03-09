from __future__ import annotations

from typing import TYPE_CHECKING

from .block import Block
from .tempmute import TempMute
from .standard import StandardModeration
from .temporary import TemporaryCommands
from .app_commands import ApplicationModeration

if TYPE_CHECKING:
    from bot import DuckBot
    
    
class Moderation(
    TempMute,
    StandardModeration,
    Block,
    TemporaryCommands,
    ApplicationModeration,
    emoji='\N{HAMMER AND PICK}',
    brief='Moderation commands!',
):
    """ Moderation commands. """


def setup(bot: DuckBot):
    bot.add_cog(Moderation(bot))
