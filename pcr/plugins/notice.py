#coding=utf-8

import datetime
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

res_path='D:/project/qq_rob/pcr_robot/resource/'
today = datetime.date.today().strftime('%Y-%m-%d')


#检测今日未记录完三刀的成员
def get_lazy_members(date):
    
    #获得成员名称
    members=open(res_path+'members.txt','r',encoding='utf-8')
    members_list=members.readlines()
    members.close()

    #获得选定日期的伤害记录
    record=open(res_path+'record/'+date+'.txt','r',encoding='utf-8')
    record_list=record.readlines()
    record.close()

    #出刀次数与名字的字典
    attack_times={}
    for name in members_list:
        name=name.strip()
        names=name.split(' ')
        attack_times[names[0]] = 0
    
    print(attack_times)

    #统计出刀次数
    for info in record_list:
        info_list=info.split(' ')
        attack_times[info_list[0]] += 1
    
    
    #统计不满三刀人员
    lazy_members=''
    for name in members_list:
        name=name.strip()
        names=name.split(' ')
        if attack_times[names[0]] < 3:
            lazy_members += '[CQ:at,qq='+names[1]+']'

    return lazy_members


@nonebot.scheduler.scheduled_job('cron', hour=2,minute=0)
async def _():
    bot = nonebot.get_bot()
    today = datetime.date.today().strftime('%Y-%m-%d')
    lazy_members=get_lazy_members(today)
    try:
        await bot.send_group_msg(group_id=1084228533,
                                 message='现在是2点整,出刀警察出动\n检测到'+lazy_members+'今日还未记录或出满三刀')
    except CQHttpError:
        pass