# ##coding=utf-8
# from nonebot import on_command, CommandSession, permission
# import datetime
# import os
# from aiocqhttp.exceptions import Error as CQHttpError
# res_path='D:/project/qq_rob/pcr_robot/resource/'
# today = datetime.date.today().strftime('%Y-%m-%d')
# members=open(res_path+'members.txt','r',encoding='utf-8')
# members_list=members.readlines()
# members.close()


# # def is_name_in_members(name):

# #     for n in members_list:
# #         n=n.strip()
# #         ns=n.split(' ')
# #         if ns[0] == name:
# #             return True
# #     return False

# @on_command('notice_all',aliases=('通知'),permission=permission.SUPERUSER ,only_to_me=False)
# async def notice_all(session: CommandSession):
#     message = session.get('info')
#     # for n in members_list:
#     #      n=n.strip()
#     #      ns=n.split(' ')
#     #      if ns[0]=='陈皮':
#     #          await session.send(ns[0])
#     await session.bot.send_private_msg(user_id=2817878659, message='test')
#     await session.bot.send_private_msg(user_id=2386432182, message='test')
#     #await session.send('已私聊通知所有群员')

# @notice_all.args_parser
# async def _(session: CommandSession):
#     stripped_arg = session.current_arg_text.strip()
#     session.state['info'] = stripped_arg
