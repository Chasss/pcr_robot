##coding=utf-8
from nonebot import on_command, CommandSession
import datetime
import os

res_path='D:/project/qq_rob/pcr_robot/resource/'
today = datetime.date.today().strftime('%Y-%m-%d')
# members=open(res_path+'members.txt','r',encoding='utf-8')
# members_list=members.readlines()
# members.close()


# def is_name_in_members(name):

#     for n in members_list:
#         n=n.strip()
#         ns=n.split(' ')
#         if ns[0] == name:
#             return True
#     return False
def get_today():

    today = datetime.date.today().strftime('%Y-%m-%d')
    yestoday = (datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    hours_now = datetime.datetime.now().strftime('%H')
    if int(hours_now)>=0 and int(hours_now)<5 :
        return yestoday
    return today

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
@on_command('police',aliases=('出警'),only_to_me=False)
async def police(session: CommandSession):
    today = get_today()
    lazy_members = get_lazy_members(today)
    hour_now = datetime.datetime.now().strftime('%H')
    time_now = datetime.datetime.now().strftime('%H:%M')
    if int(hour_now) > 18:
        message = '现在时间是'+time_now+',出刀警察出动\n检测到'+lazy_members+'今日还未记录或出满三刀'
        await session.send(message)
    else:
        await session.send('时间过早，出刀警察还没有上班。')
    
