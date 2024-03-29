#coding=utf-8
import matplotlib.pyplot as plt
def autolabel(rects):
    for rect in rects:
        width = rect.get_width()
        if width!=0 :
            plt.text(0,rect.get_y()+rect.get_height()/2-0.1,  '%.2fw' % (int(width)/10000),color="w")

plt.rcParams['font.sans-serif']=['Microsoft Yahei']
plt.rcParams['font.serif']=['Microsoft Yahei']
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率
plt.rcParams['figure.figsize'] = (4.0, 4.0)  # 尺寸


res_path='D:/project/qq_rob/pcr_robot/resource/'
record=open(res_path+'record/2020-05-17.txt','r',encoding='utf-8')
record_list=record.readlines()
record.close()
print(record_list)
boss_list = [0,0,0,0,0]
for line in record_list:
    line_list=line.split(' ')
    print(line_list)
    if line_list[0] == '摸鱼1号':
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

print(boss_list)
#获得伤害总量
sum = 0
for num in boss_list:
    sum += num
    
boss_list.insert(0,sum)
boss_name=['总伤害','老一','老二','老三','老四','老五']
#生成柱状图
barh=plt.barh(range(len(boss_list)),boss_list,tick_label=boss_name)
plt.title('2020-05-17摸鱼怪伤害统计')
print(barh)
autolabel(barh)

plt.savefig(res_path+'chart_image/result.png')