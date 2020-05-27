##coding=utf-8
from nonebot import on_command, CommandSession
import datetime
import os

res_path='D:/project/qq_rob/pcr_robot/resource/'
today = datetime.date.today().strftime('%Y-%m-%d')
members=open(res_path+'members.txt','r',encoding='utf-8')
members_list=members.readlines()
members.close()


def is_name_in_members(name):

    for n in members_list:
        n=n.strip()
        ns=n.split(' ')
        if ns[0] == name:
            return True
    return False


@on_command('record',aliases=('记录'),only_to_me=False)
async def record(session: CommandSession):
    #从会话状态获取info:id boss名称 造成伤害
    info = session.get('info')
    record_result = await record_info(info)
    await session.send(record_result)

#将函数声明为record命令的参数解释器
@record.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    info = stripped_arg.split(' ')
    info.append('')
    info.append('')
    info.append('')
    name = info[0]
    boss = info[1]
    atk = info[2]
    if not (name and boss and atk):
        session.finish('记录失败：玩家名字/BOSS编号/伤害不能为空')
    if not is_name_in_members(name):
        session.finish('记录失败：该名字不在目前成员中')
    if not atk.isdigit():
        session.finish('记录失败：伤害数字格式不正确')
    if not boss.isdigit():
        session.finish('记录失败：BOSS编号应为1-5的整数')
    if int(boss)<1 or int(boss)>5:
        print(int(boss))
        session.finish('记录失败：BOSS编号应为1-5的整数')

    session.state['info'] = stripped_arg

    
async def record_info(info: str) -> str:
    today = datetime.date.today().strftime('%Y-%m-%d')
    pcr_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    record_file=open('D:/project/qq_rob/pcr_robot/resource/record/'+today+'.txt','a',encoding='utf-8')
    record_file.write(f'{info}'+'\n')
    record_file.close()
    return '记录成功: '+today+f' {info}'