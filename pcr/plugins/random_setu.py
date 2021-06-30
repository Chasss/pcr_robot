# ##coding=utf-8
# from nonebot import on_command, CommandSession
# import datetime
# import os
# import random

# @on_command('random_setu',aliases=('来张色图'),only_to_me=False)
# async def random_setu(session: CommandSession):
#     pic_num=random.randint(0,5)
#     message='[CQ:image,file='+str(pic_num)+'.jpg]'
#     await session.send(message)