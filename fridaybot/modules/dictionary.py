"""Syntax: .meaning <word>"""

import requests
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd
from PyDictionary import PyDictionary

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd("meaning (.*)"))
@friday.on(sudo_cmd("meaning (.*)", allow_sudo=True))
async def _(event):
    stark = await edit_or_reply(event, "Finding Meaning.....")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    dictionary=PyDictionary()
    a = (dictionary.meaning(input_str))
    b = a.get("Noun")
    chsaiujwal = ""
    for x in b:
	    chsaiujwal += x+"\n"
    await stark.edit(f"<b> meaning of {input_str} is:-</b>\n {chsaiujwal}", parse_mode="HTML",)


CMD_HELP.update(
    {
        "dictionary": "**Dictionary**\
\n\n**Syntax : **`.meaning <word>`\
\n**Usage :** Get meaning and pronunciation of a word."
    }
)
