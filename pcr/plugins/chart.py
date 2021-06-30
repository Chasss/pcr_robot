#coding=utf-8
from nonebot import on_command, CommandSession
import datetime
import os
import matplotlib.pyplot as plt
from aiocqhttp import MessageSegment

def autolabel(rects):
    for rect in rects:
        width = rect.get_width()
        if width!=0 :
            plt.text(0,rect.get_y()+rect.get_height()/2-0.1,  '%.2fw' % (int(width)/10000))

plt.rcParams['font.sans-serif']=['Microsoft Yahei']
plt.rcParams['font.serif']=['Microsoft Yahei']
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率
plt.rcParams['figure.figsize'] = (4.0, 4.0)  # 尺寸

res_path='D:/project/qq_rob/pcr_robot/resource/'
today = datetime.date.today().strftime('%Y-%m-%d')

@on_command('chart',aliases=('图表统计'),only_to_me=False)
async def chart(session: CommandSession):
    #从会话状态获取人员名称和日期
    info = session.get('info')
    record_result = await get_chart(info)
    # seq=MessageSegment.image(res_path+'chart_image/result.png')
    await session.send(record_result)
    image=('[CQ:image,file=result.png]')
    await session.send(image)

#将函数声明为record命令的参数解释器
@chart.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    # info=stripped_arg.split(' ')
    # _name=info[0]
    # _time=info[1]
    # if _name and _time:
    #     session.state['name'] = _name
    #     session.state['time'] = _time

    # if not _name and _time:
    #     session.pause("名字或时间不能为空")
    if stripped_arg:
        session.state['info'] = stripped_arg

    if not stripped_arg:
        session.pause("不能为空")

async def get_chart(info: str) -> MessageSegment:
    info_str=f'{info}'
    info_list=info_str.split(' ')
    name=info_list[0]
    ctime=info_list[1]
    if ctime == '全程':
        return MessageSegment.text('全程填坑中')
    

    else:
        if os.path.exists(res_path+'record/'+ctime+'.txt') :
            record=open(res_path+'record/'+ctime+'.txt','r',encoding='utf-8')
            record_list=record.readlines()
            record.close()
        else:
            return MessageSegment.text('该日期未记录')
    
    #获得当前日期该玩家的各BOSS伤害
    boss_list = [0,0,0,0,0]
    print(record_list)
    #统计伤害
    for line in record_list:
        line_list=line.split(' ')
        if line_list[0] == name:
            if line_list[1] == '1' :
                boss_list[0] += int(line_list[2])
            if line_list[1] == '2' :
                boss_list[1] += int(line_list[2])
            if line_list[1] == '3' :
                boss_list[2] += int(line_list[2])
            if line_list[1] == '4' :
                boss_list[3] += int(line_list[2])
            if line_list[1] == '5' :
                boss_list[4] += int(line_list[2])

    #获得伤害总量
    sum = 0
    for num in boss_list:
        sum += num
    
    boss_list.insert(0,sum)
    boss_name=['总伤害','boss1','boss2','boss3','boss4','boss5']
    #生成柱状图
    barh=plt.barh(range(len(boss_list)),boss_list,tick_label=boss_name)
    plt.title(ctime+name+'伤害统计')
    autolabel(barh)
    plt.savefig('D:/project/qq_rob/go-cqhttp-v0.9.19-windows-amd64/data/images/result.png')
    plt.close('all') 
    return MessageSegment.text('制图成功')