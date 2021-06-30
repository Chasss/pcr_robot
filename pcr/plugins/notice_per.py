# #coding=utf-8

# import datetime
# import nonebot
# import pytz
# from aiocqhttp.exceptions import Error as CQHttpError

# res_path='D:/project/qq_rob/pcr_robot/resource/'
# today = datetime.date.today().strftime('%Y-%m-%d')




# @nonebot.scheduler.scheduled_job('cron', hour=13,minute=22)
# async def _():
#     bot = nonebot.get_bot()
#     #today = datetime.date.today().strftime('%Y-%m-%d')
#     #lazy_members=get_lazy_members(today)
#     try:
#         await bot.send_private_msg(user_id=2817878659, message='13：22定时私发消息测试！')
#         await bot.send_private_msg(user_id=2386432182, message='13：22定时私发消息测试！')
#         await bot.send_private_msg(user_id=292687588, message='13：22定时私发消息测试！')
#     except CQHttpError:
#         pass