# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from driver.database.dbpunish import is_gbanned_user
from pyrogram import Client, filters
from program.utils.inline import menu_markup, stream_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    ASSISTANT_USERNAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
async def set_start(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("home start")
    await query.edit_message_text(
        f"""πͺπ²πΉπ°πΌπΊπ² **[{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
π§π΅πΆπ πΆπ ππ΅π² ππΏπΌπΈπ²π» π πππΆπ°...!
βββββββββββββββββββ
β£Β» **α΄α΄ α΄α΄κ±Ιͺα΄ α΄Κα΄Κα΄Κ Κα΄α΄.** 
β£Β» **ΚΙͺΙ’Κ Η«α΄α΄ΚΙͺα΄Κ α΄α΄κ±Ιͺα΄.**
β£Β» **α΄ Ιͺα΄α΄α΄ α΄Κα΄Κ κ±α΄α΄α΄α΄Κα΄α΄α΄.**
β£Β» **α΄α΄α΄ α΄Ι΄α΄α΄α΄ κ°α΄α΄α΄α΄Κα΄κ±.**
β£Β» **κ±α΄α΄α΄Κκ°α΄κ±α΄ κ±α΄α΄α΄α΄.**
βββββββββββββββββββ
**α΄α΄κ±ΙͺΙ’Ι΄α΄α΄ ΚΚ : [α΄Κα΄α΄α΄α΄Κ α΄α΄α΄ α΄Ι΄](https://t.me/PavanMagar)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Details π", callback_data="command_list"),
                ],
                
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
async def set_guide(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("user guide")
    await query.edit_message_text(
        f"""β How to use this Bot ?, read the Guide below !

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{ASSISTANT_USERNAME} to your group or type /userbotjoin to invite her, unfortunately the userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`.
4.) Turn on/Start the video chat first before start to play video/music.

`- END, EVERYTHING HAS BEEN SETUP -`

π If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

π‘ If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="home_start")]]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
async def set_commands(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""**Κα΄ΚΚα΄α΄‘ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

**Β» κ°α΄Κ α΄Ι΄α΄α΄‘ΙͺΙ΄Ι’ α΄ α΄α΄α΄α΄α΄Ι΄α΄ ΚΙͺκ±α΄ α΄κ° ΚΚα΄α΄α΄Ι΄ α΄α΄κ±α΄ α΄Κα΄κ±κ± α΄Κα΄ Κα΄α΄α΄α΄Ι΄κ± Ι’Ιͺα΄ α΄Ι΄ Κα΄Κα΄α΄‘ α΄Ι΄α΄ Κα΄α΄α΄ α΄α΄α΄α΄α΄Ι΄α΄κ± α΄xα΄Κα΄Ι΄α΄α΄Ιͺα΄Ι΄.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π", callback_data="home_start"),
                    InlineKeyboardButton("π΅", callback_data="admin_command"),
                    InlineKeyboardButton("π₯", callback_data="admin_command"),
                    InlineKeyboardButton("π¨π»βπ»", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("α΄α΄κ±Ιͺα΄", callback_data="music_command"),
                    InlineKeyboardButton("α΄ Ιͺα΄α΄α΄", callback_data="video_command"),
                ],
                [
                    InlineKeyboardButton("κ±α΄α΄Κα΄Κ", callback_data="search_command"),
                    InlineKeyboardButton("α΄Κα΄α΄α΄", callback_data="about_command"),
                ],[
                    InlineKeyboardButton("α΄α΄α΄‘Ι΄Κα΄α΄α΄", callback_data="download_command"),
                    InlineKeyboardButton("α΄α΄Ι΄α΄", callback_data="menu_command"),
                ],[
                    InlineKeyboardButton("π₯ α΄xα΄α΄Ι΄α΄ α΄α΄Ι΄α΄ π₯", callback_data="expand_command")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("music_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Broken Music Command.

β’ /play (song name/link) - play music on video chat.

**Β© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("video_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Command list for all user.

β’ /vplay (video name/link) - play video on video chat
β’ /vstream (m3u8/yt live link) - play live stream video

**Β© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("status_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Command list for all user.

β’ /ping - show the bot ping status
β’ /uptime - show the bot uptime status
β’ /alive - show the bot alive info (in Group only)

**Β© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("lyrics_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Command list for all user.

β’ /lyric (query) - scrap the song lyric

**Β© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("search_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Command list for all user.

β’ /search (query) - search a youtube video link

**Β© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("download_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Command list for all user.

β’ /song (query) - download song from youtube

**Β© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("menu_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""βοΈ Command list for all user.

β’ /pause - pause the current track being played
β’ /resume - play the previously paused track
β’ /skip - goes to the next track
β’ /stop - stop playback of the track and clears the queue
β’ /vmute - mute the streamer userbot on group call
β’ /vunmute - unmute the streamer userbot on group call
β’ /volume `1-200` - adjust the volume of music (userbot must be admin)

** Β© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
async def set_admin(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""βοΈ Command list for group admin.

β’ /pause - pause the current track being played
β’ /resume - play the previously paused track
β’ /skip - goes to the next track
β’ /stop - stop playback of the track and clears the queue
β’ /vmute - mute the streamer userbot on group call
β’ /vunmute - unmute the streamer userbot on group call
β’ /volume `1-200` - adjust the volume of music (userbot must be admin)
β’ /reload - reload bot and refresh the admin data
β’ /userbotjoin - invite the userbot to join group
β’ /userbotleave - order userbot to leave from group

**Β© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("expand_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""**Κα΄ΚΚα΄α΄‘ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

**Β» κ°α΄Κ α΄Ι΄α΄α΄‘ΙͺΙ΄Ι’ α΄ α΄α΄α΄α΄α΄Ι΄α΄ ΚΙͺκ±α΄ α΄κ° ΚΚα΄α΄α΄Ι΄ α΄α΄κ±α΄ α΄Κα΄κ±κ± α΄Κα΄ Κα΄α΄α΄α΄Ι΄κ± Ι’Ιͺα΄ α΄Ι΄ Κα΄Κα΄α΄‘ α΄Ι΄α΄ Κα΄α΄α΄ α΄α΄α΄α΄α΄Ι΄α΄κ± α΄xα΄Κα΄Ι΄α΄α΄Ιͺα΄Ι΄.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("α΄α΄κ±Ιͺα΄", callback_data="music_command"),
                    InlineKeyboardButton("α΄ Ιͺα΄α΄α΄", callback_data="video_command"),
                ],[
                    InlineKeyboardButton("κ±α΄α΄Κα΄Κ", callback_data="search_command"),
                    InlineKeyboardButton("ΚΚΚΙͺα΄κ±", callback_data="lyrics_command"),
                ],
                [
                    InlineKeyboardButton("κ±α΄Κα΄α΄α΄", callback_data="stream_command"),
                    InlineKeyboardButton("κ±α΄α΄α΄α΄κ±", callback_data="status_command"),
                ],[
                    InlineKeyboardButton("α΄α΄α΄ΙͺΙ΄", callback_data="admin_command"),
                    InlineKeyboardButton("α΄Κα΄α΄α΄", callback_data="about_command"),
                ],[
                    InlineKeyboardButton("α΄α΄α΄‘Ι΄Κα΄α΄α΄", callback_data="download_command"),
                    InlineKeyboardButton("α΄α΄‘Ι΄α΄Κ", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("α΄α΄Ι΄α΄ κ±α΄α΄α΄ΙͺΙ΄Ι’κ±", callback_data="menu_command"),
                ],[
                    InlineKeyboardButton("π€ α΄α΄ΚΚα΄α΄κ±α΄ α΄α΄Ι΄α΄ π€", callback_data="command_list")
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("sudo_command"))
async def set_sudo(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    if user_id not in SUDO_USERS:
        await query.answer("β οΈ You don't have permissions to click this button\n\nΒ» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""βοΈ Command list for sudo user.

Β» /stats - get the bot current statistic
Β» /calls - show you the list of all active group call in database
Β» /block (`chat_id`) - use this to blacklist any group from using your bot
Β» /unblock (`chat_id`) - use this to whitelist any group from using your bot
Β» /blocklist - show you the list of all blacklisted chat
Β» /speedtest - run the bot server speedtest
Β» /sysinfo - show the system information
Β» /eval - execute any code (`developer stuff`)
Β» /sh - run any command (`developer stuff`)

β‘ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
async def set_owner(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    if user_id not in OWNER_ID:
        await query.answer("β οΈ You don't have permissions to click this button\n\nΒ» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""βοΈ Command list for bot owner.

Β» /gban (`username` or `user_id`) - for global banned people, can be used only in group
Β» /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
Β» /update - update your bot to latest version
Β» /restart - restart your bot directly
Β» /leaveall - order userbot to leave from all group
Β» /leavebot (`chat id`) - order bot to leave from the group you specify
Β» /broadcast (`message`) - send a broadcast message to all groups in bot database
Β» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin

β‘ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
async def set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("β nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
async def set_home_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
async def close_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
async def close_panel(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("βοΈ You've blocked from using this bot!", show_alert=True)
        return
    await query.message.delete()
