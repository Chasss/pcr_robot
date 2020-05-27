#coding=utf-8

from nonebot import on_command, CommandSession
import datetime
import os
from aiocqhttp import MessageSegment

res_path='D:/project/qq_rob/pcr_robot/resource/'
intro1=open(res_path+'introduce_1.txt','r',encoding='utf-8')
introduce_text1=str(intro1.read())
intro1.close()

intro2=open(res_path+'introduce_2.txt','r',encoding='utf-8')
introduce_text2=str(intro2.read())
intro2.close()

@on_command('introduce',aliases=('使用说明'),only_to_me=False)
async def introduce(session: CommandSession):
    await session.send(introduce_text1)
    await session.send(introduce_text2)