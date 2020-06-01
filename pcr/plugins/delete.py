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


@on_command('delete',aliases=('删除'),only_to_me=False)
async def delete(session: CommandSession):
    #从会话状态获取info:id boss名称 造成伤害
    info = session.get('info')
    delete_result = await delete_info(info)
    await session.send(delete_result)

#将函数声明为delete命令的参数解释器
@delete.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    session.state['info'] = stripped_arg

    
async def delete_info(info: str) -> str:
    today = get_today()
    is_delete = False
    with open(res_path+'record/'+today+'.txt','r',encoding='utf-8') as rf :
        lines = rf.readlines()
    with open(res_path+'record/'+today+'.txt','w',encoding='utf-8') as rf_w :
        for line in lines :
            if line == info+'\n' and is_delete == False:
                is_delete = True
                continue
            rf_w.write(line)
    if is_delete:
        return '删除成功: '+today+f' {info}'
    return '删除失败：未查找到该记录'