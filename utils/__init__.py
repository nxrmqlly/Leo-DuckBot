from __future__ import annotations

import asyncio
import time as time_lib
from typing import (
    TYPE_CHECKING,
    Optional, 
    Tuple,
    TypeVar,
    ParamSpec,
    Callable,
    Awaitable,
    Union,
)

from discord.ext import commands

if TYPE_CHECKING:
    from bot import DuckBot
    from logging import Logger

T = TypeVar('T')
P = ParamSpec('P')

def add_logging(func: Callable[P, Union[Awaitable[T], T]]) -> Callable[P, Union[Awaitable[T], T]]:
    """
    Used to add logging to a coroutine or function.
    
    .. code-block:: python3
        >>> async def foo(a: int, b: int) -> int:
        >>>     return a + b
        
        >>> logger = add_logging(foo)
        >>> result = await logger(1, 2)
        >>> print(result)
        3
        
        >>> def foo(a: int, b: int) -> int:
        >>>     return a + b
        
        >>> logger = add_logging(foo)
        >>> result = logger(1, 2)
        >>> print(result)
        3
    """
    async def _async_wrapped(*args: P.args, **kwargs: P.kwargs) -> Awaitable[T]:
        start = time_lib.time()
        result = await func(*args, **kwargs)  # type: ignore
        print(f'{func.__name__} took {time_lib.time() - start:.2f} seconds')
        
        return result # type: ignore
    
    def _sync_wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
        start = time_lib.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took {time_lib.time() - start:.2f} seconds')
        
        return result # type: ignore
    
    return _async_wrapped if asyncio.iscoroutinefunction(func) else _sync_wrapped # type: ignore


class DuckCog(commands.Cog):
    """The base class for all DuckBot cogs.
    
    Attributes
    ----------
    bot: DuckBot
        The bot instance.
    """
    __slots__: Tuple[str, ...] = (
        'bot',
    )
     
    def __init__(self, bot: DuckBot) -> None:
        self.bot: DuckBot = bot
