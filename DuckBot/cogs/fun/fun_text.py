import re
from discord.ext import commands

from ._base import FunBase


def fancify(text, *, style: list, normal: list = None):
    normal = normal or ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sub = dict(zip(normal, style))
    pattern = '|'.join(sorted(re.escape(k) for k in sub))

    return re.sub(pattern, lambda m: sub.get(m.group(0)), text, flags=re.IGNORECASE)


class FancyText(FunBase):

    @commands.command(name='fancify', aliases=['fancy', 'ff'])
    async def fancify(self, ctx, *, text):
        """ 𝓯𝓪𝓷𝓬𝓲𝓯𝓲𝓮𝓼 𝓽𝓮𝔁𝓽 """
        style = ['𝓪', '𝓫', '𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', '𝓴', '𝓵', '𝓶',
                 '𝓷', '𝓸', '𝓹', '𝓺', '𝓻', '𝓼', '𝓽', '𝓾', '𝓿', '𝔀', '𝔁', '𝔂', '𝔃']
        await ctx.send(fancify(text, style=style), reminders=False)

    @commands.command(name='thicc-text', aliases=['thicc', 'tt'])
    async def thicc_text(self, ctx, *, text):
        """ 𝗠𝗮𝗸𝗲𝘀 𝘁𝗲𝘅𝘁 𝗧𝗛𝗜𝗖𝗖 """
        style = ['𝗔', '𝗕', '𝗖', '𝗗', '𝗘', '𝗙', '𝗚', '𝗛', '𝗜', '𝗝', '𝗞', '𝗟', '𝗠', '𝗡', '𝗢', '𝗣', '𝗤', '𝗥', '𝗦', '𝗧', '𝗨', '𝗩', '𝗪', '𝗫', '𝗬', '𝗭',
                 '𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', '𝗺', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂', '𝘃', '𝘄', '𝘅', '𝘆', '𝘇',
                 '𝟭', '𝟮', '𝟯', '𝟰', '𝟱', '𝟲', '𝟳', '𝟴', '𝟵', '𝟬']
        normal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        await ctx.send(fancify(text, style=style, normal=normal), reminders=False)
